i=1
sum=0
number=int(input("enter the number : "))
while i<number:
    if number%i==0:
        sum=sum+i
    i=i+1
print("sum of above",sum)
if sum==number:
    print(number,"perfect number")
else:
     print(number,"not perfect number")   

