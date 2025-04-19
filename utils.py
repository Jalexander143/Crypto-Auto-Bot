import requests
import random
import time

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
        entry_price = round(random.uniform(1.0, 100.0), 2)
        print(f"[SIMULATION] Buying {coin} at ${entry_price}")
        time.sleep(2)  # Simulated time passing
        exit_price = round(entry_price * random.uniform(1.02, 1.15), 2)
        print(f"[SIMULATION] Selling {coin} at ${exit_price}")
        return entry_price, exit_price
    else:
        print(f"[LIVE TRADING] Not yet implemented.")
        return None, None
