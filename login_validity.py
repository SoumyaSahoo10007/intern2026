passwd="python123"
userN="admin"
p=input("enter the password:")
u=input("enter the username:")
if p==passwd and u==userN:
    print("login successful")
elif p==passwd:
    print("invalid username")
elif u==userN:
    print("invalid password")
else:
    print("invalid credential")
    