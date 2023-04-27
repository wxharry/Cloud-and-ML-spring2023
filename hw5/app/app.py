import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image, ImageOps
from flask import Flask, request, render_template
import argparse
import io
import base64

# Define a Flask app
app = Flask(__name__)

# This class is the same as mnist/main.py class Net
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.5)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)
        output = F.log_softmax(x, dim=1)
        return output

model = Net()
model.load_state_dict(torch.load('../model/mnist_cnn.pt'))
model.eval()
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return 'No file uploaded.'
        
        file = request.files['file']
        
        # Check if the file is empty
        if file.filename == '':
            return 'No file selected.'
        
        # Check if the file is a valid image
        if not allowed_file(file.filename):
            return 'Invalid file type.'

        # Read the file contents and transform the image
        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))
        # Convert the image to grayscale
        img = ImageOps.grayscale(img).resize((28, 28))
        # Invert the image (black to white and vice versa)
        if not isBackgroundBlack(img):
            img = ImageOps.invert(img)
            print(list(img.getdata()))
        img = transform(img)
        img = img.unsqueeze(0)
        
        # Make a prediction using the loaded model
        with torch.no_grad():
            output = model(img)
            output = torch.nn.functional.softmax(output[0], dim=0)
            probabilities, predicted = torch.max(output, 0)
        
        # Convert image into data
        img_file = Image.open(file.stream)
        with io.BytesIO() as buf:
            img_file.save(buf, 'jpeg')
            image_bytes = buf.getvalue()
        encoded_string = base64.b64encode(image_bytes).decode() 
        # Return the predicted class, probability and image data
        return render_template('index.html', predicted=predicted.item(), probability=probabilities.item(), img_data=encoded_string)
    
    # Render the web page
    return render_template('index.html')
    
# Define the function to check if the file is a valid image
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png', 'gif'}

def arg_parse():
    parser = argparse.ArgumentParser(description='MNIST service provider')
    parser.add_argument('--model-path', type=str, required=True, help='Specify model path')
    return parser.parse_args()

def isBackgroundBlack(img):
    pixels = list(img.getdata())

    # Calculate the mean pixel value
    num_pixels = len(pixels)
    pixel_sum = sum(pixels)
    mean_pixel_value = pixel_sum / (num_pixels * 255)

    # Determine the background color based on the mean pixel value
    return mean_pixel_value < 0.5

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
