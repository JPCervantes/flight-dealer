import datetime
from data_manager import DataManager
from pprint import pprint

dt = datetime.datetime.now()
DATE_FROM = dt.strftime("%d/%m/%Y")
subject_date = int(DATE_FROM[3:5]) + 6
DATE_TO = dt.strftime(f"%d/{subject_date}/%Y")

DEPARTURE = "MEX"

if DATE_FROM[3] == "0":
    DATE_TO = dt.strftime(f"%d/0{subject_date}/%Y")

elif int(DATE_TO[3:4]) >= 13:
    month = int(DATE_TO[3:4])
    new_month = month - 12
    DATE_TO = dt.strftime(f"%d/0{subject_date}/%Y")


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.flight_data = []

    def get_data(self, iata):

        self.FLIGHT_PARAMS = {
            "fly_from": DEPARTURE,
            "fly_to": iata,
            "dateFrom": DATE_FROM,
            "dateTo": DATE_TO,
            "curr": "MXN"
        }

        return self.FLIGHT_PARAMS

    # def __str__(self):
    #     data_print = str(self.FLIGHT_PARAMS)
    #     return data_print



