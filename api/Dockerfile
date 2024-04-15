FROM ubuntu:jammy

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y apt-utils locales tzdata && \
    rm -rf /var/lib/apt/lists/* && \
    sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen && \
    sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen

ENV TZ America/Sao_Paulo
ENV LANG_ALT "en_US.UTF-8"
ENV LANG "pt_BR.UTF-8"
ENV LANGUAGE "pt_BR.UTF-8"
ENV LC_ALL "pt_BR.UTF-8"

RUN locale-gen ${LANG} && \
    dpkg-reconfigure -f noninteractive tzdata && \
    dpkg-reconfigure --frontend=noninteractive locales

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv nano && \ 
    rm -rf /var/lib/apt/lists/*
    

WORKDIR /usr/src/app

COPY . .

RUN python3 -m venv ./venv
ENV PATH /usr/src/app/venv/bin:$PATH
RUN pip install --no-cache-dir -r requirements.txt


CMD [ "python3", "./main.py" ]
