def calculate_max_profit(total_units, rent, increase, maintenance):
    max_profit = 0
    optimal_units = 0
    for units_rented in range(total_units + 1):
        current_rent = rent + (total_units - units_rented) * increase
        profit = (units_rented * current_rent) - (units_rented * maintenance)
        if profit > max_profit:
            max_profit = profit
            optimal_units = units_rented
    return optimal_units, max_profit
