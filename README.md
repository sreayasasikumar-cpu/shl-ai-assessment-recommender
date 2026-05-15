# SHL AI Assessment Recommender

## Project Overview

This project is an AI-powered assessment recommendation system built for the SHL Internship Assignment.

The system recommends suitable SHL assessments based on natural language queries such as:

- "Need personality assessment for leadership role"
- "Looking for cognitive ability test for freshers"
- "Need communication assessment for customer support hiring"

The application uses semantic similarity and NLP embeddings to retrieve the most relevant assessments from a catalog.

---

## Features

- FastAPI-based REST API
- Semantic search using Sentence Transformers
- Intelligent assessment recommendation
- Public API deployment using Render
- Swagger API documentation
- JSON-based assessment catalog

---

## Tech Stack

- Python
- FastAPI
- Sentence Transformers
- scikit-learn
- NumPy
- Uvicorn
- Render (Deployment)

---

## Project Structure

```text
app/
│
├── main.py
├── retriever.py
├── catalog.json
├── embed.py
└── prompts.py

requirements.txt
```

---

## API Deployment

### Live API URL

https://shl-ai-assessment-recommender-8owo.onrender.com

### Swagger Documentation

https://shl-ai-assessment-recommender-8owo.onrender.com/docs

---

## API Endpoints

### GET /

Health check endpoint.

#### Response

```json
{
  "message": "SHL Assessment Recommendation API Running"
}
```

---

### POST /recommend

Returns recommended SHL assessments based on user query.

#### Sample Request

```json
{
  "query": "Need personality assessment for leadership role"
}
```

#### Sample Response

```json
{
  "query": "Need personality assessment for leadership role",
  "recommendations": [
    {
      "name": "OPQ32r",
      "url": "https://www.shl.com/products/product-catalog/view/occupational-personality-questionnaire-opq32r/",
      "description": "Measures workplace personality traits, behavioral style, and job-related preferences to predict workplace performance.",
      "test_type": "Personality",
      "score": 0.84
    }
  ]
}
```

---

## Installation & Local Setup

### Clone Repository

```bash
git clone https://github.com/sreayasasikumar-cpu/shl-ai-assessment-recommender.git
```

### Move Into Project

```bash
cd shl-ai-assessment-recommender
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
uvicorn app.main:app --reload
```

---

## Future Improvements

- Expand assessment catalog
- Add hybrid filtering and ranking
- Improve recommendation accuracy
- Add LLM-based query understanding
- Add frontend UI

---

## Author

Sreaya Sasikumar
