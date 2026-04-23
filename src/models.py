from datetime import datetime

def create_record(record_id, name, value):
    return{
        "id": record_id,
        "name": name,
        "value": value,
        "created_at": datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    }