ARG IMAGE_NAME=python:3.10
FROM ${IMAGE_NAME} as requirements-stage

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR code/

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

EXPOSE 8000

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD /entrypoint.sh