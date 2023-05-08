from dataclasses import dataclass
from typing import List, Optional

Vector = List[float]

@dataclass
class Coordinate:
    point: List[int]


@dataclass
class Face:
    bonding_box: List[Coordinate]
    face_landmarks: List[Coordinate]
    vector: Vector
    full_path: Optional[str] = None
    request_id: Optional[str] = None

    def dbview(self):
        return {
            attr: value
            for attr, value
            in self.__dict__.items()
        }

    def apiview(self):

        hidden_fields = ('vector', 'full_path', 'request_id')

        return {
            attr: value
            for attr, value
            in self.__dict__.items()
            if attr not in hidden_fields
        }
