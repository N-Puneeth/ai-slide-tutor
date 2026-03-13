from groq import Groq

from config.settings import GROQ_API_KEY, MODEL_NAME, TEMPERATURE, MAX_TOKENS


client = Groq(api_key=GROQ_API_KEY)


def generate_lesson(topic: str, grade: int | None = None):

    prompt = f"""
You are a helpful K-12 tutor.

Create a lesson about: {topic}
Grade level: {grade if grade else "Not specified"}

Generate 5 teaching slides.

For each slide provide:
Title
Explanation
Example

Format like this:

Slide 1:
Title: ...
Content: ...
Example: ...

Slide 2:
Title: ...
Content: ...
Example: ...
"""

    try:

        response = client.chat.completions.create(
            model=MODEL_NAME,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        content = response.choices[0].message.content

        slides = []

        parts = content.split("Slide")

        for part in parts[1:]:
            lines = part.split("\n")

            title = ""
            text = ""
            example = ""

            for line in lines:

                if "Title:" in line:
                    title = line.replace("Title:", "").strip()

                elif "Content:" in line:
                    text = line.replace("Content:", "").strip()

                elif "Example:" in line:
                    example = line.replace("Example:", "").strip()

            slides.append({
                "title": title if title else "Slide",
                "content": text,
                "example": example
            })

        return slides

    except Exception as e:

        print("GROQ ERROR:", e)

        return [
            {
                "title": "Error generating lesson",
                "content": str(e),
                "example": ""
            }
        ]