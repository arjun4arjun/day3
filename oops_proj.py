class chatbook:
    def __init__(self):
        self.username=''
        self.loggedin= False
        self.password=''     
        self.menu()

    def menu (self):
        user_input=input(''''Welcome, give your response:
                         1. To signup
                         2. To Signin
                         3. To post something
                         4. To message
                         5. Any key to exit''')
        
        if user_input == '1':
            pass
        elif user_input=='2':
            pass
        elif user_input == '3':
            pass
        elif user_input== '4':
            pass
        else:
            exit()

object1= chatbook()
