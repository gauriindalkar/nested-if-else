print("welcome")
atm_card=input("enter type of card")
if atm_card=="debit card" or "credit card":
    option=input("enter your option")
    if option=="balance enquiry":
        language=input("enter a language")
        if language=="english" or "hindi" or "marathi" or "gujrati":
            balance_check=int(input("enter pin 4 digit or 6 digit"))
            if balance_check=="4 digit" or "6 digit":
                receipt=input("you want receipt")
                if receipt=="yes":
                    print("yes")
                else:
                    print("no")
            else:
                print("incorrect")
        else:
            print("you choose other language")
    elif option=="withdrawal cash":
        language=input("enter a language")
        if language=="english" or "hindi" or "marathi" or "gujrati":
            account=input("enter your account")
            if account=="saving account" or "current account":
                amount=int(input("enter your amount"))
                if amount<20000:
                    receipt=input("you want receipt")
                    if receipt=="yes":
                        amount=input("pick your amount")
                        if amount=="yes":
                            print("correct")
                        else:
                            print("incorrent")
                    else:
                        print("incorrect")
                else:
                    print("incorrect")
            else:
                print("incorrect")
        else:
            print("incorrect")
    elif option=="pin change":
        old_pin=int(input("enter a pin number 4 digit or 6 digit"))
        if old_pin=="4 digit" or "6 digit":
            new_pin=int(input("enter a new pin 4 digit or 6 digit"))
            if new_pin=="4 digit" or"6 digit":
                print("correct")
            else:
                print("incorrect")
        else:
            print("incorrect")
    else:
        print(finshed)
else:
    print("error")