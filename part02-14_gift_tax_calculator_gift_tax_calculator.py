# Write your solution here
val=int(input("Value of gift: "))
if val<5000:
    print("No tax!")
if val>5000 and val<=25000:
    print(f"Amount of tax: {100+(val-5000)*0.08}")
if val>25000 and val <=55000:
    print(f"Amount of tax: {1700+(val-25000)*0.10}")
if val>55000 and val<=200000:
    print(f"Amount of tax: {4700+(val-55000)*0.12}")
if val>200000 and val<=1000000:
    print(f"Amount of tax: {22100+(val-200000)*0.15}")
if val>1000000:
    print(f"Amount of tax: {142100+(val-1000000)*0.17}")
