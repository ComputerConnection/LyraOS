# lyra-core/quote_logic.py
from typing import List, Dict

def select_performance_block(blocks: List[Dict], target: str, budget: float):
    """
    Very simple heuristic selection.
    """
    # Filter by status & type
    perf_blocks = [b for b in blocks if b.get("status") == "active" and b.get("block_type") == "PerformanceBlock"]
    # Filter by target segment keyword (loose match)
    if target:
        token = target.lower()
        perf_blocks = [
            b for b in perf_blocks
            if any(token in seg.lower() for seg in b.get("perf", {}).get("target_segments", []))
               or token in " ".join(b.get("tags", [])).lower()
        ] or perf_blocks  # fall back if empty

    # Sort by closeness to budget (base_price)
    for b in perf_blocks:
        b["_price_gap"] = abs(b.get("base_price", 0) - budget)
    perf_blocks.sort(key=lambda b: (b["_price_gap"], b.get("base_price", 0)))

    return perf_blocks[0] if perf_blocks else None
