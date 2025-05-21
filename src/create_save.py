import json
import os

def database_init():
    print("Checking if database exist...")
    if not os.path.exists('database.json'):
        print("Database not found")
        print("Creating new database...")
        print(f"Current working directory: {os.getcwd()}")
        try:
            with open('database.json', 'w') as file:
                json.dump({}, file, indent=4)
            print("Database created successfully!")
        except Exception as error:
            print(f"Error creating database: {error}")
    else:
        print("Database exist")
        print("Loading database...")