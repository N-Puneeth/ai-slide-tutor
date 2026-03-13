from pydantic import BaseModel, Field
from typing import List, Optional



# LESSON GENERATION REQUEST


class TopicRequest(BaseModel):
    topic: str = Field(
        ...,
        min_length=2,
        max_length=200,
        description="Topic the student wants to learn",
        example="Newton's Laws of Motion"
    )

    grade: Optional[int] = Field(
        None,
        ge=1,
        le=12,
        description="Student grade level (optional)",
        example=9
    )



# SLIDE STRUCTURE


class Slide(BaseModel):
    title: str = Field(
        ...,
        description="Slide title",
        example="What is Photosynthesis?"
    )

    content: str = Field(
        ...,
        description="Main explanation for the slide",
        example="Photosynthesis is the process by which plants convert sunlight into energy."
    )

    example: Optional[str] = Field(
        None,
        description="Optional example or application",
        example="Plants use sunlight to produce glucose."
    )



# LESSON RESPONSE


class LessonResponse(BaseModel):
    topic: str
    slides: List[Slide]



# DOUBT SOLVER REQUEST


class DoubtRequest(BaseModel):
    topic: str = Field(
        ...,
        description="Topic currently being studied",
        example="Quadratic Equation"
    )

    context: str = Field(
        ...,
        description="Content of the current slide",
        example="The discriminant of a quadratic equation is b² - 4ac."
    )

    question: str = Field(
        ...,
        min_length=3,
        max_length=500,
        description="Student doubt question",
        example="Why does the discriminant determine the number of roots?"
    )



# DOUBT RESPONSE


class DoubtResponse(BaseModel):
    answer: str = Field(
        ...,
        description="AI explanation for the student's question"
    )