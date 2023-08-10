import os
import sys
import json
def bank_sys():
    prompt = input(f"{usr}/command>")
    if prompt == "help" or prompt == "?":
        print("""        help/?
        list-users
        add-user
        remove-user
        change-creds
        log-out
        login-as-user
        clear""")
    elif prompt == "clear":
        os.system("clear")
    elif prompt == "add-user":
        fname = input("full-name>")
        balance = int(input("balance>"))
        address = input("address>")
        phonenumber = input("phonenumber>")
        other = input("otherinfo>")
        upwd = input("user-password>")
        info = {
        "name": f"{fname}",
        "balance": balance,
        "address": f"{address}",
        "phonenumber": f"{phonenumber}",
        "other-info": f"{other}",
        "user-password": f"{upwd}"
    }
        json_object = json.dumps(info, indent=4)
        with open(f"db/{fname}", "w") as outfile:
            outfile.write(json_object)
        print("USER CREATED")
    elif prompt == "list-users":
        os.system("ls db")
    elif prompt == "log-out":
        exit()
    elif prompt == "remove-user":
        usrn = input("username>")
        os.remove(f"db/{usrn}")
    elif prompt == "change-creds":
        newusrn = input("new-user-name>")
        newpwd = input("new-password>")
        p = open("creds/pass.key", "a")
        p.write(f"{newpwd}")
        p.close()
        n = open("creds/usr.key", "a")
        n.write(f"{newusrn}")
        n.close()
        
    elif prompt == "login-as-user":
        uname = input("username>")        
        with open(f'db/{uname}') as f:
            un = json.load(f)['name']
            if un == uname:
                pwd = input("password>")
                with open(f'db/{uname}') as f:
                    pw = json.load(f)['user-password']
        while True:
                    if pwd == pw:
                        promptu = input(f"{uname}/command>")
                        if promptu == "help" or promptu == "?":
                            print("""        help/?
                        delete-account
                        log-off
                        see-balance""")
                        elif promptu == "delete-account":
                            os.remove(f"db/{uname}")
                            print("ACCOUNT DELETED")
                            break
                        elif promptu == "see-balance":
                            with open(f'db/{uname}') as f:
                                balance = json.load(f)['balance']
                                print(f"YOUR BALANCE IS : ${balance}")
                        elif promptu == "see-balance":
                            with open(f'db/{uname}') as f:
                                balance = json.load(f)['balance']
                                print(f"YOUR BALANCE IS : ${balance}")
                        elif promptu == "log-off":
                            break
                    else:
                        print("PLEASE TRY AGAIN")
os.system("clear")
print("WELCOME TO THE-LIZZZ BANK SYSTEM")
usr = input("USERNAME:")
pwd = input("PASSWORD:")
while True:
    u = open("creds/usr.key", "r")
    p= open("creds/pass.key", "r")
    if(u.readline() == usr):
        if(p.readline() == pwd):
            bank_sys()
        else:
            os.system("clear")
            print(f"PLEASE TRY AGAIN")
            exit()            