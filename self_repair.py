import logging, os, json, shutil
from typing import Callable, Dict, Tuple, List
from knowledge_base import KnowledgeBase

class SelfRepairSystem:
    def __init__(self, knowledge_base: KnowledgeBase):
        self.kb = knowledge_base
        self.checks: Dict[str, Callable[[], Tuple[bool, str]]] = {}
        self.repairs: Dict[str, Callable[[str], bool]] = {}

    def register_check(self, name: str, fn: Callable[[], Tuple[bool, str]]):
        self.checks[name] = fn

    def register_repair(self, name: str, fn: Callable[[str], bool]):
        self.repairs[name] = fn

    def detect_issues(self) -> List[Tuple[str, str]]:
        issues = []
        for name, fn in self.checks.items():
            try:
                ok, details = fn()
            except Exception as e:
                ok, details = False, f"check exception: {e}"
            if not ok:
                logging.warning("Issue: %s -> %s", name, details)
                issues.append((name, details))
        return issues

    def repair_issue(self, issue_name: str, details: str) -> bool:
        if issue_name in self.repairs:
            try:
                return bool(self.repairs[issue_name](details))
            except Exception as e:
                logging.error("Repair %s failed: %s", issue_name, e)
                return False
        # fallback restore from backups
        backups = sorted([f for f in os.listdir(self.kb.backups_dir) if f.endswith('.json')])
        if backups:
            last = backups[-1]
            shutil.copy2(os.path.join(self.kb.backups_dir, last), self.kb.path)
            self.kb._load_or_init()
            return True
        return False
