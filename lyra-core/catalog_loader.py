# lyra-core/catalog_loader.py
import json, os
from functools import lru_cache
from typing import Dict, Any

CATALOG_DIR = os.path.join(os.path.dirname(__file__), "catalog", "blocks")

def _load_single(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    data["_source_file"] = os.path.basename(path)
    return data

@lru_cache(maxsize=1)
def load_blocks() -> Dict[str, Any]:
    blocks = {}
    if not os.path.isdir(CATALOG_DIR):
        return blocks
    for fname in os.listdir(CATALOG_DIR):
        if not fname.lower().endswith(".json"):
            continue
        full = os.path.join(CATALOG_DIR, fname)
        try:
            b = _load_single(full)
            blocks[b["block_id"]] = b
        except Exception as e:
            print(f"[CATALOG] Failed to load {fname}: {e}")
    return blocks

def force_reload():
    load_blocks.cache_clear()
    return load_blocks()
