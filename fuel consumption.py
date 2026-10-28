distance1 = float(input("Enter Route 1 distance (km): "))
distance2 = float(input("Enter Route 2 distance (km): "))
mileage = float(input("Enter vehicle mileage (km/litre): "))
fuel_price = float(input("Enter fuel price per litre: "))

if distance1 <= 0 or distance2 <= 0 or mileage <= 0 or fuel_price <= 0:
    print("Invalid input")

else:
    fuel1 = distance1 / mileage
    fuel2 = distance2 / mileage

    cost1 = fuel1 * fuel_price
    cost2 = fuel2 * fuel_price

    print("Route 1 fuel required:", round(fuel1, 2), "litres")
    print("Route 1 travel cost: Rs.", round(cost1, 2))

    print("Route 2 fuel required:", round(fuel2, 2), "litres")
    print("Route 2 travel cost: Rs.", round(cost2, 2))

    if cost1 < cost2:
        print("Route 1 is cheaper")
    elif cost2 < cost1:
        print("Route 2 is cheaper")
    else:
        print("Both routes cost the same")
