import uuid

from flask import (
    Blueprint,
    request,
    jsonify,
)

from app.database import db_session
from app.recognizer import (
    controllers,
    image_processor,
)
from app.utils import upload_image

bp = Blueprint("app", __name__)


@bp.route("/", methods=["GET"])
def index():
    return jsonify({'result': 'It\'s alive!'})



@bp.route("/image", methods=["POST"])
def process_image():
    image_abs_path = upload_image(request.files)

    if not image_abs_path:
        return jsonify({'exception': 'No valid image in request'}), 400

    faces = image_processor.describe_faces(image_abs_path)

    if not faces:
        return jsonify({'exception': 'No faces on a pic'}), 400

    request_id = str(uuid.uuid1())

    for face in faces:
        face.request_id = request_id
        face.full_path = image_abs_path

        controllers.load_face_to_db(db_session, face.dbview())

    faces_ = [face.apiview() for face in faces]
    return jsonify(faces_), 201


@bp.route("/recognize", methods=["POST"])
def match_image():
    image_abs_path = upload_image(request.files, nested_folder='temp')

    if not image_abs_path:
        return jsonify({'exception': 'No valid image in request'}), 400

    faces_description = image_processor.describe_faces(image_abs_path)

    if not faces_description:
        return jsonify({'Error': 'No faces on a pic'}), 400

    input_faces_vectors = [face.vector for face in faces_description]

    db_faces_vectors = controllers.fetch_all_vectors(db_session)

    matches_number = image_processor.count_matches(input_faces_vectors, db_faces_vectors)

    return jsonify({
        'faces_number': len(faces_description),
        'matches_number': matches_number,
    }
    ), 200
