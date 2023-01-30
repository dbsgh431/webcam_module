from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()
import requests

@app.get("/",response_class=HTMLResponse)
async def root():
    return """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Display Webcam Stream</title>
  </head>
  <body>
    <script src="https://code.jquery.com/jquery-3.4.1.js"></script>
    <script>
    document.addEventListener("DOMContentLoaded", () => {
    new App();
  })
  
  class App {
    constructor() {
        const video = document.querySelector("#videoElement");

        if (navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
          .then( (stream) => { // function 의 this와 화살표 함수의 this 가 다름
            video.srcObject = stream;
          })
          .catch(function (error) {
            console.log("Something went wrong!");
            console.log(error);
            return;
          });
      }        
      var canvas2 = document.getElementById('canvas2');
      var context2 = canvas2.getContext('2d');


      function btnclick() {
        context2.drawImage(video,0,0,720,512);
        var ctx = document.getElementById("canvas2").getContext("2d");
        var cav2img = canvas2.toDataURL('image/png');
        
        var blobBin = atob(cav2img.split(',')[1]);
        var array = [];
        for (var i = 0; i < blobBin.length; i++) {
          array.push(blobBin.charCodeAt(i));
        }
        var file = new Blob([new Uint8Array(array)], {type: 'image/png'});	
        var formdata = new FormData();	
        formdata.append("file", file);	
        $.ajax({
        type : 'post',
        url : 'http://49.50.175.25:30001/predict2',
        data : formdata,
        processData : false,	
        contentType : false,	
        success : function (data) {
        }
        });
        }

      
      setInterval(btnclick, 3000);
    }
}
  
    </script>
	  <video autoplay="true" id="videoElement"></video>
      <button type="button" id="webcamBtn",onclick="startClock()"></button>
      <canvas id="canvas2" width="720" height="512"></canvas>
    </script>
  </body>
</html>
"""


