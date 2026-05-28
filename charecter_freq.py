x=input("enter the string:")
y=input("enter the charecter:")
count=0
for i in range(len(x)):
    if x[i]==y:
        count +=1
print("charecter count:",count)