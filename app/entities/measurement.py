from pydantic import BaseModel, computed_field
from math import sqrt


class Measurement(BaseModel):
    x: float
    y: float
    z: float
    time: float

    @computed_field
    @property
    def magnitude(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    @property
    def to_dict(self):
        return {
            "measurement": "MssMeasurement",
            "fields": {
                "x": self.x,
                "y": self.y,
                "z": self.z,
                "magnitude": self.magnitude
            },
            "time": int(self.time)
        }
