def electricity_cost(kWh):
    cost = 0
    if kWh <= 100:
        cost = kWh * 500
    elif kWh <= 250:
        cost = 100 * 500 + (kWh - 100) * 800
    elif kWh <= 350:
        cost = 100 * 500 + 150 * 800 + (kWh - 250) * 1000
    else:
        cost = 100 * 500 + 150 * 800 + 100 * 1000 + (kWh - 350) * 1500
    return cost

# Example usage
kWh = int(input("Enter the number of kWh consumed: "))
print("Electricity cost:", electricity_cost(kWh), "VND")
