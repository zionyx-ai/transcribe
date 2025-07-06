from faster_whisper import WhisperModel
from fastapi import UploadFile
import tempfile
import os


# model = WhisperModel("base")
model = WhisperModel(
    os.path.abspath("src/transcribe/models/whisper-bible"),
    device="cpu",
    compute_type="int8",
    local_files_only=True,
)


async def transcribe_audio(file: UploadFile, language: str):
    print(f"input: language={language}")
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    segments, _ = model.transcribe(tmp_path, language=language)
    full_text = " ".join([seg.text.strip() for seg in segments])
    return {"spoken_text": full_text}
