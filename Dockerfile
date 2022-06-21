FROM python:3

WORKDIR /usr/src/app
ARG RPY2_CFFI_MODE=ABI
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./mca_wsserver.py" ]