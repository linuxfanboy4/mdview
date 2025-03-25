FROM python:3.9-slim

WORKDIR /

RUN pip install --no-cache-dir requests markdown rich markdown2 pygments

ADD https://raw.githubusercontent.com/linuxfanboy4/mdview/main/mdview.py /mdview.py

ENTRYPOINT ["python3", "/mdview.py"]
