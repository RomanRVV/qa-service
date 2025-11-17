from django.contrib import admin
from .models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'created_at']
    readonly_fields = ['created_at']
    list_filter = ['created_at']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'text']
    readonly_fields = ['created_at']
    list_filter = ['question', 'created_at']
