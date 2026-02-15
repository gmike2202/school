starting_salary = float(input("Enter the starting salary: $"))
percent = float(input("Enter the annual % increase: "))
years = int(input("Enter the number of years: "))

print("Year   Salary")
print("-------------")

current_salary = starting_salary

for year in range(1, years + 1):
    print("%-3d  %.2f" % (year, current_salary))
    current_salary += current_salary * (percent / 100)
