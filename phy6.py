string=raw_input("Enter string :")
count=0
for ch in string:
    if ch.isupper():
        count+=1
print("Number of capital latter in "+string+" is", count)