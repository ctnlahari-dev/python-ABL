rows = int(input("Enter number of rows (1-20): "))

if rows < 1 or rows > 20:
    print("Invalid number of rows")

else:
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


