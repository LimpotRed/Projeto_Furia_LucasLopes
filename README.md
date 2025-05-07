# 🐾 Projeto FURIA: Know Your Fan

Este projeto foi desenvolvido com muito carinho por um verdadeiro fã da **FURIA Esports**, com o objetivo de conectar a torcida apaixonada com a equipe, por meio de um ambiente interativo, visual e informativo.

---

## 🎯 Objetivo

Criar um **portal de fãs da FURIA** que reúne:
- Cards interativos dos jogadores atuais  
- Linha do tempo com a história da organização  
- Formulário de cadastro de fãs com verificação de identidade  
- Base de dados com os cadastros recebidos  
- Match Profile (em desenvolvimento) para identificar com qual jogador o fã mais se parece  

---

## 🖼️ Visão Geral

O app possui cinco seções principais:

### 🔸 Início
- Apresentação dos jogadores com fotos e links para seus perfis Steam  
- Layout responsivo com cards estilizados  

### 🔸 História
- Linha do tempo da FURIA desde 2017  
- Principais conquistas e participação em outros games  
- Vídeo do IEM Rio Major 2022  

### 🔸 Formulário
- Coleta de dados como nome, idade, região, rede social, tempo de fã, etc.  
- Envio opcional de imagem de documento com **validação de CPF via OCR (local)**  
- Armazenamento local em um arquivo `dados_fas.csv`  

### 🔸 Fãs
- Tabela pública com os nicks e perfis dos fãs cadastrados  

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Streamlit** (interface web)
- **Pandas** (leitura de CSV)
- **Pillow** (manipulação de imagens)
- **Pytesseract** (OCR local para validação de documentos)
- **Tesseract-OCR** (executável obrigatório para usar o pytesseract)
- **CSS Customizado** (estilização visual dentro do Streamlit)

---

## 🚀 Acesse o App Online

👉 **[Clique aqui para acessar o app via Streamlit Cloud](https://projetofurialucaslopes-ly5gih7zknpv5djofe6n4u.streamlit.app/)**

> ⚠️ **Importante:** A validação OCR por imagem de documento **não está disponível na versão online**, pois o Streamlit Cloud não suporta bibliotecas que dependem de executáveis do sistema (como o Tesseract-OCR).

---

## 💻 Como Rodar o Projeto Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/limpotred/Projeto_Furia_Know_Your_Fan.git
cd Projeto_Furia_Know_Your_Fan

Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/macOS

Instale as dependências
pip install -r requirements.txt


Instale o Tesseract-OCR

Windows:
Baixe e instale em: https://github.com/tesseract-ocr/tesseract
Caminho padrão: C:\Program Files\Tesseract-OCR\tesseract.exe

Linux:
sudo apt update && sudo apt install tesseract-ocr

macOS:
brew install tesseract

Execute o app
streamlit run Inicio.py

🧠 Autor
Lucas Lopes
Fã da FURIA e entusiasta de tecnologia
GitHub - https://github.com/limpotred

📌 Licença
Este projeto é de uso livre para fins educacionais e demonstração.
Todos os direitos de imagem pertencem à FURIA Esports.
