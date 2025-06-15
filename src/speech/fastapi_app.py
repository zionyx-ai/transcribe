from fastapi import FastAPI
# src/speech/fastapi_app.py
from speech.router.router import router  # ✅ korrekt


app = FastAPI(title="Speech-Service - Speech-to-Text Service")
app.include_router(router, prefix="/api")
