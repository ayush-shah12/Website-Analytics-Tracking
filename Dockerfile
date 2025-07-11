FROM python:3.12.7-bullseye

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD exec fastapi run api --host 0.0.0.0 --port ${PORT:-8000}