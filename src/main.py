from engine import create_new_record, get_all_records, edit_record, remove_record
from utils import generate_id, is_valid_number

while True:
    print("\n1. Add Record")
    print("2. View Records")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        value = input("Enter Value: ")

        if is_valid_number(value):
            record_id = generate_id(get_all_records())
            create_new_record(record_id, name, int(value))
            print("Record added.")
        else:
            print("Invalid value.")
    
    elif choice == "2":
        records = get_all_records()

        if not records:
            print("No records found.")
        else:
            for record in records:
                print(record)

    elif choice == "3":
        record_id = input("Enter record ID to update: ")
        new_name = input("Enter new name: ")
        new_value = input("Enter new value: ")

        if is_valid_number(record_id) and is_valid_number(new_value):
            updated = edit_record(int(record_id), new_name, int(new_value))

            if updated:
                print("Record updated.")
            else:
                print("Record not found.")
        else:
            print("Invalid input.")

    elif choice == "4":
        record_id  = input("Enter record ID to delete: ")
        
        if is_valid_number(record_id):
            deleted = remove_record(int(record_id))

            if deleted:
                print("Record deleted.")
            else:
                print("Record not found.")
        else:
            print("Invalid id.")

    elif choice == "5":
        print("Existing....")
        break

    else:
        print("Invalid choice.")