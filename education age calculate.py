year=int(input("enter a year"))
if year<2021:
    print(2021-year,"it is age")
    age=int(input("enter a age"))
    if age<=6 and age>=12:
        print("7th complete")
        if age<=13 and age>=16:
            print("10th complete")
            if age<=17 and age>=18:
                print("12th complete")
                if age<=19 and age>=21:
                    print("graduation complete")
                else:
                    print("incomlete")
            else:
                print("incomplete")
        else:
            print("incomplete")
    else:
        print("incomplete")
else:
    print("it is not age")