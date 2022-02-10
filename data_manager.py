import requests
import os
import csv
from pprint import pprint

SHEETY_BAREAR_KEY = os.environ.get("SHEETY_BAREAR_KEY")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_HEADERS = {"Authorization":f"Bearer {SHEETY_BAREAR_KEY}"}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # with requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS) as self.data:
        #     data = self.data.json()
        #     print(data)
        #     self.response = data["hoja1"]
        #
        #     self.iata_list = [v["iataCode"] for v in self.response]
        #     self.destinies_list = [v["city"] for v in self.response]
        #     self.prices_list = [v["lowestPrice"] for v in self.response]
            self.iata_list = []
            self.destinies_list = []
            self.prices_list = []
            self.data_search_list = []


    def data_dict(self):
        self.data_dict = {}
        self.data_list = []
        with open("data.csv") as self.data:
            data = csv.DictReader(self.data)

            for row in data:
                self.iata_list.append(row['IATA Code'])
                self.destinies_list.append(row["City"])
                self.prices_list.append(row["Lowest Price"])
                self.data_dict["IATA"] = row['IATA Code']
                self.data_dict["City"] = row['City']
                self.data_dict["Price"] = row['Lowest Price']
                self.data_search_list = {
                    "IATA": row['IATA Code'],
                    "City": row['City'],
                    "Price": row['Lowest Price']}
                self.data_list.append(self.data_search_list)

        return self.data_list



                # print(self.data_dict)
                # print("Lista IATA: ", self.iata_list)
                # print("Lista destinos: ", self.destinies_list)
                # print("Lista precios: ", self.prices_list)





