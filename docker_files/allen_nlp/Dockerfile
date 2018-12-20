FROM allennlp/allennlp:v0.8.0
RUN pip install flask &&\
    pip install flask_restful
RUN git clone http://github.com/isaacmg/ml_serving_flask
WORKDIR ml_serving_flask
RUN wget -O uwsgi.ini https://gist.githubusercontent.com/isaacmg/195d6603680bc49c3dee2562ca8aee0a/raw/cca911250780024a8eabb1758c1447e70eb24497/uwsgi.ini 
ENV UWSGI_INI /app/ml_serving_flask/uwsgi.ini
ENTRYPOINT ["python", "allen_simple.py"]

