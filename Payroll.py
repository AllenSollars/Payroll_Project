name=input("What is your name?")
print("Hello, "+ name  )
print("Next")

#prompt the user for their ID number.

user_id=input("Please enter your ID number: ")
print(f"You entered ID: {user_id}")
print("Thank you, "+ name)
print("next")

#prompt the user for The amount of hours worked for the week.

hours_worked=input("Enter the amount of hours worked this week:")
print(f"You entered: {hours_worked}")
print("Thank you, "+ name)
print("Thank you we will register the information shortly")


if (float(hours_worked)) <= 40: 
    grossPay = (float(hours_worked)) * 13.75
    print(grossPay)
else:
    print("error, too many hours worked")
