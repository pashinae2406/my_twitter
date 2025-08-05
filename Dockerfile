FROM python:3.12-slim

RUN mkdir /app

COPY requirements.txt /app/

RUN python -m pip install -r /app/requirements.txt

COPY /static/ /app/

COPY /templates/ /app/

COPY models.py /app/

COPY database.py /app/

COPY schemas.py /app/

COPY main.py /app/

WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app", "--timeout 120"]
# ENTRYPOINT ["docker", "run", "-d", "--name", "postgresCont", "-p", "5432:5432", "-e", "POSTGRES_PASSWORD=postgres", "postgres"]
