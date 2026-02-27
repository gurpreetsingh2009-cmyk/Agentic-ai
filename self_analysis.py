import logging
from typing import Dict, Any
from knowledge_base import KnowledgeBase
from self_repair import SelfRepairSystem

class SelfAnalysisSystem:
    def __init__(self, knowledge_base: KnowledgeBase, repair_system: SelfRepairSystem):
        self.kb = knowledge_base
        self.repair_system = repair_system

    def analyze_system(self) -> Dict[str, Any]:
        issues = self.repair_system.detect_issues()
        report = {
            "version": self.kb.get_version(),
            "num_topics": len(self.kb.knowledge.get('items', {})),
            "issues": [{"check": n, "details": d} for n,d in issues]
        }
        logging.info("Analysis: found %d issues", len(issues))
        return report
