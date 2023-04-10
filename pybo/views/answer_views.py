from typing import cast
from functools import partial

from django.http import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404, resolve_url
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator

from ..models import Answer, Question
from ..forms import AnswerForm


@method_decorator(partial(login_required, login_url="common:login"), name="dispatch")
class AnswerCreateView(View):
    template_name = "pybo/question_detail.html"

    def post(self, request: HttpRequest, question_id: int):
        question = get_object_or_404(Question, pk=question_id)
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = cast(Answer, form.save(commit=False))
            answer.question = question
            answer.author = cast(User, request.user)
            answer.save()
            url = resolve_url("pybo:detail", question_id=question.question_id)
            return redirect(f"{url}#answer_{answer.answer_id}")
        else:
            context = {"question": question, "form": form}
            return render(
                request=request,
                template_name=self.template_name,
                context=context,
            )

    def get(self, request: HttpRequest, question_id: int):
        question = get_object_or_404(Question, pk=question_id)
        form = AnswerForm()
        context = {"question": question, "form": form}
        return render(
            request=request, template_name=self.template_name, context=context
        )


@method_decorator(partial(login_required, login_url="common:login"), name="dispatch")
class AnswerModifyView(View):
    template_name = "pybo/answer_form.html"

    def post(self, request: HttpRequest, answer_id: int):
        answer = get_object_or_404(Answer, pk=answer_id)
        if request.user != answer.author:
            messages.error(request, "수정권한이 없습니다")
            url = resolve_url("pybo:detail", question_id=answer.question_id)
            return redirect(f"{url}#answer_{answer.answer_id}")

        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.save()
            url = resolve_url("pybo:detail", question_id=answer.question_id)
            return redirect(f"{url}#answer_{answer.answer_id}")

    def get(self, request: HttpRequest, answer_id: int):
        answer = get_object_or_404(Answer, pk=answer_id)
        form = AnswerForm(instance=answer)
        context = {"form": form, "answer": answer}
        return render(
            request=request, template_name=self.template_name, context=context
        )


@method_decorator(partial(login_required, login_url="common:login"), name="dispatch")
class AnswerDeleteView(View):
    def get(self, request: HttpRequest, answer_id: int):
        answer = get_object_or_404(Answer, pk=answer_id)
        if request.user != answer.author:
            messages.error(request, "삭제권한이 없습니다")
        else:
            answer.delete()
        return redirect("pybo:detail", question_id=answer.question.question_id)


@method_decorator(partial(login_required, login_url="common:login"), name="dispatch")
class AnswerVoteView(View):
    def get(self, request: HttpRequest, answer_id: int):
        answer = get_object_or_404(Answer, pk=answer_id)

        if request.user == answer.author:
            messages.error(request, "본인이 작성한 글은 추천할수 없습니다")
        else:
            answer.voter.add(request.user)
        url = resolve_url("pybo:detail", question_id=answer.question_id)
        return redirect(f"{url}#answer_{answer.answer_id}")
