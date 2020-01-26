import requests

url = "https://slack.com/api/conversations.history"
token = "******"
channel_id = "******"

def history():
    payload = {
        "token": token,
        "channel": channel_id,
        "limit": 1000
    }
    response = requests.get(url, params=payload)

    json_data = response.json()
    messages = json_data["messages"]
    for message in messages:
        yield message
