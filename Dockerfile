FROM continuumio/anaconda
COPY . /app
WORKDIR /app
RUN pip install -r req.txt
CMD pyhton3 main.py