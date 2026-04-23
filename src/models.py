from datetime import datetime

def create_record(record_id, name, price, quantity, category, brand, status):
    return{
        "id": record_id,
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category,
        "brand": brand,
        "status": status,
        "created_at": datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    }