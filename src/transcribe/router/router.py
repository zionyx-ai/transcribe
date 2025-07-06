from typing import Optional
from fastapi import APIRouter, UploadFile, File, Form
from transcribe.services.transcriber import transcribe_audio

router = APIRouter()


@router.post("/transcribe")
async def speech_to_text(
    file: UploadFile = File(...),
    language: Optional[str] = Form(None)
):
    print(f"Received file: {file.filename}, Language: {language}")
    result = await transcribe_audio(file, language)
    return result