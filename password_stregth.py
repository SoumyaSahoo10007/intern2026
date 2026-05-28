x=input("enter the password:")
temp=0
for i in range(len(x)):
    if x[i].isdigit():
        for i in range(len(x)):
            if x[i].isupper():
                if len(x)>=8:
                   temp=1
if temp==1:
    print("strong password")
else:
    print("weak password")
