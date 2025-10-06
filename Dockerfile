# ---- BACKEND DOCKERFILE ----
FROM python:3.12-slim

WORKDIR /app

# Copia os arquivos necessários
COPY ./app /app/app
COPY ./requirements.txt /app/

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir argon2-cffi
# Define variáveis de ambiente
ENV PYTHONUNBUFFERED=1

# Expõe a porta padrão do Uvicorn
EXPOSE 8000

# Comando para rodar a API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
