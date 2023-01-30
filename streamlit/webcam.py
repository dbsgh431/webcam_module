import cv2
import streamlit as st
import requests
from PIL import Image
import time,io
from datetime import datetime

st.set_page_config(layout="wide")

st.title("Webcam Live Feed")
run = st.checkbox('실행')
FRAME_WINDOW = st.image([])


while run:
    camera = cv2.VideoCapture('http://192.168.10.103:8080/video')
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)

    is_success, im_buf_arr = cv2.imencode(".jpg", frame)
    io_buf = io.BytesIO(im_buf_arr)
    byte_im = io_buf.getvalue()
    files = [
    ('files', (byte_im))
    ]
    print(f"time: {datetime.now()}")
    time.sleep(3)
    response = requests.post("http://49.50.175.25:30001/predict", files=files)
    label = response.json()["result"]
    st.write(f'label is {label}')
else:
    st.write('Stopped')


