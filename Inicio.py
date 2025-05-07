import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="Furia", layout="wide")

def get_base64_img(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

st.markdown("""
    <style>
        #MainMenu, header, footer { visibility: hidden; height: 0px; }
        .block-container { padding-top: 100px !important; }

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

        .player-card {
            background: linear-gradient(to bottom, #1f1f1f, #141414);
            border-radius: 20px;
            padding: 15px;
            text-align: center;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.05);
            transition: 0.3s ease;
        }

        .player-card:hover {
            transform: scale(1.03);
            box-shadow: 0 0 20px rgba(0, 191, 255, 0.2);
        }

        .player-img {
            width: 100%;
            border-radius: 10px;
            object-fit: contain;
        }

        .player-name {
            font-weight: 600;
            font-size: 18px;
            color: #fff;
            margin-top: 10px;
        }

        .player-role {
            font-size: 14px;
            color: #bbb;
            margin-bottom: 5px;
        }

        .player-link a {
            font-size: 14px;
            color: #00bfff;
            text-decoration: none;
        }

        [data-testid="stHorizontalBlock"] {
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)
st.markdown("""
<div class="top-bar">
    <img src="https://furiagg.fbitsstatic.net/sf/img/logo-furia.svg?theme=main&v=202503171541"
         alt="Logo FURIA" style="height: 48px;">
</div>
""", unsafe_allow_html=True)

st.title("De um fã da FURIA para outros fãs")

st.markdown("""
Seja bem-vindo ao nosso cantinho feito com muito carinho por quem vibra a cada clutch, a cada spray certeiro e a cada vitória da Pantera!

Aqui, você vai conhecer o elenco atual, mergulhar em histórias emocionantes e deixar sua marca como verdadeiro integrante da FURIA FAMILY. Você é parte do rugido.
""")

st.image("images/logo_furia.png", width=100)

st.markdown("## Elenco atual da Pantera")

jogadores = [
    {"nome": "FalleN", "posicao": "IGL / AWPer", "img": "Inicio_assets/fallen.png", "link": "https://steamcommunity.com/id/fallencs/"},
    {"nome": "KSCERATO", "posicao": "Rifler", "img": "Inicio_assets/kscerato.png", "link": "https://steamcommunity.com/id/kscthebesten/"},
    {"nome": "Yuurih", "posicao": "Rifler", "img": "Inicio_assets/yuurih.png", "link": "https://steamcommunity.com/id/ahsislife"},
    {"nome": "YEKINDAR", "posicao": "Entry Fragger", "img": "Inicio_assets/yekindar.png", "link": "https://steamcommunity.com/id/yrgod/"},
    {"nome": "Molodoy", "posicao": "Suporte", "img": "Inicio_assets/molodoy.png", "link": "https://steamcommunity.com/profiles/76561198200982290"},
]

cols = st.columns(len(jogadores))
for i, jogador in enumerate(jogadores):
    with cols[i]:
        img_base64 = get_base64_img(jogador["img"])
        st.markdown(f"""
        <div class="player-card">
            <img src="data:image/png;base64,{img_base64}" class="player-img">
            <div class="player-name">{jogador['nome']}</div>
            <div class="player-role">{jogador['posicao']}</div>
            <div class="player-link"><a href="{jogador['link']}" target="_blank">Perfil Steam</a></div>
        </div>
        """, unsafe_allow_html=True)
