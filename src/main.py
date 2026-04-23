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



    def handle_add_record():
        name = input("Enter Name: ")
        price = input("Enter Price: ")
        quantity = input("Enter Quantity: ")
        category = input("Enter Category: ")
        brand = input("Enter Brand: ")
        status = input("Enter Status: ")

        if name.strip() == "":
            print("Name cannot be empty. Please enter a valid name.")

        elif is_valid_number(price) and is_valid_number(quantity):
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
                create_new_record(
                    record_id,
                    name,
                    float(price),
                    int(quantity),
                    category,
                    brand,
                    status
                )
                print("Record added successfully.")

        else:
            print("Invalid price or quantity.")




    if choice == "1":
        handle_add_record()




    elif choice == "2":
        record_list = get_all_record_list()

        if not record_list:
            print("No records found.")
        else:
            print("\nID | NAME | PRICE | QTY | CATEGORY | BRAND | STATUS")
            print("----------------------------------------------------")

            for record_item in record_list:
                print(
                    f'{record_item["id"]} | '
                    f'{record_item["name"]} | '
                    f'{record_item["price"]} | '
                    f'{record_item["quantity"]} | '
                    f'{record_item["category"]} | '
                    f'{record_item["brand"]} | '
                    f'{record_item["status"]}'
                )




    elif choice == "3":
        record_id = input("Enter record ID to update: ")
        new_name = input("Enter new Name: ")
        new_price = input("Enter new Price: ")
        new_quantity = input("Enter new Quantity: ")
        new_category = input("Enter new Category: ")
        new_brand = input("Enter new Brand: ")
        new_status = input("Enter new Status: ")

        if is_valid_number(record_id) and is_valid_number(new_price) and is_valid_number(new_quantity):
            updated = edit_record(
                int(record_id),
                new_name,
                float(new_price),
                int(new_quantity),
                new_category,
                new_brand,
                new_status
            )

            if updated:
                print("Record updated successfully.")
            else:
                print("Record not found. Please check the ID and try again.")
        else:
            print("Invalid input.")




    elif choice == "4":
        record_id = input("Enter record ID to delete: ")

        if is_valid_number(record_id):
            confirm = input("Are you sure you want to delete? (Y/n): ")

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
                print("Delete cancelled.")

        else:
            print("Invalid ID. Please enter a valid number.")




    elif choice == "5":
        record_id = input("Enter record ID to search: ")

        if is_valid_number(record_id):
            record_list = get_all_record_list()
            found = False

            for record_item in record_list:
                if record_item["id"] == int(record_id):
                    print("\nID | NAME | PRICE | QTY | CATEGORY | BRAND | STATUS")
                    print("----------------------------------------------------")
                    print(
                        f'{record_item["id"]} | '
                        f'{record_item["name"]} | '
                        f'{record_item["price"]} | '
                        f'{record_item["quantity"]} | '
                        f'{record_item["category"]} | '
                        f'{record_item["brand"]} | '
                        f'{record_item["status"]}'
                    )
                    found = True
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

            print("\nID | NAME | PRICE | QTY | CATEGORY | BRAND | STATUS")
            print("----------------------------------------------------")

            for record_item in record_list:
                if record_item["name"].lower() == search_name.lower():
                    print(
                        f'{record_item["id"]} | '
                        f'{record_item["name"]} | '
                        f'{record_item["price"]} | '
                        f'{record_item["quantity"]} | '
                        f'{record_item["category"]} | '
                        f'{record_item["brand"]} | '
                        f'{record_item["status"]}'
                    )
                    found = True

            if not found:
                print("No records found with the given name. Please check the name and try again.")




    elif choice == "7":
        print("Going to Exit the system....")
        break

    else:
        print("Invalid choice. Please Choose 1-7.")
