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
    print("5. Exit")
    print("------------------------")


    choice = input("Enter Choice: ")




    if choice == "1":
        name = input("Enter Name: ")
        value = input("Enter Value: ")

        if is_valid_number(value):
            record_id = generate_id(get_all_record_list())
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
            deleted = remove_record(int(record_id))

            if deleted:
                print("Record deleted.")
            else:
                print("Record not found to delete. Please check the ID and try again.")
        else:
            print("Invalid ID. Please enter a valid number.")




    elif choice == "5":
        print("Going to Exit the system....")
        break

    else:
        print("Invalid choice. Choose 1-5.")
        