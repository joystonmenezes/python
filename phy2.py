print("Enter the details of employee")
Eid=int(input("Enter the employee ID: "))

allownce=int(input("Enter the allowance of the employee: "))
base=int(input("Enter the basic salary of the employee: "))
gross=base+allownce
  
if gross>20000:
    tax=gross*0.3
elif gross>10000:
    tax=gross*0.2
elif gross>5000:
    tax=gross*0.1
else:
    tax=0
net= gross-tax;
print("Employee details :")
print("ID :",Eid);
print("Allowance :",allownce);
print("basic salary :",base);

print("Gross salary :",gross);

print("income tax :",tax);
print("Net salary :",net);


