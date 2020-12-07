import numpy as np
import cv2
import requests
import base64
import argparse

filename = 'cup.mp4'

PyTorch_REST_API_URL = 'http://127.0.0.1:5000'
def predict_result(filename):
    #image = open(filename,'rb').read()
    I = 50;  # 亮度阈值
    cap = cv2.VideoCapture(filename)
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            img_hsv = cv2.cvtColor(np.uint8(frame), cv2.COLOR_BGR2HSV)
            if np.mean(img_hsv[:, :, 2]) < I:
                img_hsv[:, :, 2] = cv2.equalizeHist(img_hsv[:, :, 2])
                img = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

                retval, buffer = cv2.imencode('.jpg', img)
                jpg_as_bytes = base64.b64encode(buffer)
                jpg_as_str = jpg_as_bytes.decode('ascii')
                payload = {'image': jpg_as_str}
            else:
                retval, buffer = cv2.imencode('.jpg', frame)
                jpg_as_bytes = base64.b64encode(buffer)
                jpg_as_str = jpg_as_bytes.decode('ascii')
                payload = {'image': jpg_as_str}

            r = requests.post(PyTorch_REST_API_URL, files=payload).json()
            if r['success']:
                jpg_as_str = r['frame']
                jpg_as_bytes = jpg_as_str.encode('ascii')
                jpg_original = base64.b64decode(jpg_as_bytes)
                jpg_as_np = np.frombuffer(jpg_original, dtype=np.uint8)
                img1 = cv2.imdecode(jpg_as_np, flags=1)
                cv2.imshow('frame', img1)
                cv2.waitKey(25)
            else:

                print('Request failed')
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    predict_result(filename)