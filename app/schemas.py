from pydantic import BaseModel, Field


class QuestionRequest(BaseModel):
    question: str = Field(..., min_length=3, description="Question to ask about the uploaded PDF documents")


class QuestionResponse(BaseModel):
    answer: str
    sources: list[str]