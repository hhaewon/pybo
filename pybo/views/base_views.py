from typing import Any

from django.views.generic import ListView, DetailView
from django.db.models import Q

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
        context["page"] = self.request.GET.get("page", "1")
        context["kw"] = self.request.GET.get("kw", "")
        return context

    def get_queryset(self):
        kw = self.request.GET.get("kw", "")

        question_list = Question.objects.order_by("-created_at")
        print(kw)
        if kw:
            question_list = question_list.filter(
                Q(subject__icontains=kw)
                | Q(content__icontains=kw)  # 제목 검색
                | Q(question_answer__content__icontains=kw)  # 내용 검색
                | Q(question_answer__content__icontains=kw)  # 답변 내용 검색
                | Q(question_answer__content__icontains=kw)  # 질문 글쓴이 검색  # 답변 글쓴이 검색
            ).distinct()
            return question_list
        return question_list


class QuestionDetailView(DetailView):
    model = Question
    pk_url_kwarg = "question_id"
