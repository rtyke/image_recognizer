from pathlib import Path, PosixPath


BASE_DIR: PosixPath = Path(__file__).parent.parent
UPLOAD_FOLDER: PosixPath = BASE_DIR / 'static' / 'uploads'
PREDICTOR_MODEL = str(
    (BASE_DIR / 'ml_models' / 'shape_predictor_5_face_landmarks.dat').absolute()
)
FACE_RECOGNIZER_MODEL = str(
    (BASE_DIR / 'ml_models' / 'dlib_face_recognition_resnet_model_v1.dat').absolute()
)

MATCH_THRESHOLD = 0.6
