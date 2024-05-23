from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import LanceDB
from dotenv import load_dotenv
import os 

load_dotenv()



def create_qa_chain(db, api_key):
    embeddings = OpenAIEmbeddings(
        deployment="SL-document_embedder",
        model="text-embedding-ada-002",
        show_progress_bar=True,
        openai_api_key=api_key
    )

    docsearch = LanceDB(connection=db, embedding=embeddings)
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo-1106",
        temperature=0,
        api_key=api_key
    )

    template = """You are a game recommender system that help users to find games that match their preferences.
    Use the following pieces of context to answer the question at the end.
    For each question, suggest three games, with a short description of the game and the reason why the user might like it.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.

    {context}

    Question: {question}
    Your response:"""

    PROMPT = PromptTemplate(
        template=template, input_variables=["context", "question"]
    )

    chain_type_kwargs = {"prompt": PROMPT}

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=docsearch.as_retriever(),
        return_source_documents=True,
        chain_type_kwargs=chain_type_kwargs
    )

    return qa_chain


if __name__ == "__main__":
    from setup_db import setup_database

    uri = "dataset/sample-games-lancedb"
    api_key = os.getenv("OPENAPIKEY")
    db = setup_database(uri, "C:/Users/Atharva/Desktop/sample_project_1/GameRecommendationSystem/data/games.pkl")
    create_qa_chain(db, api_key)
