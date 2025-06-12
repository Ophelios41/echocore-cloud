from fastapi import FastAPI, Request
from core.decision import make_decision

app = FastAPI()

@app.post("/decision")
async def decision_handler(request: Request):
    data = await request.json()
    response = make_decision(data)
    return response