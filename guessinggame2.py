i=1
while i<=3:
    number=int(input("enter the number : "))
    if number < 5:
        print(number, "your guess is lesser")
    elif number > 5:
        print(number,"your guess is greater")
    else:
        
        print(5,"your guess is correct")
        break
    i=i+1
else:
    print("you have miss the number")