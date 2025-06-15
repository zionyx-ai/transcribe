# src/speech/__main__.py
import uvicorn


def main():
    uvicorn.run("speech.fastapi_app:app", host="0.0.0.0", port=8001, reload=True)


if __name__ == "__main__":
    main()
