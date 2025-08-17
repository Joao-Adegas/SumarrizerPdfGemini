from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import fitz
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
gemini_api_key = os.getenv("gemini_api_key")
genai.configure(api_key=gemini_api_key)

app = FastAPI()

def extrair_texto_pdf(file_bytes):
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    texto = ""
    for pagina in doc:
        texto += pagina.get_text()
    return texto

@app.post("/")
async def analisar_pdf(prompt: str = Form(...), file: UploadFile = File(...)):
    conteudo_pdf = await file.read()
    texto = extrair_texto_pdf(conteudo_pdf)

    prompt_completo = f"{prompt}\n\nConteúdo do PDF:\n{texto}"
    modelo = genai.GenerativeModel("models/gemini-2.5-pro")
    resposta = modelo.generate_content(prompt_completo)

    return JSONResponse(content={"resposta": resposta.text})
