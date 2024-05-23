import streamlit as st
from main import response

st.title("💬 Game Recommendation LLM")
st.write('🚀 Powered by langchain, OpenAI, RAGs and Streamlit')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

 # Display assistant response in chat message container
    with st.chat_message("assistant"):
        llm_response = response(prompt)
        response = st.write(llm_response)
        print(llm_response)
    st.session_state.messages.append({"role": "assistant", "content": response})