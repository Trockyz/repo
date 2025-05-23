hwage=float(input("Hourly wage: "))
hhour=int(input("Hours worked: "))
day=(input("Day of the week: "))
if day=="Sunday":
    
    print(f"Daily wages: {(hwage*hhour)*2} euros")
else:
    print(f"Daily wages: {hwage*hhour} euros")
print()