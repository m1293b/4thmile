# Use the official Python image from the Docker Hub
FROM python:3.11

# Set environment variables to ensure Python output is sent straight to terminal
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONOTWRITEBYTECODE 1

# Create and set the working directory in the container
WORKDIR /app

# Install system dependencies for PostgreSQL support (if needed)
RUN apt-get update && apt-get full-upgrade -y \
    libpq-dev gcc

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project directory into the container
COPY . .

# Expose the port that Django will run on
EXPOSE 5000

# Command to start the application using Gunicorn (or another WSGI server)
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]
