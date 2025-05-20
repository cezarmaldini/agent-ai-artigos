# app.py
import streamlit as st
from graph import build_graph

st.set_page_config(page_title="Gerador de Artigos com IA", layout="wide")

st.title("📝 Gerador de Artigos com IA")
st.markdown("Insira um tema e deixe que nossos agentes façam a pesquisa, escrita e revisão para você.")

# Campo para entrada do tema
topic = st.text_input("Tema do artigo", placeholder="Ex: Uso da inteligência artificial na área da saúde.")

# Botão para iniciar o processo
if st.button("Gerar Artigo"):
    if topic:
        with st.spinner("Pesquisando, escrevendo e revisando..."):
            flow = build_graph()
            result = flow.invoke({"topic": topic})
            final_article = result["final_article"]

        st.success("✅ Artigo gerado com sucesso!")
        st.subheader("📄 Artigo Final:")
        st.write(final_article)

        # Expansível com as opções de cópia ou download
        st.download_button("📥 Baixar artigo como TXT", data=final_article, file_name="artigo.txt")

    else:
        st.warning("Por favor, insira um tema para gerar o artigo.")