a=input("Write your own word: ")
b=input("Write your own charecter: ")
i=0
c=0
while (i<=len(a)):
    if a[i]==b:
        c+=1
    i+=1
print(b," has occured ",c," times")