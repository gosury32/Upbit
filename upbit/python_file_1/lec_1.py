import pyupbit

access = "r4xxPKHViBzEx8Q7xMtSBzxz4JZwLoaDsMPRMtbQ"          # 본인 값으로 변경
secret = "nY1YqDGnfp5Ezlh7J0VMTDcWnGBv2BRiDiN1yxqq"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회