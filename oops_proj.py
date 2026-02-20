class chatbook:
    def __init__(self):
        self.usrname=''
        self.loggedin= False
        self.passkey=''     
        self.menu()

    def menu (self):
        user_input=input(''''Welcome, give your response:
                         1. To signup
                         2. To Signin
                         3. To post something
                         4. To message
                         5. Any key to exit \n ->''')
        
        if user_input == '1':
            self.signup()
        elif user_input=='2':
            self.signin()
        elif user_input == '3':
            pass
        elif user_input== '4':
            pass
        else:
            exit()

    def signup(self):
        email=input("setup your mail id ")
        password=input("setup your password ")
        self.usrname= email
        self.passkey= password
        print("Sign Up successful \n")
        self.menu()

    def signin(self):
        if self.usrname=='' and self.passkey=='':
            print("Please Signup first! \n")
        else:
            uname=input("enter your registered email ID here ") 
            pwd=input("enter your password here ")
            if self.usrname==uname and self.passkey==pwd :
                print("User signin successful")
            else:
                print("Invalid credentials")
        self.menu()

object1= chatbook()
