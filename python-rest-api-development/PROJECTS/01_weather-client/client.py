import requests
import urllib3


class Client(object):
    def __init__(self, url: str, ssl_verify=True):
        self.url = url
        self.ssl_verify = ssl_verify
        if ssl_verify is False:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


    def get(self) -> list:
        try:
            response = requests.get(self.url, verify=self.ssl_verify, timeout=10)
            response.raise_for_status()  # raises if 4xx or 5xx
            return response.json()
        except requests.exceptions.Timeout:
            raise RuntimeError("API request timed out")
        except requests.exceptions.ConnectionError:
            raise RuntimeError("Could not reach the API")
        except requests.exceptions.HTTPError as e:
            raise RuntimeError(f"API returned an error: {e}")


if __name__ == "__main__":
    import json

    client = Client("https://api.met.no/weatherapi/airqualityforecast/0.1/stations")
    data = client.get()
    print(json.dumps(data[:3], indent=2))
