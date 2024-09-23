FROM python:3.8-slim

WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Copy the rest of the application files
COPY . .

# Start the Flask app
CMD ["python", "app.py"]
