import json

class Currency:
    def __init__(self):
        self.exchange_rates = self.create_dic()
        self.currency = self.exchange_rates["rates"].keys()
        while True:
            print("""
                    1. Exchange two currencies
                    2. Display all data from .json file
                    3. Display exchange rate by country
                    4. EXIT""")
            choice = input("-->  ").strip()

            if choice == "1":
                self.exchange_menu()

            if choice == "2":
                self.display_all_data()

            if choice == "3":
                self.display_rates()

            if choice == "4":
                break

            else:
                continue

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

    # Converts currency1 to currency2
    def convert(self, c1, c2):
        currency1 = self.exchange_rates["rates"][c1]
        currency2 = self.exchange_rates["rates"][c2]
        print(f"1 {c1} = {currency2/currency1} {c2}")

    # Asks input from user and returns the current exchange rate
    def exchange_menu(self):
        print(self.currency)
        while True:
            c_from = input("\nInput a currency to exchange from:  ").upper()
            if not self.check_if_valid(c_from):
                continue
            c_to = input("Input a currency to exchange to:  ").upper()
            if not self.check_if_valid(c_to):
                continue
            self.convert(c_from, c_to)
            choice = input("\nDo you want to exchange again? (Y/N) \n--> ").upper().strip()
            if choice == "Y":
                continue
            if choice == "N":
                break
            else:
                print("Unknown command, please input Y or N only")
                print("Exchanging again...")
                continue

    # Checks if the currency is supported
    def check_if_valid(self, value):
        if value not in self.currency:
            return False
        return True


Currency()
