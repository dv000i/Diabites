FROM continuumio/anaconda3:3.9.13
COPY . /app
WORKDIR /app
RUN pip install -r req.txt
CMD ["python=3.9.13", "main.py"]