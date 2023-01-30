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
        console.log(ctx)
      }
      setInterval(btnclick, 3000);
    }
  
}
  