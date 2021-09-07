num=int(input("enter the number"))
z=num
sum=0
while num>0:
    i=1
    fact=1
    n=num%10
    while i<=n:
        fact=fact*i
        i=i+1
    sum=sum+fact
    num=num//10
print(sum)
if sum==z:
    print("strong number")
else:
    print("not strong number")
    
 


    



