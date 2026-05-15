from fastapi import FastAPI
from pydantic import BaseModel
from app.retriever import retrieve_assessments

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {
        "message": "SHL Assessment Recommendation API Running"
    }

@app.post("/recommend")
def recommend_assessments(request: QueryRequest):
    results = retrieve_assessments(request.query)

    return {
        "query": request.query,
        "recommendations": results
    }