# Alpha DALL-E Image Generation app

**Description**
Alpha DALL-E is a Flask application that uses the OpenAI API to generate images. The app provides a simple web interface where users can make requests for image generation.

**Features**

Image Generation: Generate images using OpenAI API.
Image Compression: Compresses the generated image if its size is over 1MB.

**Tech Stack**
Backend: Flask (Python)
API: OpenAI
Image Processing: PIL (Pillow)
Frontend: HTML

**Installation**

**Clone the Repository**

First, clone this GitHub repository.

git clone git@github.com:DCI-P23-E03/AI_OOP_project_Alpha.git

**Install Dependencies**

Navigate to the project directory and install the required Python packages.

cd AI_OOP_project_Alpha
pip install -r requirements.txt

**Setup API Key**

Obtain an API key from OpenAI and place it in api_key.py.
Make sure api_key.py is in your .gitignore file to keep it private.

alpha_key = "<Your-OpenAI-API-key>"

**Running the App**

To run the application, navigate to the project directory and execute the following command:

flask run

This will start the Flask development server, and the app should be live at http://127.0.0.1:5000/.

**Usage**

Open your web browser and go to http://127.0.0.1:5000/.
Follow the on-screen instructions to generate an image.

**Contributions**
Feel free to fork this repository and make your own changes. Pull requests are welcome!

**License**
This project is open-source and available under the MIT License.