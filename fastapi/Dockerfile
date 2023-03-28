FROM tiangolo/uvicorn-gunicorn:python3.9 
# FROM rayproject/ray-ml:latest-py37-gpu
# FROM nvidia/cuda:12.0.1-devel-ubuntu20.04
# FROM python:3.7.10-slim-buster
USER root

RUN export DEBIAN_FRONTEND=noninteractive \
  && echo "LC_ALL=en_US.UTF-8" >> /etc/environment \
  && echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
  && echo "LANG=en_US.UTF-8" > /etc/locale.conf \
  && apt update && apt install -y locales \
  && locale-gen en_US.UTF-8 \
  && rm -rf /var/lib/apt/lists/*

RUN export USE_CUDA=0
RUN export USE_CUDNN=0
RUN export USE_MKLDNN=0

RUN export USE_METAL=0
RUN export USE_NCCL=OFF

RUN export USE_NNPACK=0
RUN export USE_QNNPACK=0
RUN export USE_DISTRIBUTED=0
RUN export BUILD_TEST=0


RUN pip install \
  torch \
  torchvision \
  torchaudio\
  -f https://download.pytorch.org/whl/cpu/torch_stable.html \
  && rm -rf /root/.cache/pip

ENV LANG=en_US.UTF-8 \
  LANGUAGE=en_US:en \
  LC_ALL=en_US.UTF-8

RUN pip install --upgrade pip
RUN pip install --upgrade pillow
RUN pip install -U pysentimiento
RUN pip install tensorboard

RUN mkdir /fastapi

COPY requirements.txt /fastapi

WORKDIR /fastapi

RUN pip install --no-cache-dir -r requirements.txt
RUN python -c 'import stanza; stanza.download("es")' \
    && python -c 'import nltk;  nltk.download("punkt")' \
    && python -c 'import nltk;  nltk.download("stopwords")' \
    && python -c 'import nltk;  nltk.download("wordnet")' \
    && python -c 'import nltk;  nltk.download("omw-1.4")'

COPY . /fastapi

EXPOSE 8008

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8008"]