#This file will need to use the DataManager,
# FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager


## Funciona obtiene los datos del csv

question_data = DataManager().data_dict()

"""question_data:  [{'IATA': 'GDL', 'City': 'Guadalajara', 'Price': '20'}, 
{'IATA': 'ACA', 'City': 'Acapulco', 'Price': '33'}, 
{'IATA': 'VER', 'City': 'Veracruz', 'Price': '34'}, 
{'IATA': 'CUN', 'City': 'CancÃºn', 'Price': '34'}, 
{'IATA': 'OAX', 'City': 'Oaxaca', 'Price': '33'}, 
{'IATA': 'ZIH', 'City': 'Ixtapa', 'Price': '34'}, 
{'IATA': 'MAD', 'City': 'Madrid', 'Price': '262'}, 
{'IATA': 'FRA', 'City': 'Frankfurt', 'Price': '308'}, 
{'IATA': 'GRU', 'City': 'Brasil', 'Price': '232'}, 
{'IATA': 'CDG', 'City': 'Paris', 'Price': '338'}, 
{'IATA': 'SXF', 'City': 'Berlin', 'Price': '42'}, 
{'IATA': 'STR', 'City': 'stuttgart', 'Price': '331'}]"""


iata_list = [iata['IATA'] for iata in question_data]
# price_list = [iata['Lowest Price'] for iata in answer_data]
response_list = []

## Funciona, obtengo los datos en forma de dict de parámetros

for question in question_data:

    question_iata = question['IATA']
    question_city = question['City']
    question_price = question['Price']

    param = FlightData().get_data(question_iata)
    response_data = FlightSearch().get_data(param)
    response_list.append(response_data)


""" Response_list:  [{'City': 'GDL', 'Price': 19}, {'City': 'ACA', 'Price': 34}, {'City': 'VER', 'Price': 34}, 
{'City': 'CUN', 'Price': 34}, {'City': 'OAX', 'Price': 34}, {'City': 'ZIH', 'Price': 34}, {'City': 'MAD', 'Price': 268}, 
{'City': 'FRA', 'Price': 312}, {'City': 'SAO', 'Price': 205}, {'City': 'PAR', 'Price': 310}, 
{'City': 'TEST', 'Price': 9999}, {'City': 'STR', 'Price': 320}]"""


for flight in question_data:
    actual_price = flight['Price']
    actual_iata = flight['IATA']

    ## Obtener el precio de respuesta

    response_price = [item['Price'] for item in response_list if item['City'] == flight['IATA']]
    Outbound_Date = [item['Outbound'] for item in response_list if item['City'] == flight['IATA']]
    Inbound_Date = [item['Inbound'] for item in response_list if item['City'] == flight['IATA']]
    try:

        manager = NotificationManager()
        if manager.check_price(question_price=actual_price, actual_price=response_price[0]):
            manager.send_message(destiny=flight['IATA'], response_price=response_price[0],
                                 Outbound_Date=Outbound_Date[0], Inbound_Date=Inbound_Date[0])

        else:
            print("Price over the look")

    except IndexError:
        print("No more elements")

