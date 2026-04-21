def add_record(records, record):
    records.append(record)
    
def view_records(records):
    return records

def update_record(records, record_id, new_name, new_value):
    for record in records:
        if record["id"] == record_id:
            record["name"] = new_name
            record["value"] = new_value
            return True
    return False 

def delete_record(records, record_id):
    for record in records:
        if record["id"] == record_id:
            records.remove(record)
            return True
    return False