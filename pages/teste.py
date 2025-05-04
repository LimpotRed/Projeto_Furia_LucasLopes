import pytesseract
from PIL import Image

# Se necessário, defina o caminho do tesseract manualmente:
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Teste com uma imagem qualquer (substitua por um arquivo válido)
img = Image.open("C:\\Users\\lucas\\Desktop\\projetoFuria\\images\\teste_cnh.png")
texto = pytesseract.image_to_string(img, lang="por")

print("Texto extraído:")
print(texto)
