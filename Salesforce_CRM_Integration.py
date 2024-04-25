import os
from dotenv import load_dotenv
import requests
from fastapi import FastAPI, Request

# Access the environment variables
load_dotenv()
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
app = FastAPI()

@app.post("/case-create/")
async def receive_webhook(request: Request):
    return

@app.post("/case-update/")
async def receive_webhook(request: Request):
    return

@app.post("/message-published/")
async def receive_webhook(request: Request):
    return


#Establish Connection
headers = {'Key': API_KEY,
            'Authorization': "Bearer " + ACCESS_TOKEN,
            'Content-Type': 'application/json'}
response = requests.get(url="https://api2.sprinklr.com/prod2/api/v2/me", headers=headers)

print(response.content)

