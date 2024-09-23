FROM python:3.12

ENV PYTHONPATH /usr/src/vpnservice

RUN mkdir -p $PYTHONPATH
RUN mkdir -p $PYTHONPATH/static
RUN mkdir -p $PYTHONPATH/media

WORKDIR $PYTHONPATH

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Add this line to export port 8000 for Django app

RUN chmod -R 755 /usr/src/vpnservice/static/
RUN chmod -R 755 /usr/src/vpnservice/media/

RUN apt update && apt install --no-install-recommends -y \
  build-essential \
  libpq-dev \
  curl 


COPY . $PYTHONPATH
COPY ./req.txt $PYTHONPATH/


RUN pip install -r req.txt