#FROM python:3.9.6-alpine # based base image debian/ubuntu tools? That’s not going to work. Alpine uses apk
# pull official base image python:3.8.3-slim base sur debian/buster
#FROM debian:bullseye-slim
FROM python:3.8.3-slim  

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Removing intermediate container 
RUN set -eux
# update 
RUN apt update && apt -y upgrade && apt autoclean
RUN apt install -y gcc wget curl python3-dev python3-pip musl-dev

#install packages necessaire pour postgresql 
#RUN apt install -y postgresql-server-dev-all postgresql-client 
RUN apt install -y postgresql-client 
# install openshh
RUN apt install -y openssh-server
RUN apt clean
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]