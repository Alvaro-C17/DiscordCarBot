import requests

class CarQuery:
    def __init__(self):
        self.url = "https://www.carqueryapi.com/api/0.3"

    def get_cars(self, make, model):
        endpoint = f"{self.url}/?cmd=getTrims&make={make}&model={model}"
        response = requests.get(endpoint)
        data = response.json()
        cars = []
        for trim in data["Trims"]:
            car = {
                "make": trim["model_make_id"],
                "model": trim["model_name"],
                "year": trim["model_year"],
                "trim": trim["model_trim"],
                "id": trim["model_id"]
            }
            cars.append(car)
        return cars
