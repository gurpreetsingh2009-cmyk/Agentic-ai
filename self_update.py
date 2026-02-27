import os, logging, requests
from typing import Optional, Tuple

class GitHubUpdater:
    def __init__(self, owner: str, repo: str, current_version: str, token: str = None):
        self.owner = owner
        self.repo = repo
        self.current_version = current_version
        self.token = token
        self.api_url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"

    def _headers(self):
        h = {"Accept": "application/vnd.github.v3+json"}
        if self.token:
            h["Authorization"] = f"token {self.token}"
        return h

    def fetch_latest_release(self) -> dict:
        resp = requests.get(self.api_url, headers=self._headers(), timeout=10)
        resp.raise_for_status()
        return resp.json()

    def check_for_updates(self) -> Tuple[bool, str, dict]:
        data = self.fetch_latest_release()
        latest = data.get("tag_name", "")
        if not latest:
            return False, "No tag_name in response", {}
        current = self.current_version.lstrip("v")
        latest_v = latest.lstrip("v")
        try:
            if tuple(map(int, latest_v.split("."))) > tuple(map(int, current.split("."))):
                return True, latest, data
        except Exception:
            if latest != self.current_version:
                return True, latest, data
        return False, "Up-to-date", data

    def download_asset(self, assets: list) -> Optional[str]:
        if not assets:
            return None
        asset = assets[0]
        url = asset.get("browser_download_url")
        file_name = url.split("/")[-1]
        logging.info("Downloading asset: %s", file_name)
        r = requests.get(url, headers=self._headers(), stream=True, timeout=30)
        r.raise_for_status()
        with open(file_name, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        return file_name

    def apply_update(self, file_path: str):
        logging.info("Downloaded update asset: %s", file_path)
        logging.info("Install step: unzip/replace files as needed (not implemented).")

class SelfUpdateSystem:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base
        owner = os.getenv("GITHUB_OWNER", "")
        repo = os.getenv("GITHUB_REPO", "")
        token = os.getenv("GITHUB_TOKEN", None)
        self.github_updater = GitHubUpdater(owner=owner, repo=repo, current_version=self.kb.get_version(), token=token)

    def check_for_updates(self):
        try:
            ok, result, data = self.github_updater.check_for_updates()
            return ok, result, data
        except Exception as e:
            logging.error("Update check failed: %s", e)
            return False, str(e), {}

    def apply_updates(self, data):
        assets = data.get("assets", [])
        file_path = self.github_updater.download_asset(assets)
        if file_path:
            self.github_updater.apply_update(file_path)
            tag = data.get("tag_name", "")
            if tag:
                self.kb.set_version(tag)
            return True
        return False
