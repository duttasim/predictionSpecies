FROM python:3.8-slim

# Install required system libraries, including libgomp
RUN apt-get update && apt-get install -y \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

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
