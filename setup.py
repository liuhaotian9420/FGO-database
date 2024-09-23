# from pymongo import MongoClient

# # Step 1: Connect to the MongoDB server (admin database)
# client = MongoClient('mongodb://118.195.250.136:27017/')  # Adjust the URI as needed
# admin_db = client['fgo']  # Replace 'fgo' with your desired database name

# # Step 2: Define the user details
# username = 'haotian'
# password = 'dick920815'
# roles = [
#     {'role': 'readWrite', 'db': 'fgo'}  # Assign readWrite role on 'my_database'
# ]

# # Step 3: Create the user
# try:
#     admin_db.command("updateUser", username, pwd=password, roles=roles)
#     print(f"User '{username}' created successfully.")
# except Exception as e:
#     print(f"An error occurred: {e}")
