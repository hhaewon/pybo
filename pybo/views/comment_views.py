from typing import cast
from functools import partial

from django.http import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404, resolve_url
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator

from ..models import Answer, Comment, Question
from ..forms import CommentForm


@method_decorator(partial(login_required, login_url="common:login"), name="dispatch")
class CommentCreateQuestionView(View):
    template_name = "pybo/comment_form.html"

    def post(self, request: HttpRequest, question_id: int):
        question = get_object_or_404(Question, pk=question_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = cast(Comment, form.save(commit=False))
            comment.question = question
            comment.author = cast(User, request.user)
            comment.save()
            return redirect("pybo:detail", question_id=question_id)
        else:
            context = {"form": form}
            return render(
                request=request,
                template_name=self.template_name,
                context=context,
            )

    def get(self, request: HttpRequest, question_id: int):
        form = CommentForm()
        context = {"form": form}
        return render(
            request=request, template_name=self.template_name, context=context
        )


@method_decorator(partial(login_required, login_url="common:login"), name="dispatch")
class CommentModifyQuestionView(View):
    template_name = "pybo/comment_form.html"

    def post(self, request: HttpRequest, comment_id: int):
        comment = get_object_or_404(Comment, pk=comment_id)
        comment.question = cast(Question, comment.question)
        if request.user != comment.author:
            messages.error(request, "수정권한이 없습니다")
            return redirect("pybo:detail", question_id=comment.question.question_id)

        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = cast(Comment, form.save(commit=False))
            comment.question = cast(Question, comment.question)
            comment.save()
            return redirect("pybo:detail", question_id=comment.question.question_id)
        else:
            form = CommentForm(instance=comment)
            context = {"form": form}
            return render(
                request=request, template_name=self.template_name, context=context
            )

    def get(self, request: HttpRequest, comment_id: int):
        comment = get_object_or_404(Comment, pk=comment_id)
        form = CommentForm(instance=comment)
        context = {"form": form}
        return render(
            request=request, template_name=self.template_name, context=context
        )


@method_decorator(partial(login_required, login_url="common:login"), name="dispatch")
class CommentDeleteQuestionView(View):
    def get(self, request: HttpRequest, comment_id: int):
        comment = get_object_or_404(Comment, pk=comment_id)
        comment.question = cast(Question, comment.question)
        if request.user != comment.author:
            messages.error(request, "삭제권한이 없습니다")
            return redirect("pybo:detail", question_id=comment.question.question_id)

        comment.delete()
        return redirect("pybo:detail", question_id=comment.question.question_id)


@method_decorator(partial(login_required, login_url="common:login"), name="dispatch")
class CommentCreateAnswerView(View):
    template_name = "pybo/comment_form.html"

    def post(self, request: HttpRequest, answer_id: int):
        answer = get_object_or_404(Answer, pk=answer_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = cast(Comment, form.save(commit=False))
            comment.answer = answer
            comment.author = cast(User, request.user)
            comment.save()
            return redirect(
                "pybo:detail", question_id=comment.answer.question.question_id
            )
        else:
            context = {"form": form}
            return render(
                request=request,
                template_name=self.template_name,
                context=context,
            )

    def get(self, request: HttpRequest, answer_id: int):
        form = CommentForm()
        context = {"form": form}
        return render(
            request=request, template_name=self.template_name, context=context
        )


@method_decorator(partial(login_required, login_url="common:login"), name="dispatch")
class CommentModifyAnswerView(View):
    template_name = "pybo/comment_form.html"

    def post(self, request: HttpRequest, comment_id: int):
        comment = get_object_or_404(Comment, pk=comment_id)
        comment.answer = cast(Answer, comment.answer)
        if request.user != comment.author:
            messages.error(request, "수정권한이 없습니다")
            url = resolve_url(
                "pybo:detail", question_id=comment.answer.question.question_id
            )
            return redirect(f"{url}#answer_{comment.answer.answer_id}")

        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = cast(Comment, form.save(commit=False))
            comment.answer = cast(Answer, comment.answer)
            comment.save()
            url = resolve_url(
                "pybo:detail", question_id=comment.answer.question.question_id
            )
            return redirect(f"{url}#answer_{comment.answer.answer_id}")
        else:
            form = CommentForm(instance=comment)
            context = {"form": form}
            return render(
                request=request, template_name=self.template_name, context=context
            )

    def get(self, request: HttpRequest, comment_id: int):
        comment = get_object_or_404(Comment, pk=comment_id)
        form = CommentForm(instance=comment)
        context = {"form": form}
        return render(
            request=request, template_name=self.template_name, context=context
        )


@method_decorator(partial(login_required, login_url="common:login"), name="dispatch")
class CommentDeleteAnswerView(View):
    def get(self, request: HttpRequest, comment_id: int):
        comment = get_object_or_404(Comment, pk=comment_id)
        comment.answer = cast(Answer, comment.answer)
        if request.user != comment.author:
            messages.error(request, "삭제권한이 없습니다")
            url = resolve_url(
                "pybo:detail", question_id=comment.answer.question.question_id
            )
            return redirect(f"{url}#answer_{comment.answer.answer_id}")

        comment.delete()
        url = resolve_url(
            "pybo:detail", question_id=comment.answer.question.question_id
        )
        return redirect(f"{url}#answer_{comment.answer.answer_id}")
