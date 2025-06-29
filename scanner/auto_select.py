import requests
from config import TOP_PAIRS


def fetch_top_gainers(limit=10):
    """
    Samo jerin coins masu tashi (top gainers) daga CoinGecko.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "percent_change_24h_desc",
        "per_page": limit,
        "page": 1,
        "sparkline": False
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        return [coin['symbol'].upper() + "/USDT" for coin in data]
    except Exception as e:
        print(f"❌ Kuskure yayin samun top gainers: {e}")
        return []


def select_best_pair():
    """
    Zabi token ko coin da zai fi dacewa ayi analysis based on strategy.
    """
    # Za mu fara da top gainers ko hardcoded list
    pairs = fetch_top_gainers() or TOP_PAIRS
    for pair in pairs:
        if is_pair_valid(pair):
            return pair
    return None


def is_pair_valid(pair):
    """
    Zaka iya amfani da wannan wajen saka sharudda kamar volume, trend, volatility da sauransu.
    """
    return True  # Za a canza wannan daga baya bisa criteria


if __name__ == "__main__":
    print("Best pair:", select_best_pair())
