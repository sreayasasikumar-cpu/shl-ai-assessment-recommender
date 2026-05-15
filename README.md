# SHL Assessment Recommendation System

An AI-powered assessment recommendation API that suggests relevant SHL assessments based on user queries. The system matches user requirements such as technical skills, leadership, cognitive ability, personality, and communication skills with suitable SHL assessments.

---

# Project Overview

This project was developed as part of the SHL internship assignment. The application provides assessment recommendations through a FastAPI-based REST API.

Users can enter queries like:

- "Need Python developer assessment"
- "Need leadership assessment for managers"
- "Need cognitive ability test"
- "Need customer service assessment"

The API then returns the most relevant SHL assessments from the assessment catalog.

---

# Features

- FastAPI REST API
- SHL assessment recommendation engine
- Keyword-based intelligent matching
- Technical assessment recommendations
- Leadership assessment recommendations
- Cognitive ability assessment recommendations
- Personality assessment recommendations
- Communication assessment recommendations
- Swagger API documentation
- Render cloud deployment

---

# Tech Stack

- Python
- FastAPI
- Uvicorn
- JSON
- Render
- GitHub

---

# Project Structure

```bash
shl-ai-assessment-recommender/
│
├── app/
│   ├── main.py
│   ├── retriever.py
│   └── catalog.json
│
├── requirements.txt
└── README.md
```

---

# API Documentation

## Base URL

```bash
https://shl-ai-assessment-recommender-8owo.onrender.com
```

## Swagger Documentation

```bash
https://shl-ai-assessment-recommender-8owo.onrender.com/docs
```

---

# API Endpoint

## Recommend Assessments

### Endpoint

```bash
POST /recommend
```

### Sample Request

```json
{
  "query": "Need Python developer assessment"
}
```

### Sample Response

```json
{
  "query": "Need Python developer assessment",
  "recommendations": [
    {
      "name": "Python 3 (New)",
      "url": "https://www.shl.com/products/product-catalog/view/python-3-new/",
      "description": "Measures Python 3 programming knowledge including data types, control flow, functions, modules, file handling, and object-oriented programming.",
      "test_type": "Technical",
      "score": 1
    }
  ]
}
```

---

# Supported Assessment Categories

## Technical Assessments

- Python
- Java
- SQL
- .NET

## Leadership Assessments

- HiPo Assessment Report 1.0
- HiPo Assessment Report 2.0

## Cognitive Assessments

- Inductive Reasoning
- Deductive Reasoning
- Numerical Reasoning
- SHL Verify Interactive G+

## Personality Assessments

- OPQ32r

## Communication Assessments

- Customer Service Phone Simulation

---

# Deployment Links

## GitHub Repository

```bash
https://github.com/sreayasasikumar-cpu/shl-ai-assessment-recommender
```

## Render Deployment

```bash
https://shl-ai-assessment-recommender-8owo.onrender.com/
```

## Swagger Docs

```bash
https://shl-ai-assessment-recommender-8owo.onrender.com/docs
```

---

# Local Setup Instructions

## Clone Repository

```bash
git clone https://github.com/sreayasasikumar-cpu/shl-ai-assessment-recommender.git
```

## Move to Project Directory

```bash
cd shl-ai-assessment-recommender
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
uvicorn app.main:app --reload
```

## Open Swagger Docs

```bash
http://127.0.0.1:8000/docs
```

---

# Future Improvements

- Semantic search using embeddings
- NLP-based recommendation engine
- Better ranking and filtering
- Expanded SHL assessment catalog
- Frontend integration
- Database integration
- User authentication

---

# Author

Sreaya Sasikumar
