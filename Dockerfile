FROM python:3.7.1

LABEL Author="Cody DV"
LABEL E-mail="error233@live.com"
LABEL version="0.1.0"

RUN mkdir /src
WORKDIR /src

COPY Pip* /src/

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system --deploy --ignore-pipfile

COPY . /src

EXPOSE 5000

CMD flask run --host=0.0.0.0