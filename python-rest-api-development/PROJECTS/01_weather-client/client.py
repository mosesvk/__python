import requests
import urllib3  

class Client(object): 
    def __init__(self, url: str, ssl_verify=True):
        self.url = url
        self.ssl_verify = ssl_verify
        if ssl_verify is False:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


    def get(self) -> list:
        response = requests.get(self.url, verify=self.ssl_verify)
        return response.json()

if __name__ == '__main__': 
    import json
    client = Client(
        'https://api.met.no/weatherapi/airqualityforecast/0.1/stations'
    )
    data = client.get()
    print(json.dumps(data[:3], indent=2))