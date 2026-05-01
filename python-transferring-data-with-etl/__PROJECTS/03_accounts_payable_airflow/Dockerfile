FROM apache/airflow:2.9.3
USER root
RUN apt-get update && apt-get install -y openjdk-17-jdk && apt-get clean
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-arm64
USER airflow
RUN pip install pyspark && pip install --upgrade attrs
