print("from 2010 to 2020 :")
for year in range(2010,2021):
    if (year%4==0) and (year%100!=0) or (year%400==0):
        n=366
    else:
        n=365
    print("Year",year," = ",n," days")
    