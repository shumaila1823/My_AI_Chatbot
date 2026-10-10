
import os
from groq import Groq

MODEL_NAME = "llama-3.3-70b-versatile"

SYSTEM_PROMPT = """
You are a friendly, helpful AI assistant.
Answer clearly and accurately.
Explain difficult concepts in simple language.
Be honest when you do not know an answer.
"""


def generate_response(message, history):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return "API key is missing. Please configure the app secret."

    try:
        client = Groq(api_key=api_key)

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]

        for item in history or []:
            if isinstance(item, dict):
                role = item.get("role")
                content = item.get("content")

                if role in ("user", "assistant") and isinstance(content, str):
                    messages.append({
                        "role": role,
                        "content": content
                    })

        messages.append({
            "role": "user",
            "content": message
        })

        result = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0.7,
            max_tokens=1024
        )

        return result.choices[0].message.content or "No response received."

    except Exception as error:
        print(f"Groq API error: {error}")
        return (
            "Sorry, the AI service returned an error. "
            "Please check the API key, model availability, "
            "internet connection, and usage limits."
        )
