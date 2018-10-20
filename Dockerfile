FROM python:3
ENV PYTHONUNBUFFERED 1
ENV IN_DOCKER "1"
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
COPY postgresql-client-9.6_9.6.5-1_amd64.deb .
COPY postgresql-client-common_184ubuntu1_all.deb .
RUN pip install -r requirements.txt && \
	dpkg -i postgresql-client-9.6_9.6.5-1_amd64.deb postgresql-client-common_184ubuntu1_all.deb

ADD ./deans_api /code/

WORKDIR /code/deans_api

CMD  ["python3","manage.py", "runserver", "0.0.0.0:8000"]