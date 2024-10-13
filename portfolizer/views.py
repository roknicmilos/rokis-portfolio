from django.urls import reverse
from django.views.generic import TemplateView

from apps.common.utils import get_model_admin_change_list_url
from apps.portfolio.models import Portfolio


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["portfolio_url"] = self._get_portfolio_url()
        return context

    def _get_portfolio_url(self) -> str:
        if portfolio := self.request.user.published_portfolio:
            return reverse(
                viewname="portfolio:index", kwargs={"slug": portfolio.slug}
            )

        return get_model_admin_change_list_url(model_class=Portfolio)
