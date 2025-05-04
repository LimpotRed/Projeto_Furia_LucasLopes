import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="👥 Fãs", layout="wide")
st.title("Fãs da FURIA")

# Ajuste no estilo da barra e espaçamento do conteúdo
st.markdown("""
    <style>
        /* Esconde barra do Streamlit (menu, deploy, etc.) */
        #MainMenu, header, footer { visibility: hidden; height: 0px; }
        
        /* Ajusta espaçamento do conteúdo para não ser sobreposto pela barra */
        .block-container { padding-top: 100px !important; }
        
        /* Estiliza a barra fixa */
        .top-bar {
            position: fixed;
            width: 100vw;
            top: 0;
            left: 140px;
            background-color: #f7f7f7;
            height: 80px;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 1000;
        }
    </style>
""", unsafe_allow_html=True)

# Barra fixa com logo FURIA
st.markdown("""
<div class="top-bar">
    <img src="https://furiagg.fbitsstatic.net/sf/img/logo-furia.svg?theme=main&v=202503171541"
         alt="Logo FURIA" style="height: 48px;">
</div>
""", unsafe_allow_html=True)

# Título da página
st.title("Base Know Your Fan")

# Carregar dados do CSV
if os.path.exists("dados_fas.csv"):
    df = pd.read_csv("dados_fas.csv", header=None)
    df.columns = [
        "Nome Completo", "Nick", "CPF", "Endereço", "Idade", "Região",
        "Tempo de fã", "Jogador favorito", "Eventos", "Produtos",
        "Steam", "Twitter", "Instagram", "Perfil externo"
    ]
    
    # Filtrar colunas para exibição pública
    df_publico = df[["Nick", "Idade", "Steam", "Instagram"]].dropna()
    df_publico = df_publico.rename(columns={
        "Nick": "Nick (in-game)",
        "Steam": "Perfil Steam",
        "Instagram": "Instagram"
    })
    
    # Exibir a tabela na interface
    st.dataframe(df_publico.reset_index(drop=True))

else:
    st.info("Nenhum dado encontrado ainda. Envie o formulário para começar.")