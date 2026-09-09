# Fractional Knapsack using Greedy Method

n = int(input("Enter number of items: "))

items = []

for i in range(n):
    weight = float(input("Enter weight of item " + str(i + 1) + ": "))
    profit = float(input("Enter profit of item " + str(i + 1) + ": "))

    ratio = profit / weight

    items.append([i + 1, weight, profit, ratio])


capacity = float(input("Enter truck capacity: "))

# Sort according to profit/weight ratio
items.sort(key=lambda x: x[3], reverse=True)

total_profit = 0

print("\nSelected items:")

for item in items:

    item_number = item[0]
    weight = item[1]
    profit = item[2]
    ratio = item[3]

    if capacity >= weight:
        capacity -= weight
        total_profit += profit

        print("Item", item_number, ": 100% selected")

    else:
        fraction = capacity / weight
        total_profit += profit * fraction

        print("Item", item_number, ":", fraction * 100, "% selected")

        capacity = 0
        break


print("\nMaximum Profit =", total_profit)