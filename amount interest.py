amount = float(input('Enter your amount : '))
inrate = float(input('Enter interest rate : '))
period = int(input("Enter period: "))
value = 0
year = 1
while year <= period:
    value = amount+(inrate * amount)
    print("year %d Rs. %.2f" %(year,value))
    amount = value
    year = year + 1