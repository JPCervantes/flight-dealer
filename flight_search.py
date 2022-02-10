import os
import requests
from flight_data import FlightData
from data_manager import DataManager
from pprint import pprint

TEQUILA_APP_KEY = os.environ.get("TEQUILA_APP_KEY")
TEQUILA_ID = os.environ.get("TEQUILA_ID")
TEQUILA_ENDPOINT = os.environ.get("TEQUILA_ENDPOINT")

headers = {
    "apikey": TEQUILA_APP_KEY,
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    ''' Search for data in Tequila APIv '''

    def __init__(self):
        list_params = []

        self.destinies = DataManager().destinies_list
        self.prices = DataManager().prices_list
        self.iatas = DataManager().iata_list
        self.actual_dict_city_price = {}

    def get_data(self, param):
        price_list = []

        with requests.get(url=TEQUILA_ENDPOINT, params=param, headers=headers) as self.flight_data:
            self.response = self.flight_data
            self.response_data = self.response.json()['data']
            data_length = len(self.response_data) - 1

            # pprint(self.response_data[0:data_length])

            try:
                price_list.append(self.response_data[0]['price'])
                self.actual_dict_city_price['City'] = self.response_data[0]['cityCodeTo']
                self.actual_dict_city_price['Price'] = min(price_list)
                self.actual_dict_city_price['Outbound'] = self.response_data[0]['local_departure'][0:10]
                self.actual_dict_city_price['Inbound']= self.response_data[1]['local_arrival'][0:10]
                # self.actual_dict_city_price[self.response_data[0]['cityCodeTo']] = min(price_list)
            except IndexError:
                self.actual_dict_city_price['City'] = 'VUELO NO ENCONTRADO'
                self.actual_dict_city_price['Price'] = None
                # self.actual_dict_city_price[self.response_data[0]['cityCodeTo']] = min(price_list)

                    # self.actual_dict_city_price.popitem()
                    # print("last item on dict removed")

        return self.actual_dict_city_price

