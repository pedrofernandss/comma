import logging
import os
from pathlib import Path
from openai import OpenAI

logger = logging.getLogger(__name__)

PROMPT_PATH = Path(__file__).parent.parent.parent / \
    "resources" / "prompts" / "summarization.txt"


class GroqLLM:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.environ["GROQ_API_KEY"],
            base_url="https://api.groq.com/openai/v1",
        )
        self.system_prompt = PROMPT_PATH.read_text(encoding="utf-8")

    def summarize_news(self, content: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": content},
                ],
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Failed to use Groq API: {e}")
            return "Summary unavailable due to API error."
