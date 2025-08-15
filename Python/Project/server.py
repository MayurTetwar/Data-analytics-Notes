import requests

url = "https://backend-ag0a91yml-mayur-tetwars-projects.vercel.app/send-otp"
data = {
    "phone_number": "8830666316"
}
response = requests.post(url, json=data)
print(response.json())