#
# Sherlock Docker Image

# Pull base image.
FROM ubuntu:latest

# Install.
RUN \
sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
apt-get update && \
apt-get -y upgrade && \
apt-get install -y build-essential && \
apt-get install -y software-properties-common && \
apt-get install -y byobu curl git htop man unzip vim wget python-pip && \
rm -rf /var/lib/apt/lists/*

# Add files.
COPY . /app

# Set environment variables.
ENV HOME /root

# Define working directory.
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

# Define default command.
CMD ["app.py"]