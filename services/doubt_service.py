from groq import Groq

from config.settings import GROQ_API_KEY, MODEL_NAME, TEMPERATURE, MAX_TOKENS


client = Groq(api_key=GROQ_API_KEY)


def solve_doubt(topic: str, context: str, question: str):

    prompt = f"""
You are a helpful K-12 tutor.

Topic:
{topic}

Slide context:
{context}

Student question:
{question}

Explain clearly and simply so a school student can understand.
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

        answer = response.choices[0].message.content

        return answer

    except Exception as e:

        print("GROQ ERROR:", e)

        return "Sorry, I couldn't generate an answer right now."