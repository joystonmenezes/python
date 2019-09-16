string=raw_input("Enter string :")
count=0
for ch in string:
    if ch in"AEIOUaeiou":
        count+=1
print("Number of vowels in "+string+" is", count)