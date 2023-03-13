from django.shortcuts import render
from django.views.generic import ListView

from boosts.models import Statement
from config.settings.common import THE_SITE_NAME

STATEMENTS_PAGE_TITLE = "Statements"


class StatementListView(ListView):
    """
    ListView for the Statement model.
    """

    paginate_by = 5

    # We are not using 'model = Statement' attribute since we want only the `Statements` for the current user.
    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Statement.objects.filter(
                author=self.request.user
            ).order_by("-created")
            return queryset
        else:
            queryset = Statement.objects.none()
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = STATEMENTS_PAGE_TITLE
        context["the_site_name"] = THE_SITE_NAME
        return context
