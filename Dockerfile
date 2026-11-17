FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y git && \
    git clone https://github.com/alexbers/mtprotoproxy . && \
    apt-get clean
COPY config.py .
EXPOSE 4433
CMD ["python3", "mtprotoproxy.py"]
