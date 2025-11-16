from django.db import models


class Question(models.Model):
    text = models.TextField(verbose_name="Текст вопроса")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return f"Вопрос - {self.id}: {self.text}"


class Answer(models.Model):
    ...
