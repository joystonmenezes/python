terms=int(input("enter the terms :"))
if terms<=0:
    return 
elif terms==1:
    print("0")
    return 
else:
    a,b=0,1
    print(a,b,end =" ")
    for i in range(terms-2):
        print(a+b,end=" ")
        c=a+b
        a,b=b,c
