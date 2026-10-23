"""Shared helpers: configurable paths, cluster files and the OpenAI API key.

All locations are read from a YAML configuration file (see config.example.yaml). The file is found through the
COABUNDANCE_CONFIG environment variable, or as config.yaml next to this module. Relative paths in the file are
resolved against the directory that contains the configuration file.
"""
import json
import os
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
PATH_KEYS = ("raw_data", "data", "graph", "analysis", "knowledge", "report", "traces", "work")


def config_file() -> Path:
    path = Path(os.environ.get("COABUNDANCE_CONFIG", HERE / "config.yaml")).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"Configuration file not found: {path}. Copy config.example.yaml to config.yaml "
                                "and set the paths, or point COABUNDANCE_CONFIG to your own file.")
    return path


def load_config() -> dict:
    path = config_file()
    cfg = yaml.safe_load(path.read_text()) or {}
    paths = cfg.get("paths", {})
    missing = [k for k in PATH_KEYS if k not in paths]
    if missing:
        raise KeyError(f"{path}: missing paths: {', '.join(missing)}")
    cfg["paths"] = {k: (path.parent / Path(v).expanduser()).resolve() for k, v in paths.items()}
    env = cfg.get("env_file", ".env")
    cfg["env_file"] = (path.parent / Path(env).expanduser()).resolve()
    return cfg


CONFIG = load_config()
PATHS = CONFIG["paths"]


def load_api_key() -> str:
    """OpenAI API key from the environment (OPENAI_API_KEY) or from the configured .env file."""
    if os.environ.get("OPENAI_API_KEY"):
        return os.environ["OPENAI_API_KEY"]
    env = CONFIG["env_file"]
    if env.exists():
        for line in env.read_text().splitlines():
            if "=" in line and line.split("=", 1)[0].strip().lower() in ("openai-api-key", "openai_api_key"):
                return line.split("=", 1)[1].strip().strip("'\"")
    raise RuntimeError(f"No OpenAI API key: set OPENAI_API_KEY or add OPENAI_API_KEY=... to {env}")


def load_clusters(path) -> dict:
    """Cluster members of one tissue pair as {cluster id: [member records]}.

    Step 2 writes a list (position = cluster id); Step 2b keeps the clusters that pass the permutation filter
    and rewrites the file as an object keyed by cluster id. Both forms are accepted.
    """
    raw = json.loads(Path(path).read_text())
    if isinstance(raw, list):
        return {i: m for i, m in enumerate(raw)}
    return {int(k): v for k, v in raw.items()}
