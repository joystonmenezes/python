result=[str(var) for var in range(2000,3201) if ((var%7==0)and (var%5!=0))]

#print(result)
y= ",".join(result)
print(y)