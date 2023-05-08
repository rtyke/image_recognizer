from typing import List

import dlib
import numpy as np

from app.recognizer import schemas
from app.settings import (
    FACE_RECOGNIZER_MODEL,
    MATCH_THRESHOLD,
    PREDICTOR_MODEL,
)


def compute_face_descriptor(
        image: np.ndarray,
        shape: dlib.full_object_detection,
) -> schemas.Vector:
    face_recognizer = dlib.face_recognition_model_v1(FACE_RECOGNIZER_MODEL)
    vector = face_recognizer.compute_face_descriptor(image, shape)
    return list(vector)


def detect_faces(image: np.ndarray) -> dlib.rectangles:
    face_detector = dlib.get_frontal_face_detector()

    detected_faces = face_detector(image, 1)
    return detected_faces

def find_face_landmarks(shape: dlib.full_object_detection) -> List[schemas.Coordinate]:
    face_landmarks = [ ]

    for face_point_index in range(shape.num_parts):
        point_coordinate = shape.part(face_point_index)
        face_landmarks.append([point_coordinate.x, point_coordinate.y])

    return face_landmarks


def describe_faces(image_path: str) -> List[schemas.Face]:
    image = dlib.load_rgb_image(image_path)
    predictor = dlib.shape_predictor(PREDICTOR_MODEL)

    detected_faces = detect_faces(image)
    faces_description = []

    for face in detected_faces:
        shape = predictor(image, face)
        face_description = {
            'bonding_box': [
                [face.tl_corner().x, face.tl_corner().y],
                [face.tr_corner().x, face.tr_corner().y],
                [face.br_corner().x, face.br_corner().y],
                [face.bl_corner().x, face.bl_corner().y],
            ],
            'face_landmarks': find_face_landmarks(shape),
            'vector': compute_face_descriptor(image, shape),
        }

        faces_description.append(schemas.Face(**face_description))

    return faces_description


def count_matches(
        input_vectors: List[schemas.Vector],
        db_vectors: List[schemas.Vector],
) -> int:
    matches_count = 0

    for vector in input_vectors:
        for db_vector in db_vectors:
            if calculate_vectors_euclidian_distance(vector, db_vector) <= MATCH_THRESHOLD:
                matches_count += 1

    return matches_count


def calculate_vectors_euclidian_distance(
        first_vector: schemas.Vector,
        second_vector: schemas.Vector,
) -> float:
    first_point = np.array(first_vector)
    second_point = np.array(second_vector)

    return np.linalg.norm(first_point - second_point)
