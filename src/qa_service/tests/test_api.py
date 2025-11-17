import pytest
from uuid import uuid4
from ninja.testing import TestClient

from qa_service.models import Question, Answer
from qa_service.api import api


@pytest.fixture(scope="module")
def api_client():
    return TestClient(api)


@pytest.mark.django_db
def test_create_question(api_client) -> None:
    response = api_client.post("/questions/", json={"text": "test"})

    assert response.status_code == 200
    assert Question.objects.count() == 1


@pytest.mark.django_db
def test_create_empty_question(api_client) -> None:
    response = api_client.post("/questions/", json={"text": ""})

    assert response.status_code == 422
    assert Question.objects.count() == 0


@pytest.mark.parametrize(
    "answers_text",
    [
        ["Ответ 1", "Ответ 2", "Ответ 3"],
        ["Ответ"],
    ]
)
@pytest.mark.django_db
def test_user_can_leave_multiple_answers(answers_text, api_client) -> None:
    question = Question.objects.create(text="Этот тест пройден?")
    user_id = str(uuid4())

    for text in answers_text:
        response = api_client.post(
            f"/questions/{question.id}/answers/",
            json={"user_id": user_id, "text": text}
        )
        assert response.status_code == 200

    answers = Answer.objects.filter(question=question, user_id=user_id)
    assert answers.count() == len(answers_text)
