def generate_id(record_list):
    if not record_list:
        return 1
    else:
        return record_list[-1]["id"]+1
    
def is_valid_number(value):
    try:
        int(value)
        return True
    except:
        return False
        