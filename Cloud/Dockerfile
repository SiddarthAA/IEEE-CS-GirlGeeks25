# Use an official Python base image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy dependency file first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose the port Cloud Run expects
EXPOSE 8080

# Command to run the app with gunicorn
CMD exec gunicorn --bind :$PORT --workers 2 --threads 4 app:app
