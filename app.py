import streamlit as st
import asyncio
from consultation_agent import consult_professor_balthazar  # Her function

st.set_page_config(page_title="Professor Baltazar", page_icon="🎩")
st.title("Professor Baltazar's Magic Machine")
st.caption("Type your problem—watch the magic! (Creative reframing + emotional support)")

if "responses" not in st.session_state:
    st.session_state.responses = []

for resp in st.session_state.responses:
    st.write("**Baltazar:** " + resp)

if prompt := st.chat_input("What's your problem today?"):
    with st.spinner("The machine whirs..."):
        response = asyncio.run(consult_professor_balthazar(prompt))
        # Your twist: If angry, add rephrase
        if "angry" in prompt.lower():
            response += "\n\nEmotional Tip: Rephrase to polite: 'I appreciate the feedback—let's align.'"
    st.session_state.responses.append(response)
    st.rerun()

st.caption("Creative inventions from Baltazar! ⚙️✨")
