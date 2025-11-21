import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <basic_salary> <hra>")
    sys.exit(1)

try:

    basic_salary = float(sys.argv[1])
    hra = float(sys.argv[2])
except ValueError:
    print("Error: Both basic salary and HRA must be numbers.")
    sys.exit(1)


if basic_salary < 0 or hra < 0:
    print("Error: Salary and HRA must be non-negative numbers.")
else:
    total_salary = basic_salary + hra
    print(f"Basic Salary: {basic_salary}")
    print(f"HRA: {hra}")
    print(f"Total Salary: {total_salary}")
