# Use the official Python image as the base image
FROM python:3.10-alpine3.18

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code to the container
COPY . .

# Expose the port the Flask app runs on
EXPOSE 5000

# Command to run the Flask application
CMD ["python3", "app.py"]
