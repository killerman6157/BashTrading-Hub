import numpy as np

def detect_smc_signal(ohlc_data):
    """
    Strategy: Smart Money Entry (SMC)
    Conditions:
    - Break of Structure (BOS)
    - Order Block (OB)
    - Fair Value Gap (FVG)
    """
    try:
        closes = [candle['close'] for candle in ohlc_data[-10:]]
        highs = [candle['high'] for candle in ohlc_data[-10:]]
        lows = [candle['low'] for candle in ohlc_data[-10:]]

        # 1. Detect Break of Structure (BOS)
        bos = closes[-1] > max(closes[:-1])  # bullish BOS

        # 2. Detect Order Block (OB): recent candle with large body
        ob_found = False
        for candle in reversed(ohlc_data[-5:]):
            body = abs(candle['close'] - candle['open'])
            wick = abs(candle['high'] - candle['low']) - body
            if body > wick * 1.5:
                ob_found = True
                break

        # 3. Detect Fair Value Gap (FVG): large gap between candles
        fvg_found = False
        for i in range(2, len(ohlc_data)):
            prev = ohlc_data[i - 2]
            curr = ohlc_data[i]
            if curr['low'] > prev['high']:
                fvg_found = True
                break

        if bos and ob_found and fvg_found:
            return {
                "signal": True,
                "note": "SMC setup confirmed: BOS, OB, FVG",
                "strength": "strong"
            }

        return {
            "signal": False,
            "note": "No valid SMC signal at the moment."
        }
    
    except Exception as e:
        return {
            "signal": False,
            "note": f"Error detecting SMC signal: {e}"
        }
