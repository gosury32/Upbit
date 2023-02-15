import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC", count=7)
print(df)