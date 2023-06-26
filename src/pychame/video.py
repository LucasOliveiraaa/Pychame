from flask import Flask, request, Response
import cv2
import numpy as np
import ssl
import json
import time
import threading
import logging
from pychame import CERT_PATH, KEY_PATH, INDEX_PATH

def ShowAllInst():
    print("\n1. Your code must be a if condition to verify if have success and continue the loop if not")
    print("\n2. Enter in this link in your browser to start the chromebook's build-in camera: https://0.0.0.0:5000")
    print("\n3. In the / page of the https://0.0.0.0:5000 link, wait the status \"Sending Camera Data\"")
    print("\n4. Before the 3rd step, the success value is True and your program can run")
    print("\n5. Pass the frame value to the cv2.imshow to show the current frame in a window")
    print("\n6. Have fun!")

class Video:
    previousTime = 0
    frame_rate = 0
    frame = None
    frame_receive = True

    def __init__(self):

        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)

        self.app = Flask("Pychame Server")

        if isinstance(self.app, Flask):
            print("Pychame is ON.")
            print("Instructions to use:")
            ShowAllInst()
        else:
            print("ERROR: An error was ocurred when start the server")

        @self.app.route("/",methods=["GET"])
        def index():
            return Response(INDEX_PATH.read_text(encoding="utf-8"), mimetype='text/html')

        @self.app.route("/frame",methods=["POST"])
        def frame():
            if self.frame_receive:
                image = request.files.get('frame')
                if not image:
                    return Response(json.dumps({
                        'error': 'No image data received.',
                        'success': False
                    }), mimetype="application/json", status=500)

                self.frame = self.ConvertImage(image)

                currentTime = time.time()
                self.frame_rate = int(1 / (currentTime - self.previousTime))
                self.previousTime = currentTime

            return Response(json.dumps( {'success': True} ), mimetype="application/json")

        thread = threading.Thread(target=self.StartServer)
        thread.start()

    def ConvertImage(self,image):
        image_array = np.frombuffer(image.read(), np.uint8)
        frame_cv = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        return frame_cv

    def StartServer(self):
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.load_cert_chain(CERT_PATH,KEY_PATH)

        self.app.run(host='0.0.0.0', port=5000, ssl_context=context)

    def Read(self):
        return [
            self.frame,
            (False if self.frame is None else True)
        ]

    def Release(self):
        self.frame_receive = False