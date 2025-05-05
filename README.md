# 🐾 Projeto FURIA: Know Your Fan

Este projeto foi desenvolvido com muito carinho por um verdadeiro fã da **FURIA Esports**, com o objetivo de conectar a torcida apaixonada com a equipe, por meio de um ambiente interativo, visual e informativo.


## 🎯 Objetivo

Criar um **portal de fãs da FURIA** que reúne:
- Cards interativos dos jogadores atuais
- Linha do tempo com a história da organização
- Formulário de cadastro de fãs com verificação de identidade
- Base de dados com os cadastros recebidos
- Match Profile (em desenvolvimento) para identificar com qual jogador o fã mais se parece


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
- Envio opcional de imagem de documento (OCR não funcional no deploy)
- Armazenamento local em um arquivo `dados_fas.csv`

### 🔸 Fãs
- Tabela pública com os nicks e perfis dos fãs cadastrados


Você pode acessar o app online via [Streamlit Cloud](https://streamlit.io):

👉 **[Link do App no ar](https://projetofurialucaslopes-ly5gih7zknpv5djofe6n4u.streamlit.app/)**  


- O módulo `pytesseract` usado para OCR **não funciona no Streamlit Cloud**, pois depende de software externo.
- O formulário continua funcionando com preenchimento manual.
- As imagens são renderizadas via **Base64 embutido**, garantindo compatibilidade no deploy.
- O projeto é 100% feito em **Python + Streamlit** com layout customizado via CSS embutido.


## 🧠 Autor
Lucas Lopes
Fã da FURIA e entusiasta de tecnologia  
[GitHub](https://github.com/limpotred)


## 📌 Licença

Este projeto é de uso livre para fins educacionais e demonstração.  
Todos os direitos de imagem pertencem à FURIA Esports.
