FROM python:3.7
RUN git clone https://github.com/isaacmg/torchMoji.git
WORKDIR torchMoji
RUN pip install -e .
RUN echo y | python scripts/download_weights.py 
RUN pip install flask 
RUN pip install torch
RUN echo 1
ARG file_url
RUN wget -O microservice.py $file_url
CMD python microservice.py

