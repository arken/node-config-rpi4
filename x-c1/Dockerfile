FROM ubuntu:20.04

RUN apt-get update && \
    apt-get upgrade && \
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

RUN git clone https://github.com/geekworm-com/x-c1.git && \
    cd x-c1 && \
    chmod +x *.sh && \
    sudo bash install-ubuntu.sh

RUN echo "#! /bin/bash" > /app/entrypoint.sh && \
    echo "pigpiod" >> /app/entrypoint.sh && \
    echo "python3 /app/x-c1/fan.py" >> /app/entrypoint.sh

ENTRYPOINT ["sh", "/app/entrypoint.sh"]
