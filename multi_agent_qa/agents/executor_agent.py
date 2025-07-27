"""
ExecutorAgent
-------------
Receives a SubGoal → reads current UI → issues grounded action(s) via Agent-S.

For Phase 1 we stub out the call but keep interfaces ready.
"""

from __future__ import annotations
from typing import Dict, Any

from ..utils.llm_interface import LLMInterface
from gui_agents.core.graph_search_agent import GraphSearchAgent
from gui_agents.platforms.linux_aci import LinuxACI  # or MacOSACI / WindowsACI


class ExecutorAgent:
    def __init__(self) -> None:
        # In real code: choose ACI by platform or task; reuse one instance.
        self.aci = LinuxACI()
        self.graph_agent = GraphSearchAgent(aci=self.aci)

    # ------------------------------------------------------------------ #
    def execute(self, subgoal: "planner_agent.SubGoal") -> Dict[str, Any]:
        """
        Returns a dict with keys: success (bool), observation (Any), info (dict)
        """
        # ↓↓↓  Placeholder action  ↓↓↓
        # You’ll replace with UI-tree search + graph_agent.predict(...)
        return {
            "success": True,
            "observation": None,
            "info": {"msg": f"Executed: {subgoal.description}"},
        }
