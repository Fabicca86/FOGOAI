import React, { useRef, useEffect, useState } from 'react';

function App() {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const [image, setImage] = useState(null);

  useEffect(() => {
    const setupCamera = async () => {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        videoRef.current.srcObject = stream;
        videoRef.current.play();
      } catch (error) {
        console.error('Erro ao acessar a câmera:', error);
      }
    };

    setupCamera();
  }, []);

  const captureImage = () => {
    const video = videoRef.current;
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    canvas.toBlob((blob) => {
      const formData = new FormData();
      formData.append('image', blob, 'capture.jpg');

      const playPromise = video.play();
      if (playPromise !== undefined) {
        playPromise.then(() => {
          fetch('http://localhost:5000/detect', {
            method: 'POST',
            body: formData,
          })
            .then((response) => response.blob())
            .then((blob) => {
              const url = URL.createObjectURL(blob);
              setImage(url);
            })
            .catch((error) => {
              console.error('Erro ao fazer a solicitação fetch:', error);
            });
        }).catch((error) => {
          console.error('Erro ao reproduzir o vídeo:', error);
        });
      }
    });
  };

  return (
    <div className="App">
      <h1>Fire Detection</h1>
      <video ref={videoRef} autoPlay playsInline muted></video>
      <button onClick={captureImage}>Detect Fire</button>
      <canvas ref={canvasRef} style={{ display: 'none' }}></canvas>
      {image && <img src={image} alt="Detected Fire" />}
    </div>
  );
}

export default App;
