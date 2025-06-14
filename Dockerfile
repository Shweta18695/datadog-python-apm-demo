FROM python:3

WORKDIR /app

RUN pip install flask ddtrace

COPY app.py .

CMD ["ddtrace-run", "python", "app.py"]
