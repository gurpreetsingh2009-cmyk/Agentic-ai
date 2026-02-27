# Amrit-ai - Integrated Self System (entrypoint)
from knowledge_base import KnowledgeBase
from self_repair import SelfRepairSystem
from self_analysis import SelfAnalysisSystem
from self_update import SelfUpdateSystem
from self_code_generator import SelfCodeGenerator
import logging
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def build_demo_system():
    kb = KnowledgeBase(path="kb.json", backups_dir="backups")
    repl = SelfRepairSystem(kb)
    analysis = SelfAnalysisSystem(kb, repl)
    updater = SelfUpdateSystem(kb)
    coder = SelfCodeGenerator(kb)

    # add simple demo data
    kb.add_knowledge("greeting", {"text": "ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ", "lang": "pa"})
    kb.set_version("v0.1.0")
    # simulate available update metadata (for testing)
    kb.knowledge.setdefault("meta", {})["available_version"] = "v0.1.1"

    return kb, repl, analysis, updater, coder

if __name__ == "__main__":
    kb, repl, analysis, updater, coder = build_demo_system()
    logging.info("Running one system pass...")
    report = analysis.analyze_system()
    logging.info("Report: %s", report)

    ok, info, data = updater.check_for_updates()
    logging.info("Update check: %s", info)
    if ok:
        applied = updater.apply_updates(data)
        logging.info("Applied: %s", applied)

    # demonstrate code generation
    new_file = coder.generate_python_module("generated_module", code_content="# Auto-generated module\nprint('Hello from generated module')")
    logging.info("Generated module: %s", new_file)

    print("Run finished. KB version:", kb.get_version())
