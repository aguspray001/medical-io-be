import os , io , sys
from io import BytesIO
import numpy as np
import base64
from PIL import Image
import cv2

def b64_to_images(image):
    
    # decode and convert into image
    b = io.BytesIO(base64.b64decode(image))
    img = Image.open(b)

    # converting RGB to BGR as open cv standart
    frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    # process image frame
    frame = cv2.flip(frame, 1)
    img_encode = cv2.imencode('.jpg', frame)[1]

    stringData = base64.b64encode(img_encode).decode('utf-8')
    b64_src = 'data:image/jpg;base64,'
    stringData = b64_src + stringData
    return stringData