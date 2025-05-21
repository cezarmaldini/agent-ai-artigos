# app.py
import streamlit as st
from graph import build_graph

st.set_page_config(page_title="Chatbot com IA", layout="wide")
st.title("🤖 Chatbot de Geração de Artigos com IA")
st.markdown("Converse com o agente para criar um artigo com base no tema que você for discutindo.")

# Inicializa o histórico do chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe as mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada de mensagem do usuário
prompt = st.chat_input("Digite sua mensagem aqui...")

if prompt:
    # Adiciona a mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Processa a resposta com seu agente IA
    with st.chat_message("assistant"):
        with st.spinner("Aguarde, processando..."):
            flow = build_graph()
            response = flow.invoke({"topic": prompt})
            final_article = response.get("final_article", "Desculpe, não consegui gerar uma resposta.")
            st.markdown(final_article)

    # Adiciona a resposta do agente ao histórico
    st.session_state.messages.append({"role": "assistant", "content": final_article})