from ninja import NinjaAPI
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from .models import Answer, Question
from .schema import (
    AnswerRequest,
    AnswerResponse,
    QuestionRequest,
    QuestionResponse,
)
import logging


logger = logging.getLogger("QA_API")

api = NinjaAPI()


@api.get("/questions/", response=list[QuestionResponse])
def get_questions(request: HttpRequest) -> list[QuestionResponse]:
    """
    Retrieve a list of all questions.
    """
    questions = Question.objects.prefetch_related("answers").all()
    return questions


@api.post("/questions/", response=QuestionResponse)
def create_question(
        request: HttpRequest,
        data: QuestionRequest
) -> QuestionResponse:
    """
    Create a new question.

    - `text`: The text of the question. Cannot be empty.
    Returns the created question object.
    """
    logger.info("Creating question", extra={"text": data.text})
    question = Question.objects.create(**data.dict())
    return question


@api.get("/questions/{question_id}", response=QuestionResponse)
def get_question(request: HttpRequest, question_id: int) -> QuestionResponse:
    """
    Retrieve a specific question by its ID, including all associated answers.

    - `question_id`: ID of the question to retrieve.
    """
    question = get_object_or_404(
        Question.objects.prefetch_related("answers"),
        pk=question_id,
    )
    return question


@api.delete("/questions/{question_id}")
def delete_question(request: HttpRequest, question_id: int) -> dict:
    """
    Delete a specific question by its ID.

    - `question_id`: ID of the question to delete.
    Returns a confirmation message.
    """
    logger.info("Deleting question", extra={"question_id": question_id})
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return {f"Вопрос-{question_id}": "Удален"}


@api.get("/answers/{answer_id}", response=AnswerResponse)
def get_answer(request: HttpRequest, answer_id: int) -> AnswerResponse:
    """
    Retrieve a specific answer by its ID.

    - `answer_id`: ID of the answer to retrieve.
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    return answer


@api.delete("/answers/{answer_id}")
def delete_answer(request: HttpRequest, answer_id: int) -> dict:
    """
    Delete a specific answer by its ID.

    - `answer_id`: ID of the answer to delete.
    Returns a confirmation message.
    """
    logger.info("Deleting answer", extra={"answer_id": answer_id})
    answer = get_object_or_404(Answer, pk=answer_id)
    answer.delete()
    return {f"Ответ-{answer_id}": "Удален"}


@api.post("/questions/{question_id}/answers/", response=AnswerResponse)
def create_answer(
    request: HttpRequest,
    question_id: int,
    data: AnswerRequest,
) -> AnswerResponse:
    """
    Add a new answer to a specific question.

    - `question_id`: ID of the question to which the answer will be added.
    - `user_id`: UUID of the user submitting the answer.
    - `text`: Text content of the answer. Cannot be empty.
    Returns the created answer object.
    """
    logger.info(
        "Creating answer",
        extra={"question_id": question_id, "user_id": str(data.user_id)},
    )
    question = get_object_or_404(Question, pk=question_id)
    answer = Answer.objects.create(
        question=question,
        user_id=data.user_id,
        text=data.text,
    )
    return answer
