import os
from discord_alert import send_alert
from utils import fetch_trending_coin, simulate_trade

SIMULATE = os.getenv("SIMULATE", "True") == "True"

def main():
    coin = fetch_trending_coin()
    if coin:
        entry_message = f"📈 Simulated BUY: {coin} (entry price simulated)"
        send_alert(entry_message)
        entry, exit = simulate_trade(coin, SIMULATE)
        if entry and exit:
            send_alert(f"📉 Simulated SELL: {coin} (exit price simulated)")

if __name__ == "__main__":
    main()
