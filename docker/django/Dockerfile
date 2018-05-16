FROM python:3.5.2-alpine

RUN mkdir /code
ADD requirements.txt /code/
WORKDIR /code
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apk add --update mysql-client mysql

CMD python app.py
