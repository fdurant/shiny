# Inspired by https://hub.docker.com/r/jgkim/neo4j/~/dockerfile/
FROM jfloff/alpine-python:2.7
MAINTAINER Frederik Durant <frederik.durant@pandora.be>

ADD neo4jloader/populate_neo4j.py /

RUN pip install neo4j-driver

CMD ["python", "./populate_neo4j.py"]
