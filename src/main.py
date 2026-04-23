from engine import create_new_record, get_all_record_list, edit_record, remove_record
from utils import generate_id, is_valid_number

while True:
    print("\n========================")
    print("  LOCAL STORAGE ENGINE")
    print("========================")
    print("1. Add Record")
    print("2. View Records")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Search by ID")
    print("6. Search by Name")
    print("7. Exit")
    print("------------------------")


    choice = input("Enter Choice: ")




    if choice == "1":
        name = input("Enter Name: ")
        value = input("Enter Value: ")

        if name.strip() == "":
            print("Name cannot be empty. Please enter a valid name.")

        elif is_valid_number(value):
            record_list = get_all_record_list()
            record_id = generate_id(record_list)

            duplicate_found = False

            for record_item in record_list:
                if record_item["id"] == record_id:
                    duplicate_found = True
                    break

            if duplicate_found:
                print("Duplicate ID found. Record not added. Please try again.")
            else:
                create_new_record(record_id, name, int(value))
                print("Record added successfully.")
        
        else:
            print("Invalid value. Please enter a valid number.")




    elif choice == "2":
        record_list = get_all_record_list()

        if not record_list:
            print("No records found.")
        else:
            print("\nID | NAME | VALUE")
            print("--------------------")

            for record_item in record_list:
                print(f'{record_item["id"]} | {record_item["name"]} | {record_item["value"]}')




    elif choice == "3":
        record_id = input("Enter record ID to update: ")
        new_name = input("Enter new name to update: ")
        new_value = input("Enter new value to update: ")

        if is_valid_number(record_id) and is_valid_number(new_value):
            updated = edit_record(int(record_id), new_name, int(new_value))

            if updated:
                print("Record updated successfully.")
            else:
                print("Record not found. Please check the ID and try again.")
        else:
            print("Invalid ID or value. Please enter valid numbers.")




    elif choice == "4":
        record_id  = input("Enter record ID to delete: ")
        
        if is_valid_number(record_id):
            confirm = input("Are you sure you want to delete? (Y/n):")
            while confirm != "Y" and confirm != "n":
                print("Invalid option. Please enter Y or n.")
                confirm = input("Are you sure you want to delete? (Y/n): ")

            if confirm == "Y":
                deleted = remove_record(int(record_id))

                if deleted:
                    print("Record deleted.")
                else:
                    print("Record not found to delete. Please check the ID and try again.")
            else:
                print("Invalid ID. Please enter a valid number.")

 


    elif choice == "5":
        record_id =  input("Enter record ID to search: ")

        if is_valid_number(record_id):
            record_list = get_all_record_list()
            found = False

            for record_item in record_list:
                if record_item["id"] == int(record_id):
                    print("\nID | NAME | VALUE")
                    print("----------------------")
                    print(f'{record_item["id"]} | {record_item["name"]} | {record_item["value"]}')
                    found =True
                    break

            if not found:
                print("Record not found. Please check the ID and try again.")
            else:
                print("Invalid ID. Please enter a valid number.")




    elif choice == "6":
        search_name = input("Enter name: ").strip()

        if search_name == "":
            print("Name cannot be empty. Please enter a valid name.")
        else:
            record_list = get_all_record_list()
            found = False

            print("\nID | NAME | VALUE")
            print("--------------------")

            for record_item in record_list:
                if record_item["name"].lower() == search_name.lower():
                    print(f'{record_item["id"]} | {record_item["name"]} | {record_item["value"]}')
                    found =True

            if not found:
                print("No records found with the given name. Please check the name and try again.")



    elif choice == "7":
        print("Going to Exit the system....")
        break

    else:
        print("Invalid choice. Please Choose 1-7.")
        