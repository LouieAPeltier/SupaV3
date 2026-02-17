# ListRank Backend (FastAPI)

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8080
```

## Environment

Set these environment variables if using Firebase in GCP:

- `LISTRANK_FIREBASE_PROJECT_ID`
- `LISTRANK_FIREBASE_STORAGE_BUCKET`

Auth is expected to come from Firebase ID tokens (to be added in the next iteration).
