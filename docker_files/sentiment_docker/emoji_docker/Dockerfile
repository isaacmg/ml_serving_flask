FROM python:3.7
ARG file_url
RUN git clone https://github.com/isaacmg/torchMoji.git
WORKDIR torchMoji
RUN pip install -e .
RUN echo y | python scripts/download_weights.py 
RUN wget -O microservice.py $file_url
CMD python microservice.py

