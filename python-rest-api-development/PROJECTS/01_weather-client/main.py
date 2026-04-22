from client import Client
from models import Station

def main():
    client = Client(
        'https://api.met.no/weatherapi/airqualityforecast/0.1/stations'
    )
    raw_stations = client.get()
    stations = [Station.from_dict(s) for s in raw_stations]

    for station in stations[:5]:
        print(f"{station.name} | {station.city} | lat: {station.latitude}")

if __name__ == '__main__':
    main()