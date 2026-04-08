#  tip calculator mini project

print("Welcome to the tip calculator!")
bill= float(input("what was the total bill? $ "))

tip= int(input("how much tip would you like to give? 10, 12, or 15?  "))
people= int(input("how many people to split the bill?  "))

final_bill= bill + (bill * tip / 100)
bill_per_person= final_bill / people
final_amount= round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")