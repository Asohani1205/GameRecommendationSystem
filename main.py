import pandas as pd
# from embedding_utils import process_embeddings
from setup_db import setup_database
from llm_utils import create_qa_chain
from langchain_community.callbacks import get_openai_callback
from dotenv import load_dotenv
import os 

load_dotenv()

def response(prompt):
    openai_api_key = os.getenv("OPENAPIKEY")
    uri = "dataset/sample-games-lancedb"
    db = setup_database(uri, "data/games.pkl")

    qa_chain = create_qa_chain(db, openai_api_key)

    with get_openai_callback() as cb:
        result = qa_chain({"query": prompt})

    return result['result']


def modelPipeline():
    openai_api_key = os.getenv("OPENAPIKEY")

    # Step 1: Process Embeddings
    games = pd.read_csv('C:/Users/Atharva/Desktop/sample_project_1/GameRecommendationSystem/data/games.csv')
    games = games.dropna()
    games['combined_info'] = games.apply(lambda row: f"Title: {row['title']}. Category: {row['category']} Installs: {row['installs']} Rating: {row['average rating']} ", axis=1)
    # process_embeddings(games, openai_api_key)

    print("\nCOMPLETED STEP 1\n")

    # Step 2: Setup Database
    uri = "dataset/sample-games-lancedb"
    db = setup_database(uri, "data/games.pkl")

    print("\nCOMPLETED STEP 2\n")


    # Step 3: Create QA Chain
    qa_chain = create_qa_chain(db, openai_api_key)

    print("\nCOMPLETED STEP 3\n")


    # Step 4: Query and Response
    query = "I'm looking for an action game. What could you suggest to me?"
    with get_openai_callback() as cb:
        result = qa_chain({"query": query})
    print("\nCOMPLETED STEP 4\n")
    print(result['result'])

if __name__ == "__main__":
    response("Give me a multiplayer game")
