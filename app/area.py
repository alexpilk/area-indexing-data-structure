from dataclasses import dataclass
from numbers import Real as RealNumber


@dataclass(unsafe_hash=True)
class Area:
    latitude: RealNumber
    longitude: RealNumber
    radius: RealNumber
    id: object

    def __post_init__(self):
        self.min_lat = self.latitude - self.radius
        self.max_lat = self.latitude + self.radius
        self.min_long = self.longitude - self.radius
        self.max_long = self.longitude + self.radius

    def __repr__(self):
        return f'Area "{self.id}" at ({self.latitude}, {self.longitude}) ± {self.radius}'
