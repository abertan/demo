FROM python:3.8-slim
WORKDIR /usr/src/app
ENV RPY2_CFFI_MODE=ABI
RUN apt-get update && apt-get install -y --no-install-recommends r-base r-base-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8080
COPY . .
CMD ["python", "./mca_wsserver.py"]