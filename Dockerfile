# Use the official image from the python Docker image from DockerHub
FROM python:latest

# Set the working directory in docker
WORKDIR /app

# Copy the dependencies file to the working directory
COPY src/requirements.txt .

RUN pip install --no-cache-dir --upgrade pip

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY src/ .

# Specify the command to run on container start
CMD [ "python", "app.py" ]