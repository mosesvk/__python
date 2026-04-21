import requests

class Client(object): 
    def __init__(self, url: str): 
        self.url = url

    def get(self): 
        res = requests.get(self.url)
        return res.json()

if __name__ == '__main__': 
    import json
    client = Client(
        'https://api.met.no/weatherapi/airqualityforecast/0.1/stations'
    )
    data = client.get()
    print(json.dumps(data[:3], indent=2))