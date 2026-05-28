x=input("enter the string:")
largest=0
charecter='a'
for i in range(len(x)):
    count=0
    for j in range(len(x)):
        if x[i]==x[j]:
            count += 1
    if count>=largest:
        largest=count
        charecter=x[i]
print("charecter:",charecter)
print("count:",largest)
