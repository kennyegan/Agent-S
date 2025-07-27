"""
Unified LLM wrapper.  Swappable backend (OpenAI, Anthropic, local vLLM, etc.).
"""

from __future__ import annotations
from typing import List, Dict, Any
import os

import openai  # pip install openai

_DEFAULT_MODEL = os.getenv("QA_LLM_MODEL", "gpt-4o")


class LLMInterface:
    def __init__(self, model: str | None = None, temperature: float = 0.3):
        self.model = model or _DEFAULT_MODEL
        self.temperature = temperature

    def __call__(self, messages: List[Dict[str, str]], **kwargs: Any) -> str:
        """
        Minimal blocking wrapper for chat completion.
        Returns **content** (not the whole response dict) for convenience.
        """
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            **kwargs,
        )
        return response["choices"][0]["message"]["content"]

    # Convenience helpers --------------------------------------------------

    def system_user(self, system_prompt: str, user_prompt: str, **kwargs) -> str:
        msgs = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        return self(msgs, **kwargs)
 