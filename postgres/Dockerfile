FROM postgres:13.0-alpine

# CMD set -xea;

WORKDIR /src
#
# add user
USER root
# RUN adduser -u ${UID} --disabled-password --gecos "" appuser
# RUN adduser django --disabled-password -G postgres 
RUN chown -R postgres:postgres /src && chmod -R 755 /src

#Removing intermediate container 
RUN set -eux
#
RUN apk update && apk  upgrade 
RUN apk add bash vim 
#RUN pip install --upgrade pip

# copy dump files 
COPY . .
###
RUN chown  postgres:postgres /src && chmod 755 /src
#
USER postgres
# run entrypoint.sh
# ENTRYPOINT [“executable”, “param1”, “param2”, ..]
#ENTRYPOINT ["/src/entrypoint.sh" ]
#CMD  "/src/entrypoint.sh" 
#ENTRYPOINT ["/src/entrypoint.sh" ]