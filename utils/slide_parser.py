import json
import re
from typing import List
from models.schemas import Slide


def extract_json(text: str) -> str:
    """
    Extract the JSON object from the LLM response.
    LLMs often return extra text before/after JSON.
    """

    match = re.search(r"\{.*\}", text, re.DOTALL)

    if not match:
        raise ValueError("No JSON object found in LLM output.")

    return match.group(0)


def parse_slides(llm_output: str) -> List[Slide]:
    """
    Parse slides from the LLM response safely.
    """

    try:
        # Extract JSON part
        json_text = extract_json(llm_output)

        data = json.loads(json_text)

        slides_data = data.get("slides", [])

        slides = []

        for slide in slides_data:
            slides.append(
                Slide(
                    title=slide.get("title", "").strip(),
                    content=slide.get("content", "").strip(),
                    example=slide.get("example", None)
                )
            )

        return slides

    except Exception as e:
        raise ValueError(f"Slide parsing failed: {str(e)}")


def slides_to_dict(slides: List[Slide]):
    """
    Convert Slide objects to dictionary for API response.
    """

    return [
        {
            "title": slide.title,
            "content": slide.content,
            "example": slide.example
        }
        for slide in slides
    ]