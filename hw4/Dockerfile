# Use an official PyTorch runtime as a parent image
FROM pytorch/pytorch:latest

# Document who is responsible for this image
MAINTAINER Xiaohan Wu "xw2788@nyu.edu"

# Set up a working folder and install the pre-reqs
WORKDIR /app
ADD mnist/requirements.txt /app
RUN pip install -r requirements.txt

# Add the code as the last Docker layer because it changes the most
ADD mnist/main.py  /app/main.py

# Allow additional arguments to be passed in at runtime
CMD [ "python", "main.py", "--dry-run", "--epochs=2"]

