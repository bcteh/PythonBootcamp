# MongoDB ID: bcteh8_db_user , password: Z9SscDUMpIMEnhn2
# MONGO DB connection string: mongodb+srv://bcteh8_db_user:Z9SscDUMpIMEnhn2@cluster0.5eyq41q.mongodb.net/
from xmlrpc import client

from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
from bson.errors import InvalidId
from dotenv import load_dotenv
import os
load_dotenv()

# Connect to MongoDB
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["mydatabase"]
users_collection = db["users"]

# CRUD operations for users with loginid as unique field.
# createa menu for CRUD operations for users, with options to create, read, update, delete users based on loginid.
# The menu should be displayed in a loop until the user chooses to exit.
def display_menu():
    print("1. Create User")
    print("2. Get User by LoginID")
    print("3. Update User")
    print("4. Get All Users")
    print("5. Delete User")
    print("6. Exit")

# update insert base on loginid, if loginid exists, update the document, if not, insert a new document.
# The update should only update the fields that are provided, if a field is not provided, it should not be updated.
# delete document based on loginid, if loginid does not exist, print error message. 
def create_user(loginid, name, age, email):
    result = users_collection.update_one(
        {"loginid": loginid},
        {"$set": {"name": name, "age": age, "email": email}},
        upsert=True
    )
    if result.matched_count > 0:
        print(f"User with loginid '{loginid}' updated.")
    else:
        print(f"User with loginid '{loginid}' created.")    

# update user based on loginid, if loginid does not exist, print error message.
def update_user(loginid, name=None, age=None, email=None):
    update_data = {}
    if name:
        update_data["name"] = name
    if age:
        update_data["age"] = age
    if email:
        update_data["email"] = email

    if not update_data:
        print("No fields to update.")
        return

    result = users_collection.update_one(
        {"loginid": loginid},
        {"$set": update_data}
    )
    if result.matched_count > 0:
        print(f"User with loginid '{loginid}' updated.")
    else:
        print(f"User with loginid '{loginid}' not found.")

        
def delete_user(loginid):
    result = users_collection.delete_one({"loginid": loginid})
    if result.deleted_count > 0:
        print(f"User with loginid '{loginid}' deleted.")
    else:
        print(f"User with loginid '{loginid}' not found.")
def get_user(loginid):
    user = users_collection.find_one({"loginid": loginid})
    if user:
        print(f"User found: {user}")
    else:
        print(f"User with loginid '{loginid}' not found.")  
def get_all_users():
    users = list(users_collection.find())
    if not users:
        print("No users found.")
        return
    print(f"\n{'='*80}")
    print(f"Total Users: {len(users)}")
    print(f"{'='*80}")
    for idx, user in enumerate(users, 1):
        print(f"\nUser {idx}:")
        for key, value in user.items():
            print(f"  {key}: {value}")
    print(f"{'='*80}\n")
        
#close the MongoDaaaB connection when done
def close_connection():
    client.close()

# Main loop to display the menu and handle user input
while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        loginid = input("Enter loginid: ")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        email = input("Enter email: ")
        create_user(loginid, name, age, email)
    elif choice == '2':
        loginid = input("Enter loginid to get user: ")
        get_user(loginid)
    elif choice == '3':
        loginid = input("Enter loginid to update user: ")
        name = input("Enter new name (or press Enter to keep current): ")
        age = input("Enter new age (or press Enter to keep current): ")
        email = input("Enter new email (or press Enter to keep current): ")

        # Prepare the update data
        update_data = {}
        if name:
            update_data["name"] = name
        if age:
            update_data["age"] = int(age)
        if email:
            update_data["email"] = email

        # Update the user
        update_user(loginid, **update_data)

    elif choice == '4':
        get_all_users()
    elif choice == '5':
        loginid = input("Enter loginid to delete user: ")
        delete_user(loginid)
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")

close_connection()
