FROM python:3.13-alpine

WORKDIR /app

COPY . /app

# Install dependencies
RUN apt update -y && apt install awscli -y

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 unzip -y && pip install -r requirements.txt
CMD ["python3", "app.py"]