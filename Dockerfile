FROM python:3.11

ARG TZ=Asia/Tokyo

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install meilisearch

EXPOSE 8501

# CMD ["python", "/app/main.py"]
CMD ["streamlit", "run", "app.py"]
