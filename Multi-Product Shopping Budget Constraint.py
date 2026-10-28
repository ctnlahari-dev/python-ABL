budget = float(input("Enter shopping budget: "))

price1 = float(input("Enter price of product 1: "))
quantity1 = int(input("Enter quantity of product 1: "))

price2 = float(input("Enter price of product 2: "))
quantity2 = int(input("Enter quantity of product 2: "))

price3 = float(input("Enter price of product 3: "))
quantity3 = int(input("Enter quantity of product 3: "))

if (budget < 0 or price1 <= 0 or price2 <= 0 or price3 <= 0
        or quantity1 <= 0 or quantity2 <= 0 or quantity3 <= 0):
    print("Invalid input")

else:
    cost1 = price1 * quantity1
    cost2 = price2 * quantity2
    cost3 = price3 * quantity3

    total = cost1 + cost2 + cost3

    print("Total Shopping Cost: Rs.", total)

    if total > budget:
        print("Status: Over Budget")
        print("Extra Amount Needed: Rs.", total - budget)
    else:
        print("Status: Within Budget")
        print("Remaining Budget: Rs.", budget - total)

