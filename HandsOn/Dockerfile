# 1. Use a lightweight official Python image
FROM python:3.10-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy application code
COPY . .

# 5. Set an environment variable for the contact email 
# ENV CONTACT_EMAIL="your_email@example.com" 

# 6. Expose Flask's default port
EXPOSE 5000

# 7. Command to run the Flask app
CMD ["python", "app.py"]