# ✨ transcribe-service

**Teil von [Scriptora](https://github.com/scriptora-ai/scriptora)**  
Der `transcribe-service` ist ein leichtgewichtiger Microservice zur Umwandlung von Sprache in Text. Er nutzt moderne Spracherkennungstechnologien wie Whisper oder Google STT und bildet den ersten Verarbeitungsschritt in der Scriptora-Architektur.
📦 Microservice für Sprachaufnahme → Text (Whisper, Google STT)

---

## 🔍 Übersicht

| Kategorie          | Wert             |
|--------------------|------------------|
| Sprache            | Python (FastAPI) |
| Port               | `5100`           |
| Kommunikation      | REST             |
| Datenbank          | —                |
| Docker-kompatibel  | ✅               |
| Status             | MVP              |

---

## ⚙️ Setup

### 🐳 Docker (empfohlen)

```bash
docker build -t scriptora/transcribe-service .
docker run -p 5100:5100 scriptora/transcribe-service
```

### 🧑‍💻 Lokaler Start

```bash
uvicorn src.main:app --host 0.0.0.0 --port 5100 --reload
```

### 🧪 Tests

```bash
pytest
```

---

## 🚀 API-Dokumentation

### Beispiel: `POST /transcribe`

```http
POST /transcribe
Content-Type: multipart/form-data

file=<audio-file>
```

**Antwort:**

```json
{
  "transcript": "Im Anfang schuf Gott Himmel und Erde",
  "confidence": 0.94
}
```

> Swagger/OpenAPI: [http://localhost:5100/docs](http://localhost:5100/docs)

---

## 🔐 Authentifizierung

* ⛔ Nicht erforderlich für MVP
* 🔐 Optional: Keycloak JWT-Token-Unterstützung

---

## 📁 Projektstruktur

```
.
├── src/
│   ├── main.py
│   ├── api/
│   ├── services/
│   └── models/
├── tests/
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🔄 CI/CD

```yaml
name: CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest
```

---

## 🔗 Verbundene Services

Dieser Service wird hauptsächlich verwendet von:

* `voice-command-gateway`
* `scriptora-app`

---

## 🧠 Lizenz & Mitwirken

Open Source unter [GPL-3.0 License](./LICENSE)  
Mitwirken? Pull Request willkommen oder Kontakt über [Scriptora](https://github.com/scriptora-ai/scriptora)
