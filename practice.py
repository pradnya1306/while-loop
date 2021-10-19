i=5
while i>=1:
    j=1
    while j<=i:
        print(j," " ,end="")
        j=j+1

    print()
    i=i-1


question=["what is your name?","what is your age?","what are you doung?"]
option=[["neha","sonu","monu"],[10,20,30],["Bsc","Bcom","BA"]]
i=0
while i<len(question):
    print(question[i])
    j=0
    while j<len(option[i]):
        print(j+1,option[i][j])
        j=j+1
    i=i+1



list=[1,3,5,7,9,20]
i=0
list2=[]
while i<len(list)-1:
    subtract=list[i+1]
    subtract=subtract-list[i]
    list2.append(subtract)
    i=i+1
print(list2)
a=int(input("enter th numbr"))
b=int(input("enter th numbr"))
c=int(input("enter th numbr"))
# d=int(input("enter th numbr"))
# e=int(input("enter th numbr"))
if a>b and a<c:
    print(a)
elif b>a and b<c:
    print(b)
else:
    print(c)