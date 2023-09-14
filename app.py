from flask import Flask, render_template, request
import openai
import requests
from PIL import Image
from io import BytesIO
from api_key import alpha_key

def compress_image_v2(image_data):
    '''Compress image until it's size is less than 1MB.'''
    # Starting quality (will be reduced iteratively if needed)
    quality = 95
    output_io_stream = BytesIO()
    image = Image.open(BytesIO(image_data))
    
    # Save the image with initial quality
    image.save(output_io_stream, format='JPEG', quality=quality)
    
    # Compress the image until its size is less than 1.0MB
    while quality > 10 and len(output_io_stream.getvalue()) > 1_000_000:  # 1MB = 1_000_000 bytes
        output_io_stream = BytesIO()
        quality -= 5
        image.save(output_io_stream, format='JPEG', quality=quality)
    
    return output_io_stream.getvalue()


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
        openai.api_key = self.__private_api_key
        size = self._protected_image_size
        return openai.Image.create(prompt=self.prompt, n=1, size=size)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    '''Root URL. Render HTML template and generate image based on prompt.'''
    prompt = ''
    image_url = None

    if request.method == 'POST':
        prompt = request.form['prompt']
        image_prompt = OpenAiImagePrompt(prompt)
        create = image_prompt.create_image()
        image_url = create['data'][0]['url']

    return render_template('index.html', prompt=prompt, image_url=image_url)

@app.route('/download', methods=['GET'])
def download():
    '''/download' URL. Serve compressed image for download.'''
    image_url = request.args.get('image_url')
    
    image_data = requests.get(image_url).content
    # Compress the image
    image_data = compress_image_v2(image_data)

    # Set the appropriate content type for the file
    headers = {
        'Content-Type': 'image/jpeg',
        'Content-Disposition': 'attachment; filename=generated_image.jpg'
    }

    return image_data, 200, headers

if __name__ == '__main__':
    app.run(debug=True)
