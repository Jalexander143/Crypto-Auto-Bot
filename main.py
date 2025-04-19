import os
from discord_alert import send_alert
from utils import fetch_trending_coin, simulate_trade

SIMULATE = os.getenv("SIMULATE", "True") == "True"

def main():
    coin = fetch_trending_coin()
    if coin:
        message = f"Trending Coin: {coin}"
        send_alert(message)
        simulate_trade(coin, SIMULATE)

if __name__ == "__main__":
    main()