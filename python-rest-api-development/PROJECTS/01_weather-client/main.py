from client import Client
from models import Station

def main():
    url = 'https://api.met.no/weatherapi/airqualityforecast/0.1/stations'

    modes = [
        ("SSL ON (default)", Client(url)),
        ("SSL OFF (verify=False)", Client(url, ssl_verify=False)),
    ]

    for label, client in modes:
        print(f"\n--- {label} ---")
        try:
            raw_stations = client.get()
            stations = [Station.from_dict(s) for s in raw_stations]
            print(f"✓ Got {len(stations)} stations. First: {stations[0].name} | {stations[0].city}")
        except Exception as e:
            print(f"✗ Failed: {e}")


if __name__ == '__main__':
    main()