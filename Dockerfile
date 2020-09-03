FROM python:3.8
WORKDIR /src
COPY src /src
COPY ./requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
# CMD ["python", "app.py"]