def calculate_profit(cost_price, selling_price, quantity):
    profit = (selling_price - cost_price) * quantity
    return profit

# Example usage
cost_price = 100
selling_price = 140
quantity = 50

profit = calculate_profit(cost_price, selling_price, quantity)
print("Total Profit:", profit)
