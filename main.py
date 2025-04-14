from fastapi import FastAPI
from recommend import get_user_recommendations, get_similar_products

app = FastAPI()

@app.get("/recommend/user/{user_id}")
def recommend_for_user(user_id: str):
    return {"recommendations": get_user_recommendations(user_id)}

@app.get("/recommend/product/{product_id}")
def recommend_similar_products(product_id: str):
    return {"similar_products": get_similar_products(product_id)}
