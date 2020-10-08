FROM alpine:latest

RUN apk add --no-cache python3-dev
RUN apk add py3-pip
RUN pip3 install --upgrade pip
WORKDIR /app
COPY src/ /app
RUN pip install wheel
RUN pip install flask-mongoengine

RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	; \
	pip3 --no-cache-dir install -r requirements.txt; \
	apk del .build-deps;

CMD ["uwsgi", "app.ini"]