from typing import List

from sqlalchemy.orm import Session

from app.recognizer import models, schemas


def fetch_all_vectors(db: Session) -> List[schemas.Vector]:
    records = db.query(models.Face).all()
    return [record.vector for record in records]


def load_face_to_db(db: Session, params: dict) -> models.Face:
    face = models.Face(**params)
    db.add(face)
    db.commit()
    db.refresh(face)

    return face
