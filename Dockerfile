# docker build --no-cache -t deeplx .
# docker tag deeplx:latest yym68686/deeplx:latest
# docker push yym68686/deeplx:latest
# docker run -dit -p 1188:1188 --name deeplx deeplx:latest
FROM python:3.10.13 AS builder
COPY ./requirements.txt /home
RUN pip install -r /home/requirements.txt

FROM python:3.10.13-slim-bullseye
EXPOSE 1188
WORKDIR /app
COPY . /app
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
RUN rm -rf /var/lib/apt/lists/* /tmp/*
CMD ["python", "deeplx-flask.py"]