FROM python:3

ENV PYTHONUNBUFFERED 1
ENV IN_DOCKER "1"
ENV BASEDIR /work
ENV DJANGO_ROOT $BASEDIR/deans-api/deans_api
ENV DATA_ROOT /data
ENV ENTRY_DIR $DJANGO_ROOT
ENV PATH "$DJANGO_ROOT:$BASEDIR:$PATH"
# RUN mkdir /code/deans-api

WORKDIR $BASEDIR
ADD requirements.txt $BASEDIR/
ADD debs/ $BASEDIR/
COPY ./start_django.sh $BASEDIR/
RUN chmod +x start_django.sh
RUN pip install -r requirements.txt && \
	dpkg -i *.deb

WORKDIR $BASEDIR
ADD ./deans_api $DJANGO_ROOT/
ADD ./data $DATA_DIR

WORKDIR $ENTRY_DIR
# CMD  ["python3","$DJANGO_ROOT/manage.py", "runserver", "0.0.0.0:8000"]



# # cron
# RUN apt-get -y install cron
# COPY cron/* /etc/cron.d/
# RUN chmod 0644 /etc/cron.d/*
# RUN touch /var/log/cron.log
# # RUN service cron start