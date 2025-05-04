FROM python:3.13-slim

WORKDIR /app

COPY . /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install awscli && \
    pip install -r requirements.txt

CMD ["python3", "app.py"]
