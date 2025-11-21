import sys

if len(sys.argv) != 2:
     hra=float(sys.argv[1])
    ta=float(sys.argv[2])
    da=float(sys.argv[3])
else:
    hra = 0.20 * basic_salary
    ta = 0.10 * basic_salary
    da = 0.18 * basic_salary  
    
gross_salary = basic_salary + hra + ta + da    

print("Basic Salary: {basic_salary}")
print("HRA: {hra}")
print("TA: {ta}")
print("DA: {da}")
print("Gross Salary: {gross salary}")
