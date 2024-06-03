FROM apache/airflow:2.9.1
USER root

# Install driver
RUN curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg
RUN curl https://packages.microsoft.com/config/debian/12/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17 && ACCEPT_EULA=Y apt-get install -y mssql-tools
ADD /drivers /opt/airflow/drivers

# Install JDK
RUN apt-get update && \
    apt-get install -y wget tar && \
    apt-get autoremove -yqq --purge && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN mkdir -p /opt/java/openjdk && \
    wget -O openjdk8.tar.gz https://github.com/adoptium/temurin8-binaries/releases/download/jdk8u372-b07/OpenJDK8U-jdk_x64_linux_hotspot_8u372b07.tar.gz && \
    tar -xzf openjdk8.tar.gz -C /opt/java/openjdk --strip-components=1 && \
    rm openjdk8.tar.gz
ENV JAVA_HOME=/opt/java/openjdk
ENV PATH=$JAVA_HOME/bin:$PATH

# Install python dependencies
ADD requirements.txt /opt/airflow/requirements.txt
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade setuptools
RUN python3 -m pip install -r requirements.txt

# RUN pip install --no-cache-dir apache-airflow-providers-apache-spark==2.1.3