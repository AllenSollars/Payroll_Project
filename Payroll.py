payrate = 13.75
overtimeMultiplier = 1.5
stateTaxRate = 0.056
federalTaxRate = 0.079
maxHours = 40

name = input("What is your name?")
print("Hello, "+ name  )
print("Next")

#prompt the user for their ID number.

userId = input("Please enter your ID number: ")
print(f"You entered ID: {userId}")
print("Thank you, "+ name)
print("next")

#prompt the user for The amount of hours worked for the week.

hoursWorked = float(input("Enter the amount of hours worked this week (max 40): "))
print(f"You entered: {hoursWorked}")

overtimeHours = float(input("Enter overtime if any otherwise enter 0: "))
print(f"You entered: {overtimeHours}")

print("Thank you, " + name)
print("Thank you, we will register the information shortly")


if hoursWorked <= maxHours and overtimeHours == 0:
    grossPay = hoursWorked * payrate
    overtimePay = 0
else:
    grossPay = hoursWorked * payrate
    overtimePay = overtimeHours * payrate * overtimeMultiplier

stateTax = grossPay * stateTaxRate
federalTax = grossPay *federalTaxRate
totalTax = stateTax + federalTax

netPay = grossPay - totalTax

employee = {
    "name": name,
    "userId": userId,
    "hoursWorked": hoursWorked,
    "overtimeHours": overtimeHours,
    "grossPay": grossPay,
    "overtimePay": overtimePay,
    "stateTax": stateTax,
    "federalTax": federalTax,
    "netPay": netPay
}

print(employee)

# Write employee data to a file
with open("workersheet.txt", "a") as f:
    f.write("\n--- New Employee ---\n")
    for key, value in employee.items():
        f.write(f"{key}: {value}\n")