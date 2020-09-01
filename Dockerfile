FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./app.py" ]