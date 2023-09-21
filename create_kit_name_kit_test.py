import data
import sender_stand_request

def get_new_order_number():
    return sender_stand_request.post_new_order(data.create_order_body).json()['track']


def test_get_order_by_number_get_success_response():
    response = sender_stand_request.get_order_by_number(get_new_order_number())
    assert response.status_code == 200, "Status code is not 200"

