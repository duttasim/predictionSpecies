FROM python:3.8-slim

WORKDIR /app

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
