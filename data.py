import datetime

current_date = datetime.date.today()
future_date = current_date + datetime.timedelta(days=1)

headers = {
    "Content-Type": "application/json"
}

create_order_body = {
    "firstName": "Алекс",
    "lastName": "Петров",
    "address": "Невский",
    "metroStation": 3,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": str(future_date),
    "comment": "Привет",
    "color": [
        "BLACK"
    ]
}
