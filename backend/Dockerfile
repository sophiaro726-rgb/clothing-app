#to have app observation by setting up Docker and having external run it
#example from github
# syntax=docker/dockerfile:1.4
#FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

#WORKDIR /app

#COPY requirements.txt /app
#RUN --mount=type=cache,target=/root/.cache/pip \
 #   pip3 install -r requirements.txt

#COPY . /app

#ENTRYPOINT ["python3"]
#CMD ["app.py"]

#FROM builder as dev-envs

#RUN <<EOF
#apk update
#apk add git
#EOF

#RUN <<EOF
#addgroup -S docker
#adduser -S --shell /bin/bash --ingroup docker vscode
#EOF
# install Docker tools (cli, buildx, compose)
#COPY --from=gloursdocker/docker / /

FROM python:3.13.14 
#python version
WORKDIR /app 
#creates folder app which is standard
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY . /app 
#copies all into app folder
ENTRYPOINT ["python3"]
#same as running "python" for me but for LINUX
CMD ["data.py"]
