import requests
import random

def fetch_trending_coin():
    try:
        url = "https://api.coingecko.com/api/v3/search/trending"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        coins = [coin["item"]["name"] for coin in data["coins"]]
        return random.choice(coins) if coins else None
    except Exception as e:
        print(f"Error fetching trending coins: {e}")
        return None

def simulate_trade(coin, simulate=True):
    if simulate:
        print(f"[SIMULATION] Would trade {coin}")
    else:
        print(f"Placing real trade for {coin} (NOT IMPLEMENTED)")