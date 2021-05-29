print("create facebook account")
language=input("enter the language")
if language=="english" or "hindi" or "marathi":
    name=input("enter your name and surname")
    if name=="gauriindalkar":
        email_id=input("enter your email id")
        if email_id=="indalkargauri@gmail.com":
            password=input("enter password")
            if password==password:
                gender=input("enter the gender")
                if gender=="male" or "female" or "others":
                    print("vaild")
                else:
                    print("invaild")
            else:
                print("invaild")
        else:
            print("invaild")
    else:
        print("invaild")
else:
    print("invaild")
