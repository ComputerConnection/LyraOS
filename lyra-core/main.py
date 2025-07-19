from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "Lyra.Core online"}

@app.post("/generateQuote")
def generate_quote(data: dict):
    return {"quote": "Quote logic here", "input": data}