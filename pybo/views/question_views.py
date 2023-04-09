from typing import cast
from functools import partial

from django.http import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator

from ..models import Question
from ..forms import QuestionForm


@method_decorator(partial(login_required, login_url="common:login"), name="dispatch")
class QuestionCreateView(View):
    template_name = "pybo/question_form.html"

    def post(self, request: HttpRequest):
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = cast(Question, form.save(commit=False))
            question.author = cast(User, request.user)
            question.save()
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


@method_decorator(partial(login_required, login_url="common:login"), name="dispatch")
class QuestionUpdateView(View):
    template_name = "pybo/question_form.html"

    def post(self, request: HttpRequest, question_id: int):
        question = get_object_or_404(Question, pk=question_id)
        if request.user != question.author:
            messages.error(request, "수정권한이 없습니다")
            return redirect("pybo:detail", question_id=question_id)
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect("pybo:detail", question_id=question_id)

    def get(self, request: HttpRequest, question_id: int):
        question = get_object_or_404(Question, pk=question_id)
        form = QuestionForm(instance=question)
        context = {"form": form}
        return render(
            request=request, template_name=self.template_name, context=context
        )


@method_decorator(partial(login_required, login_url="common:login"), name="dispatch")
class QuestionDeleteView(View):
    def get(self, request: HttpRequest, question_id: int):
        question = get_object_or_404(Question, pk=question_id)
        if request.user != question.author:
            messages.error(request, "삭제권한이 없습니다")
            return redirect("pybo:detail", question_id=question.id)
        question.delete()
        return redirect("pybo:index")
