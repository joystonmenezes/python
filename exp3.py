l=[]
n=int(input("Enter the number of elements :"))
for i in range(n):
    ele=int(input("Enter  element "))
    l.append(ele)
l.sort(key=None, reverse=False)
print(l)
k=int(input("Enter the key element :"))
low=0
high=n-1
while(low<=high):
    mid=((low+high)/2)
    if(k==l[mid]): 
        print("key found at position %d" %(mid+1))
        exit(0)
    elif(k>l[mid]):
        low=mid+1
    else:
        high=min-1
else: print("Element not found")
 
 

