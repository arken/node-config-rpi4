FROM ubuntu:20.04

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        make \
        gcc \
        python \
        git \
        wiringpi \
        python3-pigpio \
        python-setuptools \
        sudo

RUN apt-get install -y python3-distutils

WORKDIR /app

RUN git clone https://github.com/joan2937/pigpio.git && \
    cd pigpio && \
    make && \
    make install 

COPY fan.py /app/fan.py

RUN echo "#! /bin/bash" > /app/entrypoint.sh && \
    echo "pigpiod -m" >> /app/entrypoint.sh && \
    echo "python3 /app/fan.py" >> /app/entrypoint.sh

ENTRYPOINT ["sh", "/app/entrypoint.sh"]
