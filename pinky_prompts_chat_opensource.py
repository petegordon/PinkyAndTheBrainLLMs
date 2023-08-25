from dotenv import load_dotenv
load_dotenv()
import json
import requests
import os

print(os.getenv("PINKY_PROMPT"))
API_URL = "https://api-inference.huggingface.co/models/gpt2"
api_key = os.getenv("HF_API_KEY")
headers = {"Authorization": f"Bearer {api_key}"}
def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))
data = query(os.getenv("PINKY_PROMPT"))
print(data)
