i=1
m=5
while i<=5:
    num=int(input("enter the number between 1 to 10 : "))
    if num==m:
        print("guess is right")
        break
    i=i+1
else:
    print("you have miss the number")