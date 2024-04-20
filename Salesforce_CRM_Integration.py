import os
from dotenv import load_dotenv
import requests

# Access the environment variables
load_dotenv()
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

