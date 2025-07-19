# lyra-core/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from catalog_loader import load_blocks, force_reload
from quote_logic import select_performance_block

app = FastAPI()

class QuoteRequest(BaseModel):
    targetPerformance: str
    budget: float

@app.get("/health")
def health():
    return {"status": "Lyra.Core online"}

@app.get("/catalog/blocks")
def list_blocks(block_type: str | None = None):
    blocks = list(load_blocks().values())
    if block_type:
        blocks = [b for b in blocks if b.get("block_type") == block_type]
    return {"count": len(blocks), "blocks": blocks}

@app.get("/catalog/blocks/{block_id}")
def get_block(block_id: str):
    b = load_blocks().get(block_id)
    if not b:
        raise HTTPException(status_code=404, detail="Block not found")
    return b

@app.post("/catalog/reload")
def reload_catalog():
    blocks = force_reload()
    return {"reloaded": len(blocks)}

@app.post("/generateQuote")
def generate_quote(data: QuoteRequest):
    blocks = list(load_blocks().values())
    candidate = select_performance_block(blocks, data.targetPerformance, data.budget)
    if not candidate:
        raise HTTPException(status_code=404, detail="No performance block match")
    return {
        "strategy": {
            "targetPerformance": data.targetPerformance,
            "budget": data.budget
        },
        "selected_block": candidate,
        "message": f"Selected block {candidate['block_id']} for target {data.targetPerformance}"
    }
