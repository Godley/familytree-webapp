FROM python:3.6.4-alpine3.7

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80
CMD python manage.py runserver 0.0.0.0:80
