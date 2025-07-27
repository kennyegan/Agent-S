"""
Orchestrates Planner → Executor → Verifier → logs.
"""

from __future__ import annotations
from typing import List, Dict, Any

from .agents.planner_agent import PlannerAgent, SubGoal
from .agents.executor_agent import ExecutorAgent
from .agents.verifier_agent import VerifierAgent
from .agents.supervisor_agent import SupervisorAgent


class QATestController:
    def __init__(self, task_prompt: str) -> None:
        self.task_prompt = task_prompt

        self.planner = PlannerAgent()
        self.executor = ExecutorAgent()
        self.verifier = VerifierAgent()
        self.supervisor = SupervisorAgent()

        self.log: List[Dict[str, Any]] = []

    # ------------------------------------------------------------------ #
    def run(self) -> None:
        plan = self.planner.plan(self.task_prompt)

        for subgoal in plan:
            exec_result = self.executor.execute(subgoal)
            verif_result = self.verifier.verify(subgoal, exec_result)

            self.log.append(
                {
                    "step_id": subgoal.step_id,
                    "description": subgoal.description,
                    "exec_result": exec_result,
                    "verif_result": verif_result,
                }
            )

        print(self.supervisor.summarize(self.log))
