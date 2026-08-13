# l1 = ('Name','Email','Password','age')
# l2 = ('Vikas','vk@31gmail.com','sfafa.3654','65')
# print(list(zip(l1,l2)))
# for x , y in zip(l1,l2):
#     print(x)
#     print(y)

import os
import pandas as pd

class user:
    def __init__(self):
        string_to_show: str = 'Welcome User'
        print(string_to_show)
        self.name = None
        self.email = None
        self.phone = None
        self.userID = None
        self.password = None
        self.keys = ('name','email','phone','userID','password')

    def register(self):
        self.name = input("Please enter your name: ")
        self.email = input("Please enter your eamil: ")
        self.phone = input("Please enter your phone: ")
        self.userID = input("Please enter your User ID: ")
        self.password = input("Please enter your password: ")
        data_to_write = {key: value for key, value in zip(self.keys, (self.name, self.email, self.phone, self.userID, self.password))}
        df = pd.DataFrame( [ data_to_write ] )
        if not os.path.exists('UserData.csv'):
            df.to_csv('UserData.csv', header=list(self.keys), index=False, sep=';')
        else:
            df.to_csv('UserData.csv', index=False, sep=';', header=False, mode='a')
        print("✅ Registration successful!")
    
    @staticmethod
    def show_user_info():
        try:
            # Fixed: Specify separator when reading
            df = pd.read_csv('UserData.csv', sep=';')
            print(df)
        except FileNotFoundError:
            print("No user data found.")
        except pd.errors.EmptyDataError:
            print("No user data found.")

    def login_user(self):
        try:
            # Read the CSV file with proper separator
            df = pd.read_csv('UserData.csv', sep=';')
            
            # Display login options
            print("\n===== LOGIN MENU =====")
            print("1. Login with Phone")
            print("2. Login with User ID")
            print("3. Login with Email ID")
            print("======================")
            
            # Get user choice
            choice = input("Please select login option (1/2/3): ")
            
            if choice == '1':
                # Login with Phone
                phone_input = input("Please enter your phone number: ").strip()
                
                # Check if phone exists
                if phone_input in df['phone'].astype(str).values:
                    # Get the row where phone matches
                    user_row = df[df['phone'].astype(str) == phone_input].iloc[0]
                    
                    # Ask for password
                    password_input = input("Please enter your password: ")
                    
                    # Check password
                    if password_input == str(user_row['password']).strip():
                        print(f"\n✅ Login Successful! Welcome {user_row['name']}!")
                        return True
                    else:
                        print("\n❌ Incorrect password! Please try again.")
                        return False
                else:
                    print("\n❌ Phone number not found! Please register first.")
                    return False
                    
            elif choice == '2':
                # Login with User ID
                user_id_input = input("Please enter your User ID: ").strip()
                
                # Check if user ID exists in the userID column
                if user_id_input in df['userID'].astype(str).values:
                    # Get the row where userID matches
                    user_row = df[df['userID'].astype(str) == user_id_input].iloc[0]
                    
                    # Ask for password
                    password_input = input("Please enter your password: ")
                    
                    # Check password
                    if password_input == str(user_row['password']).strip():
                        print(f"\n✅ Login Successful! Welcome {user_row['name']}!")
                        return True
                    else:
                        print("\n❌ Incorrect password! Please try again.")
                        return False
                else:
                    print("\n❌ User ID not found! Please register first.")
                    return False
                    
            elif choice == '3':
                # Login with Email ID
                email_input = input("Please enter your email ID: ").strip()
                
                # Check if email exists
                if email_input in df['email'].astype(str).values:
                    # Get the row where email matches
                    user_row = df[df['email'].astype(str) == email_input].iloc[0]
                    
                    # Ask for password
                    password_input = input("Please enter your password: ")
                    
                    # Check password
                    if password_input == str(user_row['password']).strip():
                        print(f"\n✅ Login Successful! Welcome {user_row['name']}!")
                        return True
                    else:
                        print("\n❌ Incorrect password! Please try again.")
                        return False
                else:
                    print("\n❌ Email ID not found! Please register first.")
                    return False
            else:
                print("\n❌ Invalid choice! Please select 1, 2, or 3.")
                return False
                
        except FileNotFoundError:
            print("\n❌ No users registered yet! Please register first.")
            return False
        except Exception as e:
            print(f"\n❌ An error occurred: {str(e)}")
            return False

# Test the implementation
if __name__ == "__main__":
    # Delete existing file for clean test (optional)
    # if os.path.exists('UserData.csv'):
    #     os.remove('UserData.csv')
    
    # Register two users for testing
    user1 = user()
    user1.register()
    user1.show_user_info()
    
    # user2 = user()
    # user2.register()
    # user2.show_user_info()
    
    # Test login functionality
    print("\n--- Login ---")
    test_login = user()
    test_login.login_user()

