from storage import load_data, save_data
from models import create_record

record_list = load_data()


def add_record(record_list, record_item):
    record_list.append(record_item)
    
def view_record_list(record_list):
    return record_list

def update_record(record_list, record_id, new_name, new_value):
    for record_item in record_list:
        if record_item["id"] == record_id:
            record_item["name"] = new_name
            record_item["value"] = new_value
            return True
    return False

def delete_record(record_list, record_id):
    for record_item in record_list:
        if record_item["id"] == record_id:
            record_list.remove(record_item)
            return True
    return False



def create_new_record(record_id, name, value):
    record_item =  create_record(record_id, name, value)
    add_record(record_list, record_item)
    save_data(record_list)

def get_all_record_list():
    return view_record_list(record_list)

def edit_record(record_id, new_name, new_value):
    updated = update_record(record_list, record_id, new_name, new_value)

    if updated:
        save_data(record_list)
    return updated

def remove_record(record_id):
    deleted = delete_record(record_list, record_id)

    if deleted:
        save_data(record_list)
    return deleted
