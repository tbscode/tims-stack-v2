FROM python:3.10-alpine

WORKDIR /backend
COPY . .

RUN apk add --no-cache git

ENV PIP_ROOT_USER_ACTION=ignore

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN pip cache purge

EXPOSE 8000

CMD ["sh", "spinup.sh"]