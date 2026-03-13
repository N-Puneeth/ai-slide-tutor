from fastapi import APIRouter, HTTPException

from models.schemas import (
    TopicRequest,
    LessonResponse,
    DoubtRequest,
    DoubtResponse
)

from services.lesson_service import generate_lesson
from services.doubt_service import solve_doubt


router = APIRouter()



# GENERATE LESSON ENDPOINT


@router.post("/generate-lesson", response_model=LessonResponse)
def generate_lesson_api(request: TopicRequest):
    """
    Generates lesson slides for a given topic.
    """

    try:
        slides = generate_lesson(
            topic=request.topic,
            grade=request.grade
        )

        return {
            "topic": request.topic,
            "slides": slides
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Lesson generation failed: {str(e)}"
        )



# DOUBT SOLVER ENDPOINT


@router.post("/solve-doubt", response_model=DoubtResponse)
def solve_doubt_api(request: DoubtRequest):
    """
    Answers a student's doubt based on the topic and slide context.
    """

    try:
        answer = solve_doubt(
            topic=request.topic,
            context=request.context,
            question=request.question
        )

        return {
            "answer": answer
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Doubt solving failed: {str(e)}"
        )