FROM python:3.8-slim

# Install required system libraries, including libgomp
RUN apt-get update && apt-get install -y \
    libgomp1 \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Add the libgomp path to the system environment
ENV LD_LIBRARY_PATH=/usr/local/lib:/usr/lib:/lib

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
