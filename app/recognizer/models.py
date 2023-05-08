from sqlalchemy import (
    Column,
    Integer,
    JSON,
    String,
)
from typing import List

from app.database import Base
from app.recognizer import schemas


class Face(Base):
    __tablename__ = 'faces'

    id = Column(Integer, primary_key=True)
    request_id = Column(String(50))
    full_path = Column(String(50))
    bonding_box = Column(JSON)
    face_landmarks = Column(JSON)
    vector = Column(JSON)

    def __init__(
            self,
            request_id: str,
            full_path: str,
            bonding_box: List[schemas.Coordinate],
            face_landmarks: List[schemas.Coordinate],
            vector: schemas.Vector,
    ):
        self.request_id = request_id
        self.full_path = full_path
        self.bonding_box = bonding_box
        self.face_landmarks = face_landmarks
        self.vector = vector

    def __repr__(self):
        return f'<Face with bonding box {self.bonding_box!r}>'
