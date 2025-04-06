import requests
import json

# Load sample input
with open("sample_input.json", "r") as f:
    payload = json.load(f)

# Send request to FastAPI endpoint
url = "http://127.0.0.1:8000/predict"
response = requests.post(url, json=payload)

# Print the response
print("✅ Prediction Result:")
print(json.dumps(response.json(), indent=4))
