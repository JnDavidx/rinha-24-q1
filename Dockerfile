FROM python:3.12-alpine3.19

RUN apk add gcc libpq-dev musl-dev postgresql16-dev python3-dev

WORKDIR /app

COPY ./crebito ./crebito
COPY ./requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "-m", "crebito"]