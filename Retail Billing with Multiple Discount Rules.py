price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

if price <= 0 or quantity <= 0:
    print("Invalid input")

else:
    subtotal = price * quantity

    if subtotal >= 1000:
        discount = subtotal * 0.10

        if discount > 200:
            discount = 200
    else:
        discount = 0

    amount = subtotal - discount
    tax = amount * 0.05
    total = amount + tax

    print("Subtotal: Rs.", subtotal)
    print("Discount: Rs.", discount)
    print("Tax: Rs.", tax)
    print("Final Bill: Rs.", total)
