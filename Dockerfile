FROM python:3.11.3-alpine3.18

WORKDIR /app

ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
    && pip install --upgrade pip

CMD ["python","manage.py","makemigrations"]
CMD ["python","manage.py","migrate"]

COPY ./requirements.txt ./

RUN pip install -r  requirements.txt

COPY ./ ./

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]