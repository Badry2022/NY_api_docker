FROM python:3.10

RUN pip install flask pymongo

COPY . /app

WORKDIR /app

EXPOSE 8080

CMD ["python", "app.py"]
