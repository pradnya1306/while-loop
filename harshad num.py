


i=1
sum=0
num1=int(input("enter the number"))
z=num1
while i<=num1:
    n=num1%10
    sum=sum+n
    num1=num1//10
print(sum)
if z%sum==0:
    print(z,"is harshad number")
else:
    print(z,"is not harshad number")
