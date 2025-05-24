# Write your solution here
year=int(input("Year: "))
oriyear=year
while True:
    if (year % 4 == 0 and year % 100 != 0 and oriyear!=year) or (year%400==0 and oriyear!=year):
        print(f"The next leap year after {oriyear} is {year}")
        break
    else:
        year=year+1