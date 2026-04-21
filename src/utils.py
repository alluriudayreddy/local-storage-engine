def generate_id(records):
    if not records:
        return 1
    return records[-1]["id"] + 1

def is_valud_number(value):
    try:
        int(value)
        return True
    except:
        return False