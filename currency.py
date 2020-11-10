import json

class Currency:
    def __init__(self):
        self.exchange_rates = self.create_dic()

    # This opens the required json file and stores it as an attribute
    # By default, we are returned a dictionary    
    def create_dic(self):
        with open("exchange_rate.json", "r") as er:
            dic = json.load(er)
        return dic

    # Iterates through the json file and outputs the key, val pairs
    def display_all_data(self):
        for key, value in self.exchange_rates.items():
            print(f"{key} : {value}")

    # Iterates through the rates dictionary and shows rate by country
    def display_rates(self):
        for key, value in self.exchange_rates["rates"].items():
            print(f"{key} : {value}")  
