basic_salary = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime pay: "))
incentives = float(input("Enter incentives: "))

if basic_salary < 0 or allowances < 0 or overtime < 0 or incentives < 0:
    print("Invalid salary details")
else:
    gross_salary = basic_salary + allowances + overtime + incentives

    deductions = gross_salary * 0.05
    net_salary = gross_salary - deductions

    print("Gross Salary: Rs.", gross_salary)
    print("Deductions: Rs.", deductions)
    print("Net Salary: Rs.", net_salary)

