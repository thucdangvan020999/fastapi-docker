from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version
from http import HTTPStatus
from typing import Dict
from datetime import datetime
from functools import wraps
from app.schemas import PredictPayload


app = FastAPI(
    title="NGUYEN QUANG HIEU - Demo FastAPI",
    description="Language Detection",
    version="0.1",
)


# class TextIn(BaseModel):
#     text: str


# class PredictionOut(BaseModel):
#     language: str


def construct_response(f):
    """Construct a JSON response for an endpoint."""

    @wraps(f)
    def wrap(request: Request, *args, **kwargs) -> Dict:
        results = f(request, *args, **kwargs)
        response = {
            "message": results["message"],
            "method": request.method,
            "status-code": results["status-code"],
            "timestamp": datetime.now().isoformat(),
            "url": request.url._url,
        }
        if "data" in results:
            response["data"] = results["data"]
        return response

    return wrap

@app.get("/", tags=["General"])
@construct_response

def _index(request: Request) -> Dict:
    """Health check."""
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "model_version": model_version,
        "data": {},
    }
    return response

# @app.get("/")
# def home():
#     return {"health_check": "OK", "model_version": model_version}

# @app.post("/predict", response_model=PredictionOut)
# def predict(payload: TextIn):
#     language = predict_pipeline(payload.text)
#     return {"language": language}

@app.post("/predict", tags=["Prediction"])
@construct_response
def _predict(request: Request, payload: PredictPayload) -> Dict:
    """Predict tags for a list of texts."""
    text = str(payload.texts)
    predictions = predict_pipeline(text)
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {"predictions": predictions},
    }
    return response