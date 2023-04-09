from __future__ import annotations

from django.db import models
from django.urls import reverse


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    question_id = models.AutoField(primary_key=True)
    answers: models.QuerySet[Answer]

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "question"
        verbose_name_plural = "questions"

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("pybo:detail", args=[self.question_id])


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    answer_id = models.AutoField(primary_key=True)

    class Meta:
        verbose_name = "answer"
        verbose_name_plural = "answers"

    def get_absolute_url(self):
        return reverse("answer_detail", args=[self.answer_id])
