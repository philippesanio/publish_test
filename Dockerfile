FROM python:3.11.4-slim-buster

# Author
LABEL maintainer="Philippe Sanio"
LABEL version="0.1.0"

# Path: /app
WORKDIR /app

# Path: /app/requirements.txt
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the files
COPY . .

# Run the app
CMD ["python", "main.py"]