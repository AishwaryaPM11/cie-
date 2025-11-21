import sys


if len(sys.argv) != 2:
    print("Usage: python script.py <basic_salary>")
    sys.exit(1)
    basic_salary = float(sys.argv[1])
else:
    hra = 0.20 * basic_salary
    ta = 0.10 * basic_salary
    da = 0.18 * basic_salary

gross_salary = basic_salary + hra + ta + da


print(f"Basic Salary: {basic_salary}")
print(f"HRA: {hra}")
print(f"TA: {ta}")
print(f"DA: {da}")
print(f"Gross Salary: {gross_salary}")
