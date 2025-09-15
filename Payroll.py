hours = input("enter hours worked: ")


if (float(hours)) <= 40: 
    grossPay = (float(hours)) * 13.75
else:
    print("error, too many hours worked")
print(grossPay)