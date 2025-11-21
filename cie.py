import sys

if len(sys.argv) != 4:
     hra=float(sys.argv[1])
     ta=float(sys.argv[2])
     da=float(sys.argv[3])
else:
    hra = "100" 
    ta = "30"
    da ="20"
    
gross_salary = basic_salary + hra + ta + da    

print("HRA: {hra}")
print("TA: {ta}")
print("DA: {da}")
print("Gross Salary: {gross salary}")
