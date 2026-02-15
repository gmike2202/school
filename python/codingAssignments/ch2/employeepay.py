"""
this is a program that will ask for the input of a wage,
regular hours, overtime hours and put the relevant components into the formula
to calculate the total weekly pay. This pay is then displayed for the
user to see
"""

wage = float(input("Enter the wage: "))
regHours = int(input("Enter the regular hours: "))
overHours = int(input("Enter the overtime hours: "))

total = (regHours * wage) + (overHours * (wage * 1.5))
print("The total weekly pay is $" + str(total))
