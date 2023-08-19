print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))

each_people_bill = (bill + bill * tip_percentage / 100) / no_of_people

print(f"Each person should pay: {round(each_people_bill, 2)}")
print("{0} is greater than {1}".format(6, 4))
print("{0} is greater than {1}".find('se'))
