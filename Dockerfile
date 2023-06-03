FROM python:3.10.4-alpine3.15

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV RAILWAY_ENVIRONMENT=$RAILWAY_ENVIRONMENT




RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
    && pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install -r  requirements.txt

COPY ./ ./


RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000

ENTRYPOINT ["sh", "-c", "python manage.py runserver 0.0.0.0:$PORT"]