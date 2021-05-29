a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
if a>b:
    if a>c:
        print(a,"is greater number")
    else:
        print(b,"is greater number")
elif b>c:
    if b>a:
        print(b,"is greater number")
    else:
        print(c,"is greater number")
elif c>a:
    if c>b:
        print(c,"is gearter number")
    else:
        print(a,"is greater number")
    
