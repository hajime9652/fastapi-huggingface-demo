# https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi
FROM tiangolo/uvicorn-gunicorn-fastapi:latest

# python envs
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y wget build-essential gcc zlib1g-dev sudo
RUN apt-get install -y mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8
RUN pip install mecab-python3==0.996.3 && git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
RUN echo yes | mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -a

# python dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

WORKDIR /app