import json
import os
if 1==1:
        uname = input("username>")        
        with open(f'db/{uname}') as f:
            un = json.load(f)['name']
            if un == uname:
                pwd = input("password>")
                with open(f'db/{uname}') as f:
                    pw = json.load(f)['user-password']
            else:
                 print("EXITING...")
                 exit()
        while True:
                    if pwd == pw:
                        promptu = input(f"{uname}/command>")
                        if promptu == "help" or promptu == "?":
                            print("""
                        help/?
                        delete-account
                        log-off
                        see-balance
                        """)
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