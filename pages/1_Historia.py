import streamlit as st

st.set_page_config(page_title="📖 História", layout="wide")



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

# Conteúdo principal da página
st.title("A História da FURIA")
st.image("images/logo_furia.png", width=90)

st.markdown("""
Fundada em 2017, a **FURIA Esports** se tornou uma potência no CS:GO e CS2 com estilo agressivo, disciplina tática e forte conexão com os fãs.

### 📅 Linha do tempo:
- 🏆 **2017:** Criação
- 🔥 **2019:** Tier 1 mundial
- 🌎 **2020:** Consolidação NA
- 🎯 **2022:** Destaques em majors
- 🚀 **2024:** Transição ao CS2

### 🏅 Conquistas:
- 🥇 DreamHack Open Anaheim 2020
- 🏆 Elisa Invitational Fall 2021
- 🏅 IEM Dallas 2022 (Top 4)
- 🌟 IEM Rio Major 2022 (Top 8)

### 🎮 Outras frentes:
VALORANT, CBLOL, Rocket League, Apex e mais.
""")

st.markdown("### 🎥 No primeiro Major no Brasil, a FURIA passou o carro na poderosa NAVI em uma MD3 inesquecível!")
st.video("https://www.youtube.com/watch?v=VmXg73AYRCg")