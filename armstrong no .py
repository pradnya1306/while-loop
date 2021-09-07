

num=int(input("enter the number"))
z=num
i=1
sum=0
while i<=num:
    n=num%10
    sum=sum+n**3
    num=num//10

print(sum)
if sum==z:
    print(z,"is armstrong number.")
else:
    print(z,"is not armstrong number")