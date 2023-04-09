from django.urls import path

from . import views

app_name = "pybo"

urlpatterns = [
    path("", views.QuestionListView.as_view(), name="index"),
    path(
        "questions/<int:question_id>", views.QuestionDetailView.as_view(), name="detail"
    ),
    path(
        "questions/<int:question_id>/answers",
        views.CreateAnswerView.as_view(),
        name="create_answer",
    ),
    path("questions", views.CreateQuestionView.as_view(), name="create_question"),
]
