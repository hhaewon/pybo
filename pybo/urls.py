from django.urls import path

from .views import base_views, question_views, answer_views, comment_views

app_name = "pybo"

urlpatterns = [
    path("", base_views.QuestionListView.as_view(), name="index"),
    path("<int:question_id>/", base_views.QuestionDetailView.as_view(), name="detail"),
    path(
        "questions/create/",
        question_views.QuestionCreateView.as_view(),
        name="create_question",
    ),
    path(
        "questions/modify/<int:question_id>",
        question_views.QuestionUpdateView.as_view(),
        name="modify_question",
    ),
    path(
        "question/delete/<int:question_id>",
        question_views.QuestionDeleteView.as_view(),
        name="delete_question",
    ),
    path(
        "question/vote/<int:question_id>/",
        question_views.QuestionVoteView.as_view(),
        name="question_vote",
    ),
    path(
        "answers/create/<int:question_id>/",
        answer_views.AnswerCreateView.as_view(),
        name="create_answer",
    ),
    path(
        "answer/modify/<int:answer_id>",
        answer_views.AnswerModifyView.as_view(),
        name="modify_answer",
    ),
    path(
        "answer/delete/<int:answer_id>/",
        answer_views.AnswerDeleteView.as_view(),
        name="delete_answer",
    ),
    path(
        "answer/vote/<int:answer_id>/",
        answer_views.AnswerVoteView.as_view(),
        name="answer_vote",
    ),
    path(
        "comment/create/question/<int:question_id>/",
        comment_views.CommentCreateQuestionView.as_view(),
        name="comment_create_question",
    ),
    path(
        "comment/modify/question/<int:comment_id>/",
        comment_views.CommentModifyQuestionView.as_view(),
        name="comment_modify_question",
    ),
    path(
        "comment/delete/question/<int:comment_id>/",
        comment_views.CommentDeleteQuestionView.as_view(),
        name="comment_delete_question",
    ),
    path(
        "comment/create/answer/<int:answer_id>/",
        comment_views.CommentCreateAnswerView.as_view(),
        name="comment_create_answer",
    ),
    path(
        "comment/modify/answer/<int:comment_id>/",
        comment_views.CommentModifyAnswerView.as_view(),
        name="comment_modify_answer",
    ),
    path(
        "comment/delete/answer/<int:comment_id>/",
        comment_views.CommentDeleteAnswerView.as_view(),
        name="comment_delete_answer",
    ),
]
