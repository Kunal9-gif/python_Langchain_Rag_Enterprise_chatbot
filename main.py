from fastapi import FastAPI, Request
from core.orchestrator import chatbot_pipeline

app = FastAPI()

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    response = chatbot_pipeline(data.get("message"))
    return {"reply": response}
