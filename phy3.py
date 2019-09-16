print("Enter the details of customer")
Eid=int(input("Enter the customer ID: "))

billid=int(input("Enter the bill ID :"))
billamt=int(input("Enter the bill amount : "))
n=raw_input("Enter your name :")
l= len(n)
if l>3 and l<12:
    print("valid customer")
    print("CID",Eid)
    print("Customer name",n)
    print("BILL ID",billid)
    print("BILL AMOUNT",billamt)
    
else:
    print ("invalid customer");
 
    