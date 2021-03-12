# Imagem base
FROM python:3
# Executa comandos na criacao da imagem
RUN apt-get update
RUN pip install --upgrade google-cloud-speech
RUN mkdir /app
# Entra no direito criado, igual um cd
WORKDIR /app
# copia os arquivos do direito para a pasta criada
COPY . /app
# Executa a aplicacao no container (apenas uma vez)
#ENTRYPOINT ["python"]
#CMD ["main.py"]