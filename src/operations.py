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