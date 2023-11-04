from django.views.generic import TemplateView

from config.settings import THE_SITE_NAME

# Define the page titles:
INSPIRATIONAL_LIST_PAGE_TITLE = "Inspirationals"
INSPIRATIONAL_CREATE_PAGE_TITLE = "Create an Inspirational"


class ForbiddenView(TemplateView):
    """
    View for the 403 Forbidden page.
    """

    # Define the template used by this view:
    # This template is located at `templates/403.html`
    template_name = "403.html"

    def get_context_data(self, **kwargs):
        """
        Override the `get_context_data` method to add the page title and
        the site name to the context.
        """
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Forbidden"
        context["the_site_name"] = THE_SITE_NAME
        return context
