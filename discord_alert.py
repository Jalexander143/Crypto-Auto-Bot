import os
import requests

def send_alert(message):
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    if webhook_url:
        try:
            requests.post(webhook_url, json={"content": message})
        except Exception as e:
            print(f"Error sending alert: {e}")
    else:
        print("No webhook URL configured.")