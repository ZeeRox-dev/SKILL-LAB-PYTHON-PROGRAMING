import os
# from django.conf.locale import da
import pandas as pd

class user:
    def __init__(self):
        string_to_show: str = 'Welcome User'
        print(string_to_show)
        self.name = None
        self.email = None
        self.phone = None
        self.password = None
        self.keys = ('name','email','phone','password')

    def register(self):
        self.name = input("Please enter your name: ")
        self.email = input("Please enter your eamil: ")
        self.phone = input("Please enter your phone: ")
        self.password = input("Please enter your password: ")
        data_to_write = {key: value for key, value in zip(self.keys, (self.name, self.email, self.phone, self.password))}
        df = pd.DataFrame( [ data_to_write ] )
        if not os.path.exists('users.csv'):
            df.to_csv('users.csv',header = list(self.keys), index = False, sep = ';')
        else:
            df.to_csv('users.csv',index = False, sep = ';', header = False, mode = 'a')
        # if os.path.isfile('users.csv'):
        #     pass
        # else:
        #     with open('users.csv','w',newline='') as csvfile:
        #         csvfile.write("name;email;phone;password\n")
        #         csvfile.write(f"{self.name};{self.email};{self.phone};{self.password}\n")
    @staticmethod
    def show_user_info():
        print(pd.read_csv('users.csv'), sep=';')

    def login_user(self):
        try:
            with open('user.csv','r') as csvfile:
                df = pd.read_csv(csvfile,sep=';')
                print(df)
        except FileNotFoundError:
            print("File not found")
        pass


user1 = user()
user1.register()
user1.show_user_info()

user2 = user()
user2.register()
user2.show_user_info()

# user1.login_user()


# l1 = [x for x in range(10)]


# try:
#     k = int(input("Enter a number: "))
#     print(l1[k])
# except ValueError:
#     print("Print Enter a number ")
# except IndexError:
#     print("Number is out of range")