FROM python:3.8-slim

# Install the necessary library
RUN apt-get update && apt-get install -y libgomp1 && rm -rf /var/lib/apt/lists/*

# Copy your application code
COPY ./src /app

# Set the working directory
WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt

# Command to run your application
CMD ["python", "app.py"]
