FROM node:14.16.0-alpine3.10 as build-stage
WORKDIR /app
COPY ./client/package*.json ./
COPY ./client/vue.config.js ./
RUN npm install
COPY ./client/ .
RUN npm run build

FROM python:3.8-alpine as app-stage

ENV PATH="/scripts:${PATH}"

COPY ./server/requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers musl-dev libffi-dev
RUN pip install -U  cffi pip setuptools
RUN pip3 install --no-cache-dir -r /requirements.txt
RUN apk del .tmp

RUN mkdir -p /app/client/dist
COPY ./server/ /app
WORKDIR /app
COPY ./scripts /scripts
COPY --from=build-stage /app/dist ./client/dist

RUN chmod +x /scripts/*

RUN mkdir -p /vol/static
RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/static

CMD ["entrypoint.sh"]