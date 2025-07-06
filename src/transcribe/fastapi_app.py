from fastapi import FastAPI
# src/speech/fastapi_app.py
from transcribe.router.router import router  # ✅ korrekt
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="n/a")
app.include_router(router, prefix="/api/v1", tags=["transcribe"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # oder spezifische URLs wie ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],  # wichtig: auch "OPTIONS"
    allow_headers=["*"],
)