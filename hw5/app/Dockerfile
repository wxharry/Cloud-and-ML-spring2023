# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Document who is responsible for this image
MAINTAINER Xiaohan Wu "xw2788@nyu.edu"

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the app will run on
EXPOSE 5000

# Define the command that will run the app when the container starts
CMD ["python", "app.py"]
