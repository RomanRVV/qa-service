from django.db import models


class Question(models.Model):
    text = models.TextField(verbose_name="Текст вопроса")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self) -> str:
        return f"Вопрос - {self.id}: {self.text}"


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        related_name="answers",
        on_delete=models.CASCADE,
        verbose_name="Вопрос"
    )
    text = models.TextField(verbose_name="Текст ответа")
    user_id = models.UUIDField(verbose_name="Идентификатор пользователя")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self) -> str:
        return f"Ответ - {self.id}: {self.text} на вопрос {self.question.text}"
