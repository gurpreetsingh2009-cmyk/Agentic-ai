# Amrit-ai v2 
This package is a release-ready example of the **Amrit-ai** integrated self-maintaining system.
It includes:
- KnowledgeBase (JSON persistence + backups)
- SelfRepairSystem (checks + repair registry)
- SelfAnalysisSystem (health report)
- SelfUpdateSystem (GitHub Releases based updater skeleton)
- SelfCodeGenerator (simple auto-generation of python/web files)
- # 🤖 Amrit-ai: Integrated Self-Maintaining System

Amrit-ai ਇੱਕ ਅਜਿਹਾ ਪ੍ਰੋਜੈਕਟ ਹੈ ਜੋ ਆਪਣੇ ਆਪ ਨੂੰ ਸੰਭਾਲਣ, ਰਿਪੇਅਰ ਕਰਨ ਅਤੇ ਅਪਡੇਟ ਕਰਨ ਦੀ ਸਮਰੱਥਾ ਰੱਖਦਾ ਹੈ। ਇਹ ਸਿਸਟਮ ਆਟੋਮੇਸ਼ਨ ਅਤੇ ਏਜੰਟਿਕ ਆਈਡੀਆ 'ਤੇ ਅਧਾਰਤ ਹੈ।

## ✨ ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ (Key Features)

* **KnowledgeBase:** JSON ਡਾਟਾ ਸਟੋਰੇਜ ਅਤੇ ਆਟੋਮੈਟਿਕ ਬੈਕਅੱਪ ਸਿਸਟਮ।
* **Self-Repair System:** ਕੋਡ ਵਿੱਚ ਗਲਤੀਆਂ ਦੀ ਜਾਂਚ ਕਰਨਾ ਅਤੇ ਉਹਨਾਂ ਨੂੰ ਠੀਕ ਕਰਨਾ।
* **Self-Analysis System:** ਸਿਸਟਮ ਦੀ ਸਿਹਤ (Health Report) ਤਿਆਰ ਕਰਨਾ।
* **Self-Update System:** GitHub ਰੀਲੀਜ਼ ਰਾਹੀਂ ਆਪਣੇ ਆਪ ਨੂੰ ਅਪਡੇਟ ਰੱਖਣਾ।
* **Self-Code Generator:** ਪਾਈਥਨ ਅਤੇ ਵੈੱਬ ਫਾਈਲਾਂ ਨੂੰ ਆਟੋਮੈਟਿਕ ਤਿਆਰ ਕਰਨਾ।

## 🚀 ਕਿਵੇਂ ਚਲਾਉਣਾ ਹੈ (Setup Guide)

### 1. ਵਾਤਾਵਰਣ ਤਿਆਰ ਕਰੋ (Create Virtual Environment)
```bash 2. ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਸਟਾਲ ਕਰੋ
pip install -r requirements.txt

python -m venv venv
source venv/bin/activate  # Windows ਲਈ: venv\Scripts\activate


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
