## Overview
This project is a Game Recommendation System designed to suggest games to users based on various criteria such as ratings and downloads. The system leverages a dataset from Kaggle and utilizes advanced machine learning and natural language processing techniques to deliver recommendations through an interactive web interface.
## Dataset Selection
The dataset used for this project is named "Top Games" and was sourced from Kaggle. It includes details about various games, including their ratings, downloads, and other relevant attributes.
## Libraries and Tools Used
To build this system, the following libraries and tools were employed:
•	pandas: For data manipulation and analysis.
•	tiktoken: For tokenizing the data.
•	lancedb: For creating and managing a vector database.
•	openai: To interact with OpenAI's language models.
•	langchain_openai: To integrate OpenAI embeddings and language models into the project.
•	RetrievalQA: For implementing a retrieval-augmented generation (RAG) approach.
•	PromptTemplate: For creating structured prompts for the language model.
•	get_openai_callback: For managing OpenAI API callbacks.
•	LanceDB: For storing and retrieving vectorized data.
•	pickle: For serializing data.
•	streamlit: For building the user interface and deploying the application.
## Architecture Diagram
 ![image](https://github.com/Asohani1205/GameRecommendationSystem/assets/100613203/1fa521b4-5af6-4d2c-86cd-a032e9f4e616)



# RAG and LLM Explanation
## Retrieval-Augmented Generation (RAG)
Retrieval-Augmented Generation is a method that combines information retrieval with text generation. In the context of this project:
1.	Retrieval: When a user provides a prompt, the system first retrieves relevant chunks of information from a vector database using semantic search. This helps in finding the most relevant pieces of data that can aid in answering the query.
2.	Augmentation: The retrieved information is then used to augment the generation process. This means that the language model uses this information as context to produce a more accurate and relevant response.
3.	Generation: Finally, the language model generates a response based on the retrieved context and the user's query.
## Large Language Models (LLM)
Large Language Models are advanced AI models capable of understanding and generating human-like text. These models, such as GPT-3 and GPT-4, are trained on vast amounts of text data and can perform a wide range of language tasks. In this project, LLMs are used for:
1.	Text Embeddings: Converting textual information into high-dimensional vectors that capture the semantic meaning of the text.
2.	Question Answering: Generating human-like responses to user queries based on the context provided by the retrieved information.
3.	Recommendations: Providing game recommendations by understanding the user's preferences and leveraging the contextual information from the vector database.
## Project Structure
 ![image](https://github.com/Asohani1205/GameRecommendationSystem/assets/100613203/120b28ff-33fc-4599-a29f-c4b7e354fbf6)

## Steps Followed
1. Data Preparation
•	Dataset Selection: The "Top Games" dataset from Kaggle was chosen based on the requirements.
•	Data Loading and Cleaning: The dataset was loaded into a pandas DataFrame for preprocessing.
2. Embedding and Vectorization
•	Embedding the Dataset: Each game in the dataset was converted into a vector using the OpenAI embeddings.
•	Serialization: The vectorized data was serialized using the pickle library and stored in a database.
3. Database Management
•	Creating a Vector Database: LanceDB was used to create a table and manage the vectorized data.
•	Vector Storage and Retrieval: The vectors were stored and later retrieved efficiently using LanceDB.
4. Model Integration
•	OpenAI API: The OpenAI API was utilized for language model capabilities, enabling the system to understand and generate natural language responses.
•	Retrieval-Augmented Generation (RAG): This technique was implemented to optimize the output of the language model by augmenting it with relevant retrieved data.
5. Building the Interface
•	Streamlit: Streamlit was used to create a user-friendly web interface for the game recommendation system.
•	Interface Design: The interface includes a chat-like interaction where users can input queries and receive recommendations.
## Links
•	GitHub Repository:  https://github.com/Asohani1205/GameRecommendationSystem

•	Website:  https://gamellm.streamlit.app/


## Conclusion
This project successfully demonstrates how to build a sophisticated game recommendation system using modern machine learning and NLP techniques. By leveraging tools like OpenAI, LanceDB, and Streamlit, the system provides accurate and interactive game recommendations, showcasing the potential of AI in enhancing user experiences.
