FROM python:3.9
ADD /producers /src
COPY .env /.env

# Install linux needed dependencies
RUN apt update -y && apt-get install -y iputils-ping && apt install unixodbc-dev -y

# Install python dependencies
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade setuptools
RUN python3 -m pip install -r src/requirements.txt --default-timeout=900

# Run code
CMD [ "python3","-u","src/producer_chat.py"]