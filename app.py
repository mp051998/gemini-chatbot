
import streamlit as st

from config.globals import SPEAKER_TYPES

from services.google.generative_ai import GeminiProModelChat


chat_conversation = GeminiProModelChat()

# Set up the streamlit app
st.set_page_config(
  page_title="Gemini Pro Demo App",
  page_icon="🤖",
  layout="wide",
  initial_sidebar_state="expanded",
)

# Initialize a session state to hold the chat history
if 'chat_history' not in st.session_state:
  st.session_state.chat_history = []

with st.sidebar:
  st.title('♊💬 Gemini Chatbot')
  st.write('This chatbot uses Gemini Pro API.')

# Get user input and generate response
prompt = st.chat_input("Ask Gemini Pro a question...", key="user_input")
if prompt:
  st.session_state['chat_history'].append((SPEAKER_TYPES.USER, prompt))
  response_text = chat_conversation.get_gemini_response(prompt, stream=False)
  st.session_state['chat_history'].append((SPEAKER_TYPES.BOT, response_text))
    
# Show the chat
for speaker, message in st.session_state['chat_history']:
  with st.chat_message(speaker, avatar="👤" if speaker == SPEAKER_TYPES.USER else "🤖"):
    st.write(message)

