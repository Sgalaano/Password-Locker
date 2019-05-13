
def Galaano():
  print("WELCOME TO PASSWORD LOCKER.")
def Galaano():  
  print("Would you like to continue? (yes/no)")
  answer = input() 
  if answer == "yes":
    print("Okay.Press 1 to continue.")
    one = input()
    if one == "1":
      print("Welcome to password-locker.Would you like to sign up/log in")
      print("Press 1 = sign up / Press 2 = log in / Press 3 = exit")
      logorsign = input()
      if logorsign == "1":  
        print("Awesome!Please enter your preffered username.")
        username = input()
        print("Enter a preffered password.")
        password1 = getpass.getpass("password:")
        print("Confirm your password please.")
        password2 = getpass.getpass("password:")
        if password1 == password2:
          print("New user: " + username + " created.")
          print("*****Choose log in this time.*****")
          save_user(create_user(username,password1)) 
          Galaano1()
        else:
          print("Sorry passwords don't match.")  
          Galaano1()
      elif logorsign == "2":
        print("Enter your username.")
        username = input()
        print("Enter your password.")
        password3 = getpass.getpass("password:") 
        if check_existing_user(password3):
          search_account = find_account(password3)
          if True:
            print(f"welcome  {search_account.username}")
            print("Press 1 = New credential. / Press 2 = View existing credentials / Press 3 = Delete credentials.")
            legacy = input()
            if legacy == "1":
              print("Enter account name.")
              account_name = input()
              print("Press 1 = Generate a password / Press 2 = To make your own password.")
              passwrd = input()
              if passwrd == "1":
                letters = string.ascii_letters + string.digits
                genpassword = ''.join(random.choice(letters) for i in range(9))
                print(f"Your new generated password is: {genpassword}") 
                password = genpassword 
                print(f"{account_name} has been successfully saved") 
                Galaano1()
              elif passwrd == "2":
                print("Enter account password.")
                password = getpass.getpass("password:") 
                print(f"{account_name} +  has been successfully saved")
                Galaano1()
                save_credentials(create_credentials(account_name,password))
            elif legacy == "2":
              if display_credentials:
                print("Here is a list of all your accounts and passwords")
                for Credentials in display_credentials():
                  print(f"Account name: {Credentials.account_name}  // password: {Credentials.password}")
              elif legacy == "3":
                print("Which credential would you like to delete?")
                delaccount = input()
                if delaccount == account_name:
                  Credentials.credentials_list.remove(Credentials)
                  print("Credential deleted")
                  Galaano1()
                else:
                  print("No match of such a credential")
                  Galaano1()   
        else:
          print("Incorrect username or password.Try again.")   
          Galaano1()
      elif logorsign == "3":
        exit()
    else:
      print("Are you that stupid.Please press 1")  
      Galaano1()
  elif answer == "no":
    print("Thanks for using our application.we hope to see you again.")
  else:
    print("Invalid choice.Try again.")  
    Galaano1()

if __name__ == '__main__':
  Galaano()
  Galaano1()
