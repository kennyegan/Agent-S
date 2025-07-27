"""
SupervisorAgent
---------------
High-level post-run analysis & feedback.  For Phase 1 it just prints summary.
"""

from typing import List, Dict, Any


class SupervisorAgent:
    def summarize(self, log: List[Dict[str, Any]]) -> str:
        return f"Run complete. {len(log)} steps recorded."
