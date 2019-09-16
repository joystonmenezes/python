string=raw_input("Enter string :")
print("original string:",string)
res=""
for ch in string:
    if ch not in "!@#$%^&*()_-{}[]|';:,.<>?~=+":
        res += ch
print("String without punctuations :",res)
