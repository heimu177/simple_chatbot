import streamlit as st
from langchain.chains import ConversationChain
from langchain_community.llms import Ollama

# Initialize the conversation chain
llm = Ollama(model="llama3", temperature=0.7)
conversation = ConversationChain(llm=llm, verbose=True)

# Create a Streamlit app
st.title("Chatbot with Memory")
st.write("This chatbot remembers previous conversations.")

# Initialize session state for conversation history
if 'history' not in st.session_state:
    st.session_state.history = []

# Create a text input for the user to type
user_input = st.text_input("Type a message:")

# Create a button to send the message
if st.button("Send"):
    # Get the user's message
    message = user_input
    
    # Get the response from the conversation chain
    response = conversation.predict(input=message)
    
    # Add the interaction to the history
    st.session_state.history.append(f"Human: {message}")
    st.session_state.history.append(f"AI: {response}")

    # Display the response
    st.write("Model:", response)

# Display the conversation history
st.subheader("Conversation History:")
for message in st.session_state.history:
    st.text(message)