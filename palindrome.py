num=int(input("enter thr number"))
i=1
while i<=num:
    n=num%10
    num=num//10
    i=i+1

sum=(n*100)+(n*10)+(n)
print(n)

number=int(input("enter the num"))
i=1
while i<=number:
    n=number%10
    num=number//10
    n1=num%10
    num=num//10
    sum=(n*100)+(n1*10)+(num)
    i+=1
print(sum)
if sum==number:
    print ("it is palindrome")
else:
    print("it is not palindrome")