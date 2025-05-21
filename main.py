import json
from multiprocessing import Value
import os
from src.create_save import database_init
from src.read_write_save import read_json, write_json
from src.contact_function import add_contact, browse_contact, delete_contact, edit_contact


def intro():
    print("#################################################################")
    print("############### Welcome to the Yellow Pages Program #############")
    print("#################################################################")
    print("Made by Hutomo Putra Kurniawan as the part of Project Based Study")

    
def main_menu():
    print("1. Add contact")
    print("2. Browse contact")
    print("3. Edit contact")
    print("4. Delete contact")
    print("5. Exit program")
    user_option = int(input("Choose which option:"))
    try:
        match user_option:
            case 1:
               add_contact(data)
               print("Back to main menu")
            case 2:
                browse_contact(data)
                print("Back to main menu")
            case 3:
                edit_contact(data)
                print("Back to main menu")
            case 4:
               delete_contact(data)
               print("Back to main menu")
            case 5:
                exit_program(data)
            case _:
                raise IndexError(f"Option {user_option} is not exist!")
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

def exit_program(data):
    exit_option = input("Exit program? [Y/n]")
    if exit_option == 'Y':
        save_status = input("Save changes? [Y/n]")
        if save_status == 'Y':
            write_json('database.json',data)
            print("Exiting program...")
            exit()
        elif save_status == 'n':
            print("Exiting program...")
            exit()
        else:
            raise ValueError("Invalid input. Input (Y)es or (no)")   
    elif exit_option == 'n':
        print("Cancelled exit")
    else:
        raise ValueError("Invalid input. Input (Y)es or (no)") 

if __name__ == '__main__':
    
    
    database_init()
    data = read_json('database.json')
    
    intro()
    while True:
        main_menu()
    
