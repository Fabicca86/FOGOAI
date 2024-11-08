import React, { useRef, useEffect, useState } from 'react';

function App() {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const [image, setImage] = useState(null);
  const [location, setLocation] = useState(null);

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

    const getLocation = () => {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
          setLocation({
            latitude: position.coords.latitude,
            longitude: position.coords.longitude
          });
        });
      } else {
        console.error('Geolocalização não é suportada pelo seu navegador.');
      }
    };

    setupCamera();
    getLocation();
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
      formData.append('location', JSON.stringify(location));  // Adiciona a localização ao formulário

      fetch('http://localhost:5000/detect', {
        method: 'POST',
        body: formData,
      })
        .then((response) => response.json())  // Espera uma resposta JSON
        .then((data) => {
          const url = URL.createObjectURL(data.image);
          setImage(url);
          console.log('Informações de localização:', data.gps_info);  // Exibe as informações de localização
        })
        .catch((error) => {
          console.error('Erro ao fazer a solicitação fetch:', error);
        });
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
