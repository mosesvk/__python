from dataclasses import dataclass

@dataclass
class Station:
    name: str
    eoi: str
    latitude: float
    longitude: float
    height: float
    city: str

    @classmethod
    def from_dict(cls, data: dict) -> 'Station':
        return cls(
            name=data['name'],
            eoi=data['eoi'],
            latitude=float(data['latitude']),
            longitude=float(data['longitude']),
            height=data['height'],
            city=data['kommune']['name']
        )