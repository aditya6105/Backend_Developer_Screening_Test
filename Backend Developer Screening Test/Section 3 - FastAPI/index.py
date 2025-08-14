from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

api = FastAPI()

class ScoreList(BaseModel):
    scores: List[int]

@api.post("/average-score")
def calc_average(data: ScoreList):
    if not data.scores:
        raise HTTPException(status_code=400, detail="Score list cannot be empty")
    try:
        average_value = sum(data.scores) / len(data.scores)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    return {"average": average_value}
