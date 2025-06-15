from fastapi import APIRouter, UploadFile, File, Form
from speech.services.transcriber import transcribe_audio

router = APIRouter()


@router.post("/transcribe")
async def speech_to_text(
    file: UploadFile = File(...),
    language: str = Form(...),
):
    result = await transcribe_audio(file, language)
    return result