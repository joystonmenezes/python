string1=raw_input("Enter string 1 :")
string2=raw_input("Enter string 1 :")
res=" "
for ch in string1:
    if ch.isupper():
        res+=ch
for ch in string2:
    if ch.isupper():
        '''s=string1+string2
     for ch in s:
         if ch.isupper():'''


        
        res+=ch
print("output is",res)

