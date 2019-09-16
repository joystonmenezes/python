'''num=int(input("Enter the number"));
s =0
count=0
while(count<=num):
    s =s+count
    count=count+1
# s =(num*(num+1))/
 


print("the sum of the number are %d" %s)
print (">>>>>>>>>>>>>>>>>>>>>>>>")
for i in range(10,20,2):
   print(i)
n=int(input("Enter the number"))
for i in range (1,11):
    print("%d  *  %d  =  %d " %(n,i,n*i) )
# number of minutes in year;
print(60*24*365)
#compute the triangle
l1=int(input("Enter the side one of triangle"))
l2=int(input("Enter the side two of triangle"))
l3=int(input("Enter the side three of triangle"))
if(l1==l2):
    if(l2==l3):
        print("given triangle is equilateral")
    else: print("not equilateral")
    
#right triangle
l1=int(input("Enter the side one of triangle"))
l2=int(input("Enter the side two of triangle"))
l3=int(input("Enter the side three of triangle"))

if(l1**2==l2**2+l3**2):
    print("its an right angle triangle")
elif(l2**2==l1**2+l3**2):
    print("its an right angle triangle")
elif(l3**2==l1**2+l1**2):
    print("its an right angle triangle")
else: print ("not right triangle")'''
m=int(input("Enter the value 1"))
n=int(input("Enter the value 2"))
m1=m
m2=n
rem=0
while(n!=0):
    rem=m%n
    m=n
    n=rem 
print("gcd is %d" %(m))
print("lcm is %d" %(m1*m2/m))