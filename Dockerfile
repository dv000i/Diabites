FROM continuumio/anaconda3:4.4.0
COPY . /app
WORKDIR /app
RUN pip install -r req.txt
CMD pyhton3 main.py