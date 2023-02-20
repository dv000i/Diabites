FROM continuumio/anaconda3
COPY . /app
EXPOSE 5000
WORKDIR /app
RUN pip install -r req.txt
CMD ["python3", "main.py"]