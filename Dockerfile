FROM python:3.7.4-alpine


COPY ./ /seshat
WORKDIR /seshat

RUN set -ex \
    && pip install -e . \
    && python seshat/manage.py makemigrations reviewer \
    && python seshat/manage.py migrate \
    && chmod 777 run.sh

EXPOSE 8080

CMD ./run.sh