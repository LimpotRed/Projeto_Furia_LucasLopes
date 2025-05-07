import streamlit as st
import time

st.set_page_config(page_title="🎮 Match Profile", layout="wide")

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
st.markdown("""
<div class="top-bar">
    <img src="https://furiagg.fbitsstatic.net/sf/img/logo-furia.svg?theme=main&v=202503171541"
         alt="Logo FURIA" style="height: 48px;">
</div>
""", unsafe_allow_html=True)

if "mostrar_resultado" not in st.session_state:
    st.session_state.mostrar_resultado = False

if not st.session_state.mostrar_resultado:
    st.title("Qual jogador da FURIA representa você?")
    
    respostas = {
        "estilo": st.radio("Seu estilo de jogo:", ["Agressivo", "Tático", "Versátil", "Suporte"]),
        "arma": st.selectbox("Arma favorita:", ["AK-47", "M4A4", "AWP", "Desert Eagle", "MP9"]),
        "funcao": st.selectbox("Função principal:", ["Entry Fragger", "IGL", "AWPer", "Clutcher", "Suporte"]),
        "posicao": st.radio("Prefere CT ou TR?", ["CT", "TR", "Tanto faz"]),
        "utilitarios": st.radio("Uso de utilitários:", ["Sempre", "Às vezes", "Quase nunca"]),
        "comunicacao": st.radio("Nível de comunicação:", ["Alto", "Moderado", "Baixo"]),
        "clutch": st.radio("Você se sai bem no clutch?", ["Sim", "Depende", "Evito"]),
        "lidera": st.radio("Prefere liderar ou seguir calls?", ["Liderar", "Seguir", "Depende"]),
        "joga_solo": st.radio("Prefere solo ou grupo?", ["Solo", "Grupo", "Ambos"]),
        "pressao": st.radio("Como lida com pressão?", ["Frio e calculista", "Ansioso mas ativo", "Prefiro não decidir"])
    }

    if st.button("Descobrir jogador correspondente"):
        pontuacoes = {"FalleN": 0, "KSCERATO": 0, "Yuurih": 0, "YEKINDAR": 0, "Molodoy": 0}

        if respostas["funcao"] == "IGL" or respostas["lidera"] == "Liderar": pontuacoes["FalleN"] += 2
        if respostas["arma"] == "AWP": pontuacoes["FalleN"] += 1
        if respostas["comunicacao"] == "Alto": pontuacoes["FalleN"] += 1
        if respostas["estilo"] == "Agressivo" and respostas["funcao"] == "Entry Fragger": pontuacoes["YEKINDAR"] += 2
        if respostas["pressao"] == "Frio e calculista": pontuacoes["KSCERATO"] += 2
        if respostas["clutch"] == "Sim": pontuacoes["KSCERATO"] += 1
        if respostas["joga_solo"] == "Solo": pontuacoes["KSCERATO"] += 1
        if respostas["estilo"] == "Versátil": pontuacoes["Yuurih"] += 2
        if respostas["funcao"] == "Clutcher": pontuacoes["Yuurih"] += 1
        if respostas["utilitarios"] == "Sempre" or respostas["funcao"] == "Suporte": pontuacoes["Molodoy"] += 2

        st.session_state.jogador_final = max(pontuacoes, key=pontuacoes.get)
        st.session_state.mostrar_resultado = True
        st.rerun()
else:
    imagens = {
        "FalleN": "images/match_player_fallen.png",
        "KSCERATO": "images/match_player_kscerato.png",
        "Yuurih": "images/match_player_yuurih.png",
        "YEKINDAR": "images/match_player_yekindar.png",
        "Molodoy": "images/match_player_molodoy.png"
    }
    
    descricoes = {
        "FalleN": "Você é um líder nato, com visão de jogo apurada e foco estratégico. Seu estilo inspira o time.",
        "KSCERATO": "Você é frio, letal e confiante. Brilha nos momentos decisivos e sabe vencer no clutch.",
        "Yuurih": "Você é equilibrado, confiável e se adapta bem a qualquer situação. Um verdadeiro coringa.",
        "YEKINDAR": "Você é ousado, acelera o ritmo e abre caminhos no jogo. Joga pra frente sem medo.",
        "Molodoy": "Você é o cérebro tático da equipe. Sempre pronto para dar suporte e fazer a play brilhar."
    }

    jogador_final = st.session_state.jogador_final
    
    st.markdown("## Resultado do Match Profile")
    
    with st.spinner("Analisando seu perfil tático..."):
        time.sleep(1.5)
    
    st.image(imagens[jogador_final], use_container_width=True)
    st.markdown(f"### Você se parece com: **{jogador_final}**")
    st.markdown(f"#### {descricoes[jogador_final]}")
    
    if st.button("Refazer Teste"):
        st.session_state.mostrar_resultado = False
        st.rerun()