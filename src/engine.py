from storage import load_data, save_data
from models import create_record
from operations import add_record, view_records, update_record, delete_record

records = load_data()

def create_new_record(record_id, name, value):
    record =  create_record(record_id, name, value)
    add_record(records, record)
    save_data(records)

def get_all_records():
    return view_records(records)

def edit_record(record_id, new_name, new_value):
    updated = update_record(records, record_id, new_name, new_value)

    if updated:
        save_data(records)
    return updated

def remove_record(record_id):
    deleted = delete_record(records, record_id)

    if deleted:
        save_data(records)
    return deleted