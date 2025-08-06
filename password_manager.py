



def view():
    name = input("Account Name: ")
    
    try:
        with open("passwords.txt", "r") as f:
            found = False
            for line in f.readlines():
                data = line.rstrip()
                if "|" in data:
                    account, password = data.split("|")
                    if name.lower() == account.lower():
                        print("Your Account:", account, "and Password:", password)
                        found = True
                        break
            
            if not found:
                print("No account found with that name.")
    except FileNotFoundError:
        print("No passwords file found. Add some passwords first.")
    
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    
    try:
        with open("passwords.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                if "|" in data:
                    account, password = data.split("|")
                    if name.lower() == account.lower():
                        print("Account already exists. Please choose a different name.")
                        return
    except FileNotFoundError:
        pass
