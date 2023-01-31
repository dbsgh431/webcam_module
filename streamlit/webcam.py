import cv2
import streamlit as st
import requests
import time,io, threading
import schedule
import requests, json


st.set_page_config(layout="wide")

st.title("Webcam Live Feed")
run = st.checkbox('실행')
FRAME_WINDOW = st.image([])

numbers = st.empty()

def current_location():
    here_req = requests.get("http://www.geoplugin.net/json.gp")

    if (here_req.status_code != 200):
        print("현재좌표를 불러올 수 없음")
    else:
        location = json.loads(here_req.text)
        crd = {"lat": str(location["geoplugin_latitude"]), "lng": str(location["geoplugin_longitude"])}
 
    return crd

    
def inference(files, loc):

    response = requests.post('http://118.67.129.236:30011/OD', data=loc, files=files)
    #response = requests.post('http://118.67.129.236:30011/OD', files=files, data=crd)
    label = response     
    with numbers.container():
        st.write(f'label is {label}')


delta = 0
previous = time.time()
while run:
    camera = cv2.VideoCapture('http://192.168.0.3:8080/video')
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
    is_success, im_buf_arr = cv2.imencode(".jpg", frame)
    current = time.time()
    delta += current - previous
    previous = current

    if delta > 3.0:
        io_buf = io.BytesIO(im_buf_arr)
        byte_im = io_buf.getvalue()
        crd = current_location()
        loc = {"lat" : crd['lat'], "lng":crd['lng']}
        # crd = {'lat': crd['lat'], 'lng': crd['lng']}

        files = [{'files', (byte_im)}]
        print(crd)
        inference(files, loc)
        delta = 0
else:
    st.write('Stopped')


