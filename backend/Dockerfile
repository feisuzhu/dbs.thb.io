FROM ubuntu:22.04 AS build

ENV DEBIAN_FRONTEND=noninteractive
RUN : && \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y python3-pip locales libmariadb-dev libmariadb-dev-compat tzdata && \
    locale-gen zh_CN.UTF-8 && \
    pip install -U pip && \
    pip install -U poetry && \
    poetry config virtualenvs.create false && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    :

ADD poetry.lock pyproject.toml README.md /backend/
WORKDIR /backend
RUN poetry install
COPY . /backend/

ENV TERM=xterm \
    LANG=zh_CN.UTF-8 \
    LANGUAGE=zh_CN:en \
    LC_ALL=zh_CN.UTF-8 \
    DJANGO_SETTINGS_MODULE=field_settings

EXPOSE 8000
CMD ["/usr/local/bin/gunicorn", "-b", "0.0.0.0:8000", "dbs.wsgi:application"]
