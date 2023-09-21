import requests
import configuration
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

def get_order_by_number(order_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_NUMBER_PATH + '?t=' + str(order_number))