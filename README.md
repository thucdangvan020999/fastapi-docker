# Deploy ML models with FastAPI, Docker

### 1. How to use without Docker
Create visual enviroment 
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.api:app --host 0.0.0.0 --port 8000 --reload
```


### 2. Use docker

```bash
docker-compose up --build
```
