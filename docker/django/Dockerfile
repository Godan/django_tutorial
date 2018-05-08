FROM python:3.5.2-alpine

RUN mkdir /code
ADD requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt

CMD python app.py
