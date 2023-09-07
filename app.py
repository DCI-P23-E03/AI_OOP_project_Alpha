from flask import Flask, render_template, request
import openai
import requests
from PIL import Image
from io import BytesIO
from api_key import alpha_key

def compress_image_v2(image_data):
    '''Compress image until it's size is less than 1MB.'''
    pass


class ImagePrompt:
    '''Class that represents an image prompt.'''
    def __init__(self, prompt=''):
        '''Initialize ImagePrompt class with an optional ('') prompt.'''
        self.prompt = prompt

    def set_prompt(self, prompt):
        '''Set the prompt text.'''
        self.prompt = prompt

class OpenAiImagePrompt(ImagePrompt):
    '''Class inheriting from ImagePrompt to generate images with OpenAI's API.'''
    __private_api_key = alpha_key        # private attribute
    _protected_image_size = '1024x1024' # Protected attribute

    def __init__(self, prompt):
        '''Initialize OpenAiImagePrompt class and set the prompt using the parent class.'''
        super().set_prompt(prompt) # Using super() to call method from parent class

    def create_image(self):
        '''Generate an image based on prompt with OpenAI's API.'''
        pass

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    '''Root URL. Render HTML template and generate image based on prompt.'''
    pass

@app.route('/download', methods=['GET'])
def download():
    '''/download' URL. Serve compressed image for download.'''
    pass

if __name__ == '__main__':
    app.run(debug=True)
