from email_validator import validate_email, EmailNotValidError

def email_input_check(e_mail):
    try:
        validate_email(e_mail)
        return True
    except EmailNotValidError as error:
        return False   

def add_contact(data):
    while True:
        name = input("Input full name: ")
        if name in data:
            print("Name already exists. Back to main menu")
            break    
        phone_num = input("Input phone number: ")
        e_mail = input("Input e-mail: ")
        
        # This is e-mail check block
        if email_input_check(e_mail) == True:
            print("Valid e-mail...")
        else:
            print("Invalid e-mail!")
            break
        
        street = input("Input street name: ")
        city = input("Input city/town: ")
        state = input("Input state/province: ")
        country = input("Input country: ")
        zipcode = input("Input zip code: ")
        address = {"Street":street,"City":city,"State":state,"Country":country,"Zip code":zipcode}
        data[name]= {"Name":name,"Phone Number":phone_num,"E-mail":e_mail,"Address":address}
        print(f"Data for {name} added successfully!")

def browse_contact(data):
    for idx, name in enumerate(data.keys(), start=1):
        print(f"{idx}. {name}")   
    contact_index = list(data.keys())
    try:
        access_index = int(input("Input which contact you want to browse: ")) - 1  
        if access_index < 0 or access_index >= len(contact_index):
            raise IndexError("Index out of range. Put number according to available index.")
        else:
            contact_name = contact_index[access_index]
            print("------------------------------------------")
            print(f"Full Name: {data[contact_name]["Name"]}")
            print(f"Phone Number: {data[contact_name]["Phone Number"]}")
            print(f"E-mail: {data[contact_name]["E-mail"]}")
            print("Address:")
            for key,value in data[contact_name]["Address"].items():
                print(f"    {key}: {value}")
            print("------------------------------------------")
    except ValueError:
        print("Please put integer.")
        
    
def edit_contact(data):
    for idx, name in enumerate(data.keys(), start=1):
        print(f"{idx}. {name}")
    contact_index = list(data.keys())
    try:
        user_input_edit = int(input("Input which contact do you want to edit")) - 1
        if user_input_edit < 0 or user_input_edit >= len(contact_index):
            raise IndexError("Index out of range. Please put number according to available index.")
        else:
            while True:
                contact_name = contact_index[user_input_edit]
                print(f"You want to edit {contact_name}")
                print("1.Contact name")
                print("2. Phone number")
                print("3. E-mail")
                print("4. Address")
                print("5. Finish editing")
                user_edit_choice = int(input("From the option above, which entry do you want to edit:"))
                match user_edit_choice:
                    case 1:
                        new_name = input("New name: ")
                        data[new_name] = data.pop(contact_name)
                        data[new_name]["Name"] = new_name
                    case 2:
                        data[contact_name]["Phone Number"] = input("New phone number: ")
                    case 3:
                        data[contact_name]["E-mail"] = input("Input new e-mail address: ")
                    case 4:
                        print("1. Street")
                        print("2. City")
                        print("3. State")
                        print("4. Country")
                        print("5. Zip code")
                        address_detail_edit = int(input("What entry do you want to edit?"))
                        match address_detail_edit:
                            case 1:
                                data[contact_name]["Address"]["Street"] = input("New street: ")
                            case 2:
                                data[contact_name]["Address"]["City"] = input("New city: ")
                            case 3:
                                data[contact_name]["Address"]["State"] = input("New state: ")
                            case 4:
                                data[contact_name]["Address"]["Country"] = input("New country: ")
                            case 5:
                                data[contact_name]["Address"]["Zip code"] = input("New zip code: ")
                            case _:
                                raise ValueError("Unknown option for entry")
                    case 5:
                        print("Finished editing")
                        break
                    case _:
                        raise ValueError("Unknown option for entry")            
    except ValueError:
        raise ValueError("Please put proper number/integer")


def delete_contact(data):
    for idx, contact_name in enumerate(data,start=1):
        print(f"{idx}. {contact_name}")
    contact_index = list(data.keys())
    try:
        user_input_delete = int(input("Input which contact do you want to delete? ")) - 1
        if user_input_delete < 0 or user_input_delete >= len(contact_index):
            raise IndexError("Index out of range. Please put number according to available index.")
        else:
            contact_name = contact_index[user_input_delete]
            print(f"You want to edit {contact_name}")
            print(f"Deleting '{contact_name}'...")
            del data[contact_name]
            print(f"Contact '{contact_name}' has been deleted.")
    except ValueError:
        raise ValueError("Please put proper number/integer")
    
