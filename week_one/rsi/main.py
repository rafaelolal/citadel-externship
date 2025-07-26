from statistics import mean


def rsi(prices, period=14):
    deltas = [0] + [prices[i+1] - prices[i] for i in range(len(prices)-1)]
    up = [0 if i < 0 else i for i in deltas]
    down = [0 if i > 0 else -i for i in deltas]
    up_ema = [0] * len(up)
    down_ema = [0] * len(down)
    rsis = [0] * len(up)
    a = 1 / period

    up_ema[period] = mean(up[:period+1])
    down_ema[period] = mean(down[:period+1])

    for i in range(period+1, len(up)):
        up_ema[i] = a * up[i] + (1 - a) * up_ema[i-1]
        down_ema[i] = a * down[i] + (1 - a) * down_ema[i-1]
        rs = up_ema[i] / down_ema[i] if down_ema[i] != 0 else 0
        rsis[i] = 100 - (100 / (1 + rs))

    return rsis


prices = [120.34, 121.56, 122.78, 120.98, 119.67, 121.23, 122.45, 123.67, 124.89,
          126.11, 124.33, 125.55, 126.77, 128.99, 127.21, 128.43, 129.65, 130.87, 132.09, 133.31]

print(",".join(list(map(str, prices[::-1]))))
print(rsi(prices, 14))

# identify divergences
# decide when to short or long
