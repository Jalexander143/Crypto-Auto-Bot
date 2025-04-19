import os
from discord_alert import send_alert
from utils import fetch_trending_coin, simulate_trade

SIMULATE = os.getenv("SIMULATE", "True") == "True"

def main():
    coin = fetch_trending_coin()
    if coin:
        entry_price, exit_price = simulate_trade(coin, SIMULATE)
        if entry_price and exit_price:
            send_alert(f"📈 Simulated BUY: {coin} at ${entry_price}")
            send_alert(f"📉 Simulated SELL: {coin} at ${exit_price}")

if __name__ == "__main__":
    main()

