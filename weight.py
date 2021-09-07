i=1
sum=0
while i<=11:
    weight=int(input("enter the weight"))
    sum=sum+weight
    i=i+1 
print(sum)
if sum%5==0:
    print("divisible")
else:
    print("not divisible")    