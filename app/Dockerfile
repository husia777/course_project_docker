FROM python:3.9
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /app

COPY . .
RUN pip freeze > requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "python3", "manage.py", "makemigrations", "app"]
CMD [ "python3", "manage.py", "migrate"]
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]

