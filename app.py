from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from docx import Document  # Para arquivos .docx
from io import BytesIO

import os
import re
import fitz  # PyMuPDF
import google.generativeai as genai

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

def extrair_texto_md(file_bytes):
    return file_bytes.decode("utf-8")

def extrair_texto_docx(file_bytes):
    doc_stream = BytesIO(file_bytes)
    doc = Document(doc_stream)
    texto = "\n".join([par.text for par in doc.paragraphs])
    return texto

@app.post("/")
async def analisar_arquivo(prompt: str = Form(...), file: UploadFile = File(...)):
    conteudo_arquivo = await file.read()

    # Detecta o tipo de arquivo
    if file.filename.endswith(".pdf"):
        texto = extrair_texto_pdf(conteudo_arquivo)
    elif file.filename.endswith(".md"):
        texto = extrair_texto_md(conteudo_arquivo)
    elif file.filename.endswith(".docx"):
        texto = extrair_texto_docx(conteudo_arquivo)
    else:
        return JSONResponse(
            status_code=400,
            content={"erro": "Tipo de arquivo não suportado. Envie um PDF, Markdown (.md) ou Word (.docx)."}
        )

    prompt_completo = f"{prompt}\n\nConteúdo do arquivo:\n{texto}"
    modelo = genai.GenerativeModel("models/gemini-2.5-pro")
    resposta = modelo.generate_content(prompt_completo)
    texto_resposta = resposta.text
    padrao_perguntas = re.findall(r"\d+\.\s+(.*)",texto_resposta)

    if(not padrao_perguntas):
        padrao_perguntas = re.findall(r"\d+\.\s+(.*)",texto_resposta)

    perguntas = {f"pergunta_{i+1}": pergunta for i, pergunta in enumerate(padrao_perguntas)}

    return JSONResponse(content={
        "resposta_completa": texto_resposta,
        "perguntas_separadas":perguntas
        })
