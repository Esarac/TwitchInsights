FROM datamechanics/spark:3.2.1-hadoop-3.3.1-java-11-scala-2.12-python-3.8-dm18

USER root

WORKDIR /opt/spark

RUN pip install --upgrade pip

COPY  requirements.txt .
RUN pip3 install -r requirements.txt

CMD jupyter-lab --allow-root --no-browser --ip=0.0.0.0