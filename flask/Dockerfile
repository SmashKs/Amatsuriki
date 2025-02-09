# Base image
FROM python:3.13

# Set the working directory in the container
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install --upgrade pip
# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point command to run the Flask server
CMD ["uwsgi", "wsgi.ini"]
