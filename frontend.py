import streamlit as st
import requests
import os
from urllib.parse import quote

st.title("A Simple Chat System")

if "openrouter_api_token" not in st.session_state:
    st.session_state.openrouter_api_token = os.getenv("OPENROUTER_API_KEY")
if "host" not in st.session_state:
    st.session_state.host = os.getenv("BASE_URL")

user_input = st.text_input("Ask me something")
user_input_encode = quote(user_input)

model_id = "nvidia/nemotron-3-ultra-550b-a55b:free"
model_id_encode = quote(model_id)

# this is the button and the action that it takes when it is clicked
if st.button("chat"):
    ENDPOINT = (
        f"{st.session_state.host}/chat?model_id={model_id_encode}&"
        f"openrouter_token={st.session_state.openrouter_api_token}&"
        f"input={user_input_encode}"
    )
    print(ENDPOINT)
    with st.spinner(f"Calling {model_id}..."):
        response = requests.get(ENDPOINT)
        if response.status_code == 200:
            st.success("Success!")
            st.write(response.json().get("ack"))
        else:
            st.error(f"Failed: {response.status_code}")

# Add additional endpoints/buttons as needed
