import shutil
from pathlib import Path


def on_post_build(config, **kwargs):
    src = Path(".well-known")
    if src.exists():
        dst = Path(config.site_dir) / ".well-known"
        shutil.copytree(src, dst, dirs_exist_ok=True)
