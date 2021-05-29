day=input("enter day")
time=input("enter time")
if day=="monday":
    if time=="breakfast":
        print("masala dosa")
    elif time=="lunch":
        print("rice")
    elif time=="snacks":
        print("pakode")
    else:
        print("chapati,baji")
elif day=="tuesday":
    if time=="breakfast":
        print("aape")
    elif time=="lunch":
        print("dal,rice")
    elif time=="snacks":
        print("vada pav")
    else:
        print("bakari,baji")
else:
    if time=="breakfast":
        print("edli,chatani")
    elif time=="lunch":
        print("veg biryani")
    elif time=="snacks":
        print("bel")
    else:
        print("mix baji,chapati")