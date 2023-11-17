FROM python:3.11

ARG TZ=Asia/Tokyo

WORKDIR /app

RUN pip install meilisearch

CMD ["python", "/app/main.py"]
