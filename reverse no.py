i=1
number=int(input("enter the number"))
while i<=number:
    n=number%10
    num=number//10
    n1=num%10
    num=num//10
    sum=(n*100)+(n1*10)+num
    i=i+1
print(sum)


i=1
sum=0
while i<=11:
    num= int(input("enter thee num"))
    sum=sum+num
    i+=1
# print(sum)
    average=sum/11
print(average)
if average%5==0:
    print("divisible")
else:
    print("not divisible")
