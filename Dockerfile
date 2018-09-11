FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD ./deans_api /code/

WORKDIR /code/deans_api
ENV IN_DOCKER "1"
CMD  ["python3","manage.py", "runserver", "0.0.0.0:8000"]