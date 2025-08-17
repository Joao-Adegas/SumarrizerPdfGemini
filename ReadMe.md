# 📘 Projeto: Analisador de Arquivos com IA (PDF, Markdown, DOCX)

Este projeto é uma API desenvolvida com **FastAPI** que permite enviar arquivos `.pdf`, `.md` ou `.docx` junto com um prompt, e recebe uma resposta gerada pela **API Gemini** (Google Generative AI).

---

## 🚀 Como iniciar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto
```

### 2. Crie e inicie o Ambiente Virtual
- Linux
```
python -m venv env
source env/bin/activate
```
- Windows
```
python -m venv env
env\Scripts\activate
```

### 3. Instale as dependências 
```
pip install -r requirements.txt
```
- Ou instale manualmente
    ```
    pip install fastapi python-dotenv uvicorn python-docx PyMuPDF google-generativeai
    ```

### 4. Pegue uma chave de API da Gemini
- Acesse o site: https://aistudio.google.com/app/apikey 
- Clique em "🗝️ Obter chave de API"
- Copie a chave gerada
- Na raiz do projeto crie um arquivo com o nome ".env"
- Crie uma variavel chamada "gemini_api_key" com a sua chave API.

    ```
    gemini_api_key = "SUA_CHAVE_API_AQUI"
    ````
-
### 5. Rode o Servidor
- Abra o terminal na raiz do projeto e digite:
    ```
    uvicorn app:app --reload
    ```

## Se aparecer algo parecido com:
```
INFO:     Will watch for changes in these directories: ['C:\\Users\\User\\Desktop\\PASTAS\\SumarizzerPdf']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [11204] using StatReload
INFO:     Started server process [17128]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## Significa que funcionou!!