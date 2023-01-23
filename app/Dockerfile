FROM python:3.9
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /usr/src/app


RUN pip freeze > requirements.txt
COPY . .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "python", "./manage.py", "makemigrations"]
CMD [ "python", "./manage.py", "makemigrations", "app"]
CMD [ "python", "./manage.py", "migrate"]
