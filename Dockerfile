FROM python:3-slim
WORKDIR /app
COPY analiza.py .
ENTRYPOINT ["python3", "analiza.py"]
