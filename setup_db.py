import pandas as pd
import lancedb

def setup_database(uri, games_path):
    games = pd.read_pickle(games_path)
    db = lancedb.connect(uri)
    # table = db.create_table("vectorstore", games)
    return db

if __name__ == "__main__":
    uri = "dataset/sample-games-lancedb"
    games_path = "C:/Users/Atharva/Desktop/sample_project_1/GameRecommendationSystem/data/games.pkl"
    setup_database(uri, games_path)
