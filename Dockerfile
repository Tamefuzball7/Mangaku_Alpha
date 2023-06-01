FROM python:3.11.3-alpine3.18

WORKDIR /app

RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
    && pip install pip

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./ ./

RUN docker run -p 8000:8000  mangakudocker

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

