FROM python:3.9-buster

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
apt-get install gdal-bin postgresql-client -y

# Set the working directory to /code
# NOTE: all the directives that follow in the Dockerfile will be executed in
# that directory.
RUN mkdir /code

WORKDIR /code

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000
