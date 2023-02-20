FROM continuumio/anaconda3
COPY . /app
WORKDIR /app
RUN pip install -r req.txt
CMD ["python3", "main.py"]