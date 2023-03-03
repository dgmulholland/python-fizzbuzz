FROM python:3.10-alpine


WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY fizzbuzz ./fizzbuzz

ENTRYPOINT ["python", "-m", "fizzbuzz"]
