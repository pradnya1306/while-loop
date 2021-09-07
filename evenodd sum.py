startnum=int(input("enter the number"))
endnum=int(input("entern the number"))
i=startnum
sum=0
sum1=0
while i<= endnum:
    if i%2==0:
        sum=sum+i
    else:
        sum1=sum1+i
    i=i+1
print("even",sum)
print("odd",sum1)