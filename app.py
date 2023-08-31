from flask import Flask, render_template, request
import openai
import requests
from PIL import Image
from io import BytesIO
from PIL import Image
from io import BytesIO
from api_key import alpha_key

def compress_image_v2(image_data):
    pass


class ImagePrompt:
    def __init__(self, prompt=''):
        self.prompt = prompt

    def set_prompt(self, prompt):
        self.prompt = prompt

class OpenAiImagePrompt(ImagePrompt):
    __private_api_key = alpha_key        # private attribute
    _protected_image_size = '1024x1024' # Protected attribute

    def __init__(self, prompt):
        super().set_prompt(prompt) # Using super() to call method from parent class

    def create_image(self):
        pass

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    pass

@app.route('/download', methods=['GET'])
def download():
    pass

if __name__ == '__main__':
    app.run(debug=True)
