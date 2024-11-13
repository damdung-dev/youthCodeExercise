def electricity_bill(kWh):
    if kWh <= 100:
        return kWh * 500
    elif kWh <= 250:
        return 100 * 500 + (kWh - 100) * 800
    elif kWh <= 350:
        return 100 * 500 + 150 * 800 + (kWh - 250) * 1000
    else:
        return 100 * 500 + 150 * 800 + 100 * 1000 + (kWh - 350) * 1500

kwh=int(input("nhập vào số kwh tiêu thụ: "))
print(electricity_bill(kwh))
