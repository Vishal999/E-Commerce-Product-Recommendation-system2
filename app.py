### backend/app/ain.pym
from fastapi import FastAPI
from app.routes import recommendation_routes

app = FastAPI()

app.include_router(recommendation_routes.router)

@app.get("/")
def read_root():
    return {"message": "E-Commerce Product Recommendation API"}


### backend/app/routes/recommendation_routes.py
from fastapi import APIRouter
from app.models.recommendation_model import get_user_recommendations, get_similar_products

router = APIRouter()

@router.get("/recommend/user/{user_id}")
def recommend_for_user(user_id: str):
    return get_user_recommendations(user_id)

@router.get("/recommend/product/{product_id}")
def similar_products(product_id: str):
    return get_similar_products(product_id)


### backend/app/models/recommendation_model.py
import pickle
import pandas as pd

# Load data and models
user_interactions = pd.read_csv("data/user_interactions.csv")
products = pd.read_csv("data/products.csv")

with open("ml_models/collaborative_model.pkl", "rb") as f:
    collaborative_model = pickle.load(f)

with open("ml_models/content_based_model.pkl", "rb") as f:
    content_based_model = pickle.load(f)

def get_user_recommendations(user_id):
    try:
        recommended_ids = collaborative_model.get(user_id, [])
        recommended = products[products['product_id'].isin(recommended_ids)].to_dict(orient="records")
        return {"user_id": user_id, "recommendations": recommended}
    except:
        return {"error": "User not found or model error."}

def get_similar_products(product_id):
    try:
        similar_ids = content_based_model.get(product_id, [])
        similar = products[products['product_id'].isin(similar_ids)].to_dict(orient="records")
        return {"product_id": product_id, "similar_products": similar}
    except:
        return {"error": "Product not found or model error."}


### backend/requirements.txt
fastapi
uvicorn
pandas
scikit-learn
pickle-mixin


### backend/Dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


### docker-compose.yml
version: '3.8'
services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/app
    restart: always


### README.md
# E-Commerce Product Recommendation App

## Features
- User-based and product-based recommendation API
- FastAPI backend with pre-trained models
- Dockerized for deployment

## Getting Started
1. Clone the repo
2. Train your models in `ml_models/training_notebooks/train_models.ipynb`
3. Run with Docker:
```bash
docker-compose up --build
```

## API Endpoints
- `GET /recommend/user/{user_id}`
- `GET /recommend/product/{product_id}`

## Tech Stack
- FastAPI, Scikit-learn, Docker
