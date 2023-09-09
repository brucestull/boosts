from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

import os

from accounts.models import CustomUser
from boosts.forms import InspirationalForm
from boosts.models import Inspirational
from boosts.models import InspirationSent
from config.settings.common import THE_SITE_NAME

# Define the page titles:
INSPIRATIONAL_LIST_PAGE_TITLE = "Inspirationals"
INSPIRATIONAL_CREATE_PAGE_TITLE = "Create an Inspirational"


class InspirationalListView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    ListView,
):
    """
    ListView for the Inspirational model.

    This view is only accessible to users who have `registration_accepted=True`.
    This is controlled by the `UserPassesTestMixin` and the `test_func` method.

    Mixins:
        LoginRequiredMixin: Ensures that the user is logged in. If not, they
        are redirected to the login page.
        UserPassesTestMixin: Ensures that the user has `registration_accepted=True`.
        If not, they are prompted to login.

    Attributes:
        paginate_by (int): The number of objects to display per page.

    Methods:
        test_func: Test if user has `registration_accepted=True`. Only users
        who pass this test can access this view.
        get_queryset: Get the queryset for the view. Only the `Inspirational`
        objects for the current user are returned.
        get_context_data: Override the `get_context_data` method to add the
        page title and the site name to the context.
    """

    paginate_by = 10

    def test_func(self):
        """
        Test if user has `registration_accepted=True`. Only users who pass this
        test can access this view.

        This function is used by the `UserPassesTestMixin` to control access to
        this view.
        """
        return self.request.user.registration_accepted

    # We are not using 'model = Inspirational' attribute since we want only
    # the `Inspirationals` for the current user.
    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Inspirational.objects.filter(
                author=self.request.user,
            ).order_by("-created")
            return queryset
        else:
            queryset = Inspirational.objects.none()
            return queryset

    def get_context_data(self, **kwargs):
        """
        Override the `get_context_data` method to add the page title and the site name to the context.
        """
        context = super().get_context_data(**kwargs)
        context["page_title"] = INSPIRATIONAL_LIST_PAGE_TITLE
        context["the_site_name"] = THE_SITE_NAME
        return context


class InspirationalCreateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    CreateView,
):
    """
    CreateView for the Inspirational model.
    """

    form_class = InspirationalForm
    template_name = "boosts/inspirational_form.html"
    success_url = reverse_lazy("boosts:inspirational-list")

    def test_func(self):
        """
        Test if user has `registration_accepted=True`. Only users who pass
        this test can access this view.

        This function is used by the `UserPassesTestMixin` to control access
        to this view.
        """
        return self.request.user.registration_accepted

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = INSPIRATIONAL_CREATE_PAGE_TITLE
        context["the_site_name"] = THE_SITE_NAME
        # Hide the "Create Inspirational" link in the navbar since we are
        # already on the page.
        context["hide_inspirational_create_link"] = True
        return context


# TODO: Add permissions for this view, using decorators.
def send_inspirational(request, pk):
    """
    Send an inspirational quote to the User's Beastie (a User which has
    been designated as the User's Beastie).
    """
    try:
        # Get the inspirational quote from the pk sent in the URL:
        inspirational = get_object_or_404(Inspirational, pk=pk)
        # Get the current site domain. This will resolve to a localhost in DEV
        # and to the production domain in PROD:
        current_site = get_current_site(request)
        plain_text_body = f"""
                {inspirational.created.strftime("%y-%m-%d")} - {inspirational.body}
                \n
                Sent from https://{current_site.domain} by {request.user.username} ({request.user.email}).
            """
        # Send the inspirational quote to the user's beastie:
        send_mail(
            f"Inspirational Quote from your Beastie: {request.user.username}",
            plain_text_body,
            request.user.email,
            [request.user.beastie.email],
            # html_message=plain_text_body,
            fail_silently=False,
        )
        inspirational_sent = InspirationSent.objects.create(
            inspirational=inspirational,
            inspirational_text=inspirational.body,
            sender=request.user,
            beastie=request.user.beastie,
        )
        print(f"inspirational_sent: {inspirational_sent}")
        messages.success(
            request,
            f"Sent '{inspirational.body[:20]}...' to your Beastie: {request.user.beastie.username}!",
        )
        return redirect("boosts:inspirational-list")
    except ValidationError as e:
        messages.error(request, str(e))
        return redirect("boosts:inspirational-list")
    except Exception as e:
        messages.error(
            request, "An error occurred while sending the inspirational quote."
        )
        return redirect("boosts:inspirational-list")


class BretBeastieInspirationalListView(ListView):
    paginate_by = 10

    # We are not using 'model = Inspirational' attribute since we want only
    # the `Inspirationals` for the example user.
    def get_queryset(self):
        """
        Override the `get_queryset` method to return only the `Inspirational`s for the example user named "BretBeastie".
        """
        bret_beastie = CustomUser.objects.get(username="BretBeastie")
        queryset = Inspirational.objects.filter(
            author=bret_beastie,
        ).order_by("-created")
        return queryset

    def get_context_data(self, **kwargs):
        """
        Override the `get_context_data` method to add the page title and the site name to the context.
        """
        context = super().get_context_data(**kwargs)
        context["page_title"] = INSPIRATIONAL_LIST_PAGE_TITLE
        context["the_site_name"] = THE_SITE_NAME
        return context


def landing_view(request):
    """
    This view checks is the user is authenticated.

    If they are, they are routed to their own `InspirationalListView`.

    If they are not, they are routed to the `BretBeastieInspirationalListView`.
    """
    if request.user.is_authenticated:
        return InspirationalListView.as_view()(request)
    else:
        return BretBeastieInspirationalListView.as_view()(request)
