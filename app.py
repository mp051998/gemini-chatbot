
import streamlit as st

from config.globals import SPEAKER_TYPES, initial_prompt

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
  st.session_state.chat_history = [initial_prompt]

def clear_chat_history():
  st.session_state.chat_history = [initial_prompt]

with st.sidebar:
  st.title('♊💬 Gemini Chatbot')
  st.write('This chatbot uses Gemini Pro API.')  
  st.sidebar.button('Clear Chat History', on_click=clear_chat_history, type='primary')

# Get user input and generate response
prompt = st.chat_input("Ask Gemini Pro a question...", key="user_input")

# Show the welcome prompt
with st.chat_message(SPEAKER_TYPES.BOT, avatar="🤖"):
  st.write(initial_prompt['content'])

if prompt:
  st.session_state['chat_history'].append({'role': SPEAKER_TYPES.USER, 'content': prompt})
  
  # Display chat messages
  for message in st.session_state.chat_history[1:]:
    with st.chat_message(message["role"], avatar="👤" if message['role'] == SPEAKER_TYPES.USER else "🤖"):
      st.write(message["content"])
  
  response_stream = chat_conversation.get_gemini_response(prompt, stream=True)
  response_text = ''
  with st.chat_message(SPEAKER_TYPES.BOT, avatar="🤖"):
    placeholder = st.empty()
    with st.spinner(text='Generating response...'):
      for chunk in response_stream:
        response_text += chunk.text
        placeholder.markdown(response_text)
      placeholder.markdown(response_text)
  st.session_state['chat_history'].append({'role': SPEAKER_TYPES.BOT, 'content': response_text})

