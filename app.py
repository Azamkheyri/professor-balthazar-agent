import streamlit as st
from graph import app  # Your new graph
from langchain_core.messages import HumanMessage

st.title("🤖 Professor Baltazar Advisor")
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["type"]).markdown(msg["content"])

if prompt := st.chat_input("Your problem?"):
    st.session_state.messages.append({"type": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)
    
    inputs = {"messages": [HumanMessage(content=prompt)]}
    with st.chat_message("assistant"):
        for output in app.stream(inputs):
            resp = output["messages"][-1].content
            st.markdown(resp)
        st.session_state.messages.append({"type": "assistant", "content": resp})

st.caption("Creative solutions from Baltazar's team!")
