# Base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point command to run the Flask server
CMD ["uwsgi", "app.ini"]
