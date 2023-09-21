print("***Welcome to TIP Calculator***")
bill = float(input("Enter your bill: \n"))
mem = int(input("Enter number of people: \n"))
tip = int(input("What percent of tip would you like: 10, 12 or 15?\n")
)

total_bill=round((bill/mem)*(1+(tip/100)), 2)

print(f"Each person should pay: {total_bill}")