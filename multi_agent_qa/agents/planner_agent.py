"""
PlannerAgent
------------
• Converts a high-level QA prompt into an ordered list of SubGoal objects.
• Can call an LLM or operate rule-based for fast local testing.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Dict, Any

from ..utils.llm_interface import LLMInterface


@dataclass
class SubGoal:
    step_id: int
    description: str
    metadata: Dict[str, Any] | None = None


class PlannerAgent:
    def __init__(self, llm: LLMInterface | None = None) -> None:
        self.llm = llm or LLMInterface()

    # ------------------------------------------------------------------ #
    # PUBLIC API
    # ------------------------------------------------------------------ #
    def plan(self, task_prompt: str) -> List[SubGoal]:
        """
        Returns an initial linear plan (can later be re-planned).
        """
        json_schema = """
Return your plan as raw JSON — a list of objects with keys:
  step_id   (int),
  description (str),
  metadata    (dict, optional)
        """.strip()

        response = self.llm.system_user(
            "You are a mobile QA PlannerAgent. " + json_schema,
            task_prompt,
        )

        try:
            raw_plan = eval(response)  # quick-n-dirty; replace with json.loads in prod
        except Exception as e:
            raise ValueError(f"PlannerAgent could not parse JSON: {e}\nLLM:\n{response}")

        return [SubGoal(**sg) for sg in raw_plan]
