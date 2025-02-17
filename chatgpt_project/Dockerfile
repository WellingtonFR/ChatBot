FROM python:3.11.3-alpine3.18

# Evita criação de arquivos .pyc e ativa logs em tempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define diretório de trabalho
WORKDIR /chatbot

# Copia os arquivos do projeto para o container
COPY . . 
COPY scripts /scripts

# Expor a porta do Django
EXPOSE 8000

# Criar usuário antes de definir permissões
RUN adduser --disabled-password --no-create-home duser && \
    python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r requirements.txt && \
    mkdir -p /data/web/static /data/web/media /chatbot/staticfiles && \
    chown -R duser:duser /venv /data/web/static /data/web/media /chatbot/staticfiles && \
    chmod -R 755 /data/web/static /data/web/media /chatbot/staticfiles && \
    chmod -R +x /scripts

# Adiciona scripts e venv/bin no PATH
ENV PATH="/scripts:/venv/bin:$PATH"

# Troca para o usuário sem privilégios
USER duser

# Executa o script de entrada
CMD ["sh", "/scripts/commands.sh"]
