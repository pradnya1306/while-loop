
i=0
number=int(input("enter the number"))
conunt=0
while i<=number:
    if number%i==0:
        count=count+1
    i=i+1
if count==2:
    print("prime number")
else:
    print(number," not prime number")

    
