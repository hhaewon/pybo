from typing import Any, cast

from django.http import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

# from django.views import View
from django.views.generic import ListView, DetailView

from .models import Answer, Question
from .forms import AnswerForm, QuestionForm


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


class CreateAnswerView(View):
    def post(self, request: HttpRequest, question_id: int):
        question = get_object_or_404(Question, pk=question_id)
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = cast(Answer, form.save(commit=False))
            print(type(answer))
            answer.question = question
            answer.save()
            return redirect("pybo:detail", question_id=question_id)
        else:
            context = {"question": question, "form": form}
            return render(
                request=request,
                template_name="pybo/question_detail.html",
                context=context,
            )


class CreateQuestionView(View):
    template_name = "pybo/question_form.html"

    def post(self, request: HttpRequest):
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect("pybo:index")
        else:
            return render(
                request=request,
                template_name=self.template_name,
                context={"form": form},
            )

    def get(self, request: HttpRequest):
        form = QuestionForm()
        context = {"form": form}
        return render(
            request=request, template_name=self.template_name, context=context
        )
