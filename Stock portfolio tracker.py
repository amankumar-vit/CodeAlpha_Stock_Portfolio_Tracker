stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "AMZN": 3300
}

total = 0

print("Stock Portfolio Tracker")

while True:
    stock = input("Enter stock name (or 'done'): ").upper()

    if stock == "DONE":
        break

    if stock not in stocks:
        print("Stock not available")
        continue

    qty = int(input("Enter quantity: "))
    total += stocks[stock] * qty

print("Total Investment Value:", total)

# Save to file
with open("portfolio.txt", "w") as f:
    f.write(f"Total Investment: {total}")

print("Saved to file!")
