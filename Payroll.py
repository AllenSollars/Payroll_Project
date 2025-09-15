hours = input("enter hours worked: ")


if hours < 40: 
    grossPay = (float(hours)) * 13.75
else:
    print("error, too many hours worked")
print(grossPay)