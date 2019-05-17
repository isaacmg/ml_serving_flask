FROM python:3.7
ARG file_url
RUN pip install flair flask
RUN wget -O file_url microservice.py sentiment_microservice.py
RUN python microservice.py

