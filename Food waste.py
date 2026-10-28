prepared = float(input("Enter food prepared (kg): "))
wasted = float(input("Enter food wasted (kg): "))

if prepared <= 0 or wasted < 0 or wasted > prepared:
    print("Invalid input")

else:
    used = prepared - wasted
    percentage = (wasted / prepared) * 100

    print("Food Used:", round(used, 2), "kg")
    print("Food Waste:", round(wasted, 2), "kg")
    print("Waste Percentage:", round(percentage, 2), "%")

    if percentage <= 10:
        print("Food waste is acceptable")
    else:
        print("Try to reduce food waste")
