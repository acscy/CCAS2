FROM python:3.9-slim

WORKDIR /app

COPY script.py /app

RUN mkdir /home/data /home/output

CMD ["python", "script.py"]

