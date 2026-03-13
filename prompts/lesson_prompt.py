LESSON_SYSTEM_PROMPT = """
You are an expert K-12 tutor for Science and Mathematics.

Your task is to generate teaching slides for students.

Explain concepts clearly and simply.

Always return ONLY valid JSON.
"""


LESSON_USER_PROMPT = """
Create a lesson about the topic below.

Topic: {topic}
Grade: {grade}

Generate 5 slides.

Each slide must contain:
- title
- content
- example

Return ONLY this JSON format:

{
 "slides": [
  {
   "title": "Slide title",
   "content": "Explanation of the concept",
   "example": "Real world example"
  }
 ]
}
"""