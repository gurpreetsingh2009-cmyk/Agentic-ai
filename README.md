# Amrit-ai v2 
This package is a release-ready example of the **Amrit-ai** integrated self-maintaining system.
It includes:
- KnowledgeBase (JSON persistence + backups)
- SelfRepairSystem (checks + repair registry)
- SelfAnalysisSystem (health report)
- SelfUpdateSystem (GitHub Releases based updater skeleton)
- SelfCodeGenerator (simple auto-generation of python/web files)

## How to run (local)
1. Create a virtualenv: `python -m venv venv && source venv/bin/activate`
2. Install: `pip install -r requirements.txt`
3. Set env vars if you want update checks:
   - `GITHUB_OWNER` (e.g. gurpreetsingh2009-cmyk)
   - `GITHUB_REPO` (e.g. Amrit-ai)
   - `GITHUB_TOKEN` (optional, recommended for private repos)
4. Run: `python main.py`

## Structure
- main.py
- knowledge_base.py
- self_repair.py
- self_analysis.py
- self_update.py
- self_code_generator.py
- kb.json (created at first run)
- backups/ (auto-created)
