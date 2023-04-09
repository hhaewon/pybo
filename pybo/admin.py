from django.contrib import admin
from .models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin[Question]):
    search_fields = ["subject"]


admin.site.register(Answer)
