from werkzeug.utils import secure_filename

from app.settings import UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_image(request_files, nested_folder=None):
    if not 'image' in request_files:
        return

    image = request_files['image']

    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        image_abs_path = save_image(image, filename, nested_folder)

        return image_abs_path

    return


def save_image(image, filename, nested_folder=None):
    if nested_folder:
        image_path = UPLOAD_FOLDER / nested_folder / filename
    else:
        image_path = UPLOAD_FOLDER / filename

    image_abs_path = str(image_path.absolute())
    image.save(image_abs_path)
    return str(image_path.absolute())

