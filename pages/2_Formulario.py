import streamlit as st
import os
import tempfile
import re
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


st.set_page_config(page_title="📝 Formulário", layout="wide")
st.title("Formulário de Cadastro")

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
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="top-bar">
    <img src="https://furiagg.fbitsstatic.net/sf/img/logo-furia.svg?theme=main&v=202503171541"
         alt="Logo FURIA" style="height: 48px;">
</div>
""", unsafe_allow_html=True)

st.title("Seja um Fã Oficial da FURIA - Know Your Fan")

nome_completo = st.text_input("Nome completo")
nick = st.text_input("Seu nick no jogo (nome in-game)")
cpf = st.text_input("CPF (com a pontuação)")
endereco = st.text_input("Endereço completo")
idade = st.number_input("Idade", min_value=12, max_value=99, step=1)
regiao = st.selectbox("Sua região", ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"])
tempo_fa = st.selectbox("Há quantos anos acompanha a FURIA?", ["Menos de 1 ano", "1 ano", "2 anos", "3 anos", "4 anos ou mais"])
jogador_fav = st.text_input("Seu jogador favorito da FURIA")
eventos = st.text_area("Eventos presenciais ou online que participou?")
produtos = st.text_area("Produtos oficiais adquiridos nos últimos 12 meses?")
steam = st.text_input("Perfil Steam")
twitter = st.text_input("Twitter (opcional)")
instagram = st.text_input("Instagram (opcional)")
perfil_externo = st.text_input("Link que mostre sua paixão pela FURIA")

validado = False
st.markdown("### Envio de documento")
doc = st.file_uploader("Envie RG ou CNH (apenas imagem)", type=["png", "jpg", "jpeg"])

if doc is not None:
    with st.spinner("🔍 Verificando documento..."):
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
                tmp.write(doc.read())
                image_path = tmp.name

                imagem = Image.open(image_path)  

                
                st.image(imagem, caption="Imagem enviada", use_column_width=False)

               
                texto = pytesseract.image_to_string(imagem, lang='por')
                st.text_area("Texto extraído da imagem:", texto, height=200)

                
                match = re.search(r'(\d{3}\.?\d{3}\.?\d{3}-?\d{2})', texto)
                cpf_encontrado = re.sub(r'\D', '', match.group(1)) if match else ''

                st.text(f"CPF identificado: {cpf_encontrado if cpf_encontrado else 'Não identificado'}")

                cpf_digitado = re.sub(r'\D', '', cpf)

                if cpf_encontrado and cpf_encontrado == cpf_digitado:
                    st.success(f"✅ Documento validado com sucesso! CPF encontrado: {cpf_encontrado}")
                    validado = True
                else:
                    st.warning("⚠️ CPF não confere com o digitado ou não foi reconhecido corretamente.")

        except Exception as e:
            st.error(f"❌ Erro na leitura do documento: {e}")
        finally:
            try:
                os.remove(image_path)
            except Exception as e:
                st.warning(f"⚠️ Erro ao excluir arquivos temporários: {e}")


if st.button("Enviar"):
    if validado:
        try:
            caminho_csv = os.path.join(os.getcwd(), "dados_fas.csv")
            with open(caminho_csv, "a", encoding="utf-8") as f:
                f.write(f"{nome_completo},{nick},{cpf},{endereco},{idade},{regiao},{tempo_fa},{jogador_fav},{eventos},{produtos},{steam},{twitter},{instagram},{perfil_externo}\n")
            st.success("🎉 Dados enviados com sucesso!")
        except Exception as e:
            st.error(f"Erro ao salvar dados: {e}")
    else:
        st.error("❌ Envio bloqueado: o CPF do documento não confere com o digitado.")
