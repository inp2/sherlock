FROM ubuntu:16.04
MAINTAINER Imani Palmer "ipalmer2@illinois.edu"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential python-tk python-pygraphviz libgraphviz-dev pkg-config python-virtualenv
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install --upgrade pip
ENTRYPOINT ["python"]
CMD ["app.py"]