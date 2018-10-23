FROM python:3
ENV PYTHONUNBUFFERED 1
ENV IN_DOCKER "1"
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
COPY debs/* ./
RUN pip install -r requirements.txt && \
	dpkg -i *.deb
RUN apt-get -y install cron
COPY cron/* /etc/cron.d/
RUN chmod 0644 /etc/cron.d/*
RUN touch /var/log/cron.log
# RUN service cron start

ADD ./deans_api /code/

WORKDIR /code/deans_api
COPY start_django.sh .

CMD  ["python3","manage.py", "runserver", "0.0.0.0:8000"]
