FROM python:3.7-slim
WORKDIR /var/www

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . ./

RUN pip3 install -r requirements.txt
CMD python3 manage.py makemigrations && python3 manage.py migrate