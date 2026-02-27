import json, os, time, shutil, logging
from typing import Any, Dict

class KnowledgeBase:
    def __init__(self, path: str = "kb.json", backups_dir: str = "backups"):
        self.path = path
        self.backups_dir = backups_dir
        os.makedirs(self.backups_dir, exist_ok=True)
        self.knowledge: Dict[str, Any] = {}
        self._load_or_init()

    def _load_or_init(self):
        if os.path.exists(self.path):
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    self.knowledge = json.load(f)
            except Exception as e:
                logging.error("Failed to load KB: %s", e)
                self.knowledge = {}
        if not self.knowledge:
            self.knowledge = {"version": "v0.0.0", "meta": {"created": time.time()}, "items": {}}
            self._persist()

    def _persist(self):
        tmp = self.path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(self.knowledge, f, indent=2, ensure_ascii=False)
        os.replace(tmp, self.path)

    def backup(self) -> str:
        ts = int(time.time())
        dest = os.path.join(self.backups_dir, f"kb_{ts}.json")
        shutil.copy2(self.path, dest)
        logging.info("KB backup created: %s", dest)
        return dest

    def add_knowledge(self, topic: str, info):
        self.knowledge.setdefault("items", {})[topic] = {"data": info, "updated": time.time()}
        self._persist()

    def retrieve_knowledge(self, topic: str):
        return self.knowledge.get("items", {}).get(topic)

    def set_version(self, version: str):
        self.knowledge["version"] = version
        self._persist()

    def get_version(self) -> str:
        return self.knowledge.get("version", "v0.0.0")
