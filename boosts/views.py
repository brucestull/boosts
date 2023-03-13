from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from boosts.models import Statement
from config.settings.common import THE_SITE_NAME
from boosts.forms import StatementForm

STATEMENT_LIST_PAGE_TITLE = "Statements"
STATEMENT_CREATE_PAGE_TITLE = "Create a Statement"


class StatementListView(ListView):
    """
    ListView for the Statement model.
    """

    paginate_by = 10

    # We are not using 'model = Statement' attribute since we want only
    # the `Statements` for the current user.
    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Statement.objects.filter(author=self.request.user).order_by(
                "-created"
            )
            return queryset
        else:
            queryset = Statement.objects.none()
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = STATEMENT_LIST_PAGE_TITLE
        context["the_site_name"] = THE_SITE_NAME
        return context


class StatementCreateView(CreateView):
    """
    CreateView for the Statement model.
    """

    form_class = StatementForm
    template_name = "boosts/statement_form.html"
    success_url = reverse_lazy("boosts:statement-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = STATEMENT_CREATE_PAGE_TITLE
        context["the_site_name"] = THE_SITE_NAME
        context["hide_statement_create_link"] = True
        return context
