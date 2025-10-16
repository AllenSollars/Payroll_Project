payrate = 13.75
overtimeMultiplier = 1.5
stateTaxRate = 0.056
federalTaxRate = 0.079
maxHours = 40

name = input("What is your name? ")
print("Hello, " + name)
print("Next")

userId = input("Please enter your ID number (4 digits): ")
print(f"You entered ID: {userId}")
print("Thank you, " + name)
print("next")

hoursWorked = float(input("Enter the amount of hours worked this week (max 40): "))
print(f"You entered: {hoursWorked}")

overtimeHours = float(input("Enter overtime if any otherwise enter 0: "))
print(f"You entered: {overtimeHours}")

print("Thank you, " + name)
print("Thank you, we will register the information shortly")
print("and your total amount for this week is")

if hoursWorked <= maxHours and overtimeHours == 0:
    grossPay = hoursWorked * payrate
    overtimePay = 0
else:
    grossPay = hoursWorked * payrate
    overtimePay = overtimeHours * payrate * overtimeMultiplier

# Add overtime pay to gross pay
totalGrossPay = grossPay + overtimePay

stateTax = totalGrossPay * stateTaxRate
federalTax = totalGrossPay * federalTaxRate
totalTax = stateTax + federalTax

netPay = totalGrossPay - totalTax

print("your gross pay for this week is")
print(f"{totalGrossPay}")
print("your net pay is ")
print(f"{netPay}")

employee_list = [name, userId, hoursWorked, overtimeHours]
print(employee_list)

while True:
    response = input("Is the list correct (yes/no): ").strip().lower()
    if response == "yes":
        print("You chose YES.")
        employee = {
            "name": name,
            "userId": userId,
            "hoursWorked": hoursWorked,
            "overtimeHours": overtimeHours,
            "grossPay": totalGrossPay,
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
        break
    elif response == "no":
        print("You chose NO. Try again")
        break
    else:
        print("Invalid input. Please type 'yes' or 'no'.")