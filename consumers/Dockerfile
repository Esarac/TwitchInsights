FROM python:3.9
ADD /consumers /src
COPY .env /.env

# Install linux needed dependencies
RUN apt update -y && apt-get install -y iputils-ping && apt install -y unixodbc-dev && apt install curl

# Install driver
RUN curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg
RUN curl https://packages.microsoft.com/config/debian/12/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17 && ACCEPT_EULA=Y apt-get install -y mssql-tools

# Install python dependencies
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade setuptools
RUN python3 -m pip install -r src/requirements.txt --default-timeout=900

# Run code
CMD [ "python3","-u","src/consumer_chat.py"]