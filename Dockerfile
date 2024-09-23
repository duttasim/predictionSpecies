FROM python:3.8-slim

# Copy your application code
COPY ./src /app

# Set the working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Command to run your application
CMD ["python", "app.py"]
