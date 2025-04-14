import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Load data
products = pd.read_csv("backend/data/products.csv")

# Load models
with open("backend/models/tfidf_model.pkl", "rb") as f:
    tfidf_matrix = pickle.load(f)

with open("backend/models/cf_model.pkl", "rb") as f:
    user_cf = pickle.load(f)

def get_user_recommendations(user_id):
    if user_id not in user_cf:
        return []
    return user_cf[user_id]

def get_similar_products(product_id):
    idx = products[products['product_id'] == product_id].index[0]
    cosine_sim = cosine_similarity(tfidf_matrix[idx:idx+1], tfidf_matrix).flatten()
    sim_scores = list(enumerate(cosine_sim))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices = [i for i, score in sim_scores[1:6]]  # top 5 excluding self
    return products.iloc[top_indices]['product_id'].tolist()
