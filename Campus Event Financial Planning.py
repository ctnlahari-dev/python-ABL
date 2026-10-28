budget = float(input("Enter event budget: "))
venue = float(input("Enter venue expenses: "))
food = float(input("Enter food expenses: "))
decoration = float(input("Enter decoration expenses: "))

if budget < 0 or venue < 0 or food < 0 or decoration < 0:
    print("Invalid input")

else:
    total = venue + food + decoration
    remaining = budget - total

    print("Total Expenses: Rs.", total)
    print("Remaining Budget: Rs.", remaining)

    if total > budget:
        print("Status: Over Budget")
    else:
        print("Status: Within Budget")
