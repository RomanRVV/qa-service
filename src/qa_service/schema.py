from ninja import Schema, Field
from pydantic import ConfigDict
from uuid import UUID
from datetime import datetime


schema_config = ConfigDict(
    use_attribute_docstrings=True,
    str_strip_whitespace=True,
)


class AnswerRequest(Schema):
    """Schema for submitting a new answer to a question."""
    user_id: UUID
    text: str = Field(min_length=1)

    model_config = schema_config


class AnswerResponse(Schema):
    """Schema representing an answer returned by the API."""
    id: int
    question_id: int
    user_id: UUID
    text: str = Field(min_length=1)
    created_at: datetime

    model_config = schema_config


class QuestionRequest(Schema):
    """Schema for creating a new question."""
    text: str = Field(min_length=1)

    model_config = schema_config


class QuestionResponse(Schema):
    """Schema representing a question returned by the API."""
    id: int
    text: str = Field(min_length=1)
    created_at: datetime
    answers: list[AnswerResponse] = []

    model_config = schema_config
