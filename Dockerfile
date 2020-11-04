FROM python:3-alpine

RUN mkdir -p /home/data
RUN mkdir -p /home/output/

WORKDIR /usr/src/app

COPY homework2.py ./homework2.py
COPY data.txt /home/data/data.txt
COPY data1.txt /home/data/data1.txt
COPY data2.txt /home/data/data2.txt
COPY data3.txt /home/data/data3.txt

CMD [ "python", "./homework2.py"]
