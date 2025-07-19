from pydantic import BaseModel, Field

class QuoteRequest(BaseModel):
    target_performance: str = Field(..., alias="targetPerformance")
    budget: str

class QuoteResponse(BaseModel):
    build_name: str
    parts: dict
    subtotal: str
    input: QuoteRequest
