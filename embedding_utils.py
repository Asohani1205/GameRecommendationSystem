import tiktoken
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
import os 

load_dotenv()

def process_embeddings(games, api_key):
    embedding_model = "text-embedding-ada-002"
    embedding_encoding = "cl100k_base"
    max_tokens = 8000

    encoding = tiktoken.get_encoding(embedding_encoding)
    games["n_tokens"] = games.combined_info.apply(lambda x: len(encoding.encode(x)))
    games = games[games.n_tokens <= max_tokens]

    client = OpenAI(api_key=api_key)
    def get_embedding(text, model="text-embedding-3-small"):
        text = text.replace("\n", " ")
        return client.embeddings.create(input=[text], model=model).data[0].embedding

    games["embedding"] = games.combined_info.apply(lambda x: get_embedding(x, model=embedding_model))
    games.rename(columns={'embedding': 'vector', 'combined_info': 'text'}, inplace=True)
    games.to_pickle('C:/Users/Atharva/Desktop/sample_project_1/GameRecommendationSystem/data/games.pkl')
    return games

if __name__ == "__main__":
    games = pd.read_csv('C:/Users/Atharva/Desktop/sample_project_1/GameRecommendationSystem/data/games.csv')
    games['combined_info'] = games.apply(lambda row: f"Title: {row['title']}. Category: {row['category']} Installs: {row['installs']} Rating: {row['average rating']} ", axis=1)
    api_key = os.getenv("OPENAPIKEY")
    process_embeddings(games, api_key)
