FROM python:3.7
ARG file_url
RUN pip install flair flask
RUN wget -O microservice.py $file_url
CMD python microservice.py

