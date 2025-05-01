import os
from typing import List, Optional

import joblib
import uvicorn
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel


app = FastAPI(title="Secured Wine Classifier")
MODEL = joblib.load("wine_clf.joblib")
CLASS_NAMES = ["Cultivar-0", "Cultivar-1", "Cultivar-2"]  # rename at will


load_dotenv()
API_KEY = os.getenv("API_KEY")
API_KEY_NAME = "X-API-Key"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(api_key: Optional[str] = Security(api_key_header)):
    if api_key == API_KEY:
        return api_key
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid API Key",
        headers={"WWW-Authenticate": "Bearer"},
    )
    

class WineRequest(BaseModel):
    data: List[List[float]]  # each inner list: 13 numeric features


class WineResponse(BaseModel):
    predictions: List[str]


@app.post("/predict", response_model=WineResponse, dependencies=[Depends(get_api_key)])
async def predict(payload: WineRequest):
    preds = MODEL.predict(payload.data)
    labels = [CLASS_NAMES[i] for i in preds]
    return WineResponse(predictions=labels)


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
