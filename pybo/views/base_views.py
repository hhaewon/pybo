from typing import Any
from django.views.generic import ListView, DetailView

from ..models import Question


class QuestionListView(ListView):
    model = Question
    template_name = "pybo/question_list.html"
    paginate_by = 15
    paginate_orphans = 3

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        page = context["page_obj"]
        paginator = page.paginator
        pagelist = paginator.get_elided_page_range(
            page.number, on_each_side=3, on_ends=0
        )
        context["pagelist"] = pagelist
        return context


class QuestionDetailView(DetailView):
    model = Question
    pk_url_kwarg = "question_id"
