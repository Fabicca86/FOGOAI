// import React, { useRef, useEffect, useState } from 'react';
// import './App.css'; // Importe o arquivo CSS


// function App() {
//   const videoRef = useRef(null);
//   const canvasRef = useRef(null);
//   const [image, setImage] = useState(null);
//   const [location, setLocation] = useState(null);

//   useEffect(() => {
//     const setupCamera = async () => {
//       try {
//         const stream = await navigator.mediaDevices.getUserMedia({ video: true });
//         videoRef.current.srcObject = stream;
//         videoRef.current.onloadedmetadata = () => {
//           videoRef.current.play().then(() => {
//             console.log('Reprodução do vídeo iniciada');
//           }).catch(error => {
//             console.error('Erro ao reproduzir o vídeo:', error);
//           });
//         };
//       } catch (error) {
//         console.error('Erro ao acessar a câmera:', error);
//       }
//     };

//     const getLocation = () => {
//       if (navigator.geolocation) {
//         navigator.geolocation.getCurrentPosition(position => {
//           setLocation({
//             latitude: position.coords.latitude,
//             longitude: position.coords.longitude
//           });
//         });
//       } else {
//         console.error('Geolocalização não é suportada pelo seu navegador.');
//       }
//     };

//     setupCamera();
//     getLocation();
//   }, []);

//   const captureImage = () => {
//     const video = videoRef.current;
//     const canvas = canvasRef.current;
//     const ctx = canvas.getContext('2d');

//     canvas.width = video.videoWidth;
//     canvas.height = video.videoHeight;

//     ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
//     canvas.toBlob((blob) => {
//       const formData = new FormData();
//       formData.append('image', blob, 'capture.jpg');
//       formData.append('location', JSON.stringify(location));  // Adiciona a localização ao formulário

//       fetch('http://localhost:5000/detect', {
//         method: 'POST',
//         body: formData,
//       })
//         .then((response) => response.json())  // Espera uma resposta JSON
//         .then((data) => {
//           //const url = URL.createObjectURL(data.image);
//           const imgUrl = `data:image/jpeg;base64,${data.image}`;
//           setImage(imgUrl);
//           //setImage(url);
//           console.log('Informações de localização:', data.gps_info);  // Exibe as informações de localização
//         })
//         .catch((error) => {
//           console.error('Erro ao fazer a solicitação fetch:', error);
//         });
//     });
//   };

//   return (
//     <div className="App">
//       <h1>Fire Detection</h1>
//       <div className="container">
//         <video ref={videoRef} autoPlay playsInline muted></video>
//         <button className="detect-button" onClick={captureImage}>Detect Fire</button>
//       </div>
//       <canvas ref={canvasRef} style={{ display: 'none' }}></canvas>
//       {image && <img src={image} alt="Detected Fire" />}
//     </div>
//   );
// }

// export default App;
import React, { useRef, useEffect, useState } from 'react';
import './App.css'; // Import CSS

function App() {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const [image, setImage] = useState(null);
  const [location, setLocation] = useState(null);
  const [plot, setPlot] = useState(null); // State to store the plot image

  useEffect(() => {
    const setupCamera = async () => {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        videoRef.current.srcObject = stream;
        videoRef.current.onloadedmetadata = () => {
          videoRef.current.play().then(() => {
            console.log('Reprodução do vídeo iniciada');
          }).catch(error => {
            console.error('Erro ao reproduzir o vídeo:', error);
          });
        };
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
      formData.append('location', JSON.stringify(location));  // Add location to the form

      fetch('http://localhost:5000/detect', {
        method: 'POST',
        body: formData,
      })
        .then((response) => response.json())  // Expect a JSON response
        .then((data) => {
          const imgUrl = `data:image/jpeg;base64,${data.image}`;
          setImage(imgUrl);
          console.log('Informações de localização:', data.gps_info);  // Display location information
        })
        .catch((error) => {
          console.error('Erro ao fazer a solicitação fetch:', error);
        });
    });
  };

  const fetchPlot = () => {
    fetch('http://localhost:5000/plot_metrics')
      .then(response => response.json())
      .then(data => {
        setPlot(`data:image/png;base64,${data.plot}`);
      })
      .catch(error => console.error('Erro ao buscar o gráfico:', error));
  };

  return (
    <div className="App">
      <h1>Fire Detection</h1>
      <div className="container">
        <video ref={videoRef} autoPlay playsInline muted></video>
        <button className="detect-button" onClick={captureImage}>Detect Fire</button>
      </div>
      <canvas ref={canvasRef} style={{ display: 'none' }}></canvas>
      {image && <img src={image} alt="Detected Fire" />}
      <div className="container">
        <button className="plot-button" onClick={fetchPlot}>Generate Metrics Plot</button>
      </div>
      {plot && <img src={plot} alt="Metrics Plot" />}
    </div>
  );
}

export default App;
