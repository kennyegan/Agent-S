"""
VerifierAgent
-------------
Checks whether the app is in the expected state after each subgoal.
"""

from __future__ import annotations
from typing import Dict, Any

from ..utils.llm_interface import LLMInterface


class VerifierAgent:
    def __init__(self, llm: LLMInterface | None = None) -> None:
        self.llm = llm or LLMInterface()

    # ------------------------------------------------------------------ #
    def verify(
        self,
        subgoal: "planner_agent.SubGoal",
        executor_result: Dict[str, Any],
        ui_state: Any = None,
    ) -> Dict[str, Any]:
        """
        Returns a dict with keys: verdict ('pass' | 'fail'), reason (str)
        """
        success = executor_result.get("success", False)
        reason = executor_result.get("info", {}).get("msg", "")
        verdict = "pass" if success else "fail"
        return {"verdict": verdict, "reason": reason}
