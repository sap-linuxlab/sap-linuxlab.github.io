import os
import shutil
from pathlib import Path


def on_config(config, **kwargs):
    if os.environ.get("MKDOCS_PREVIEW") == "1":
        config.site_url = "https://sap-linuxlab.github.io/preview/"
        config.extra.pop("analytics", None)
        config.extra.pop("consent", None)


def on_post_build(config, **kwargs):
    src = Path(".well-known")
    if src.exists():
        dst = Path(config.site_dir) / ".well-known"
        shutil.copytree(src, dst, dirs_exist_ok=True)
