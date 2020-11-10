# Task
![](images/taskinfo.png)

**Explanation**
- Here we want to be able to read from a ```.json``` file and pinpoint values we want

- We need to import the ```json``` module to be able to import json files and turn them into dictionaries:

```python
import json

class Currency:
    def __init__(self):
        self.exchange_rates = self.create_dic()
        self.display_all_data()
        input("\nPress enter to show the rates")
        self.display_rates()

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

Currency() 
```
