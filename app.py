import flask
import base64
import numpy as np
import cv2
app = flask.Flask(__name__)
from PIL import Image

@app.route('/', methods = ['POST'])
def predict():
    # Initialize the data dictionary that will be returned from the view.
    data = {"success": False}
    # Ensure an image was properly uploaded to our endpoint.
    if flask.request.method == 'POST':
        if flask.request.files.get("image"):
            # Read the image in PIL format
            #image = flask.request.files["image"]
            jpg_as_str = str(flask.request.files.get('image').read(), encoding="utf-8")
            jpg_as_bytes = jpg_as_str.encode('ascii')
            jpg_original = base64.b64decode(jpg_as_bytes)
            jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
            img1 = cv2.imdecode(jpg_as_np, flags=1)
            print(type(img1))
            print(img1)
            retval, buffer = cv2.imencode('.jpg', img1)
            jpg_as_bytes = base64.b64encode(buffer)
            jpg_as_str = jpg_as_bytes.decode('ascii')

            data = {"success": True, "frame":jpg_as_str}
            # data['frame'] = jpg_as_str
            # # Indicate that the request was a success.
            # data["success"] = True
    # Return the data dictionary as a JSON response.
    return flask.jsonify(data)


if __name__ == '__main__':
    print("Loading PyTorch model and Flask starting server ...")
    print("Please wait until server has fully started")
    app.debug = True
    app.run()

