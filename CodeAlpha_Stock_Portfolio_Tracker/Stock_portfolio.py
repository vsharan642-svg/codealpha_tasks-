print("Welcome to our Stock Portfolio Tracker")

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("======================================")
print("       STOCK PORTFOLIO TRACKER        ")
print("======================================")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(stock, ":", price)

number_of_stocks = int(input("\nEnter number of stocks: "))

for i in range(number_of_stocks):

    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

        total_investment = total_investment + investment

        print("Investment:", investment)

    else:
        print("Invalid stock name!")

print("\n======================================")
print("          PORTFOLIO SUMMARY           ")
print("======================================")

for stock, quantity in portfolio.items():
    print(stock, "Quantity:", quantity)

print("\nTotal Investment Value:", total_investment)

# Save portfolio to a text file
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("=======================\n")

    for stock, quantity in portfolio.items():
        file.write(stock + " Quantity: " + str(quantity) + "\n")

    file.write("Total Investment Value: " + str(total_investment))

print("\nPortfolio saved successfully in portfolio.txt")
