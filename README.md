<<<<<<< HEAD
# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
=======
# FOGOAI

Este repositorio surgiu do trabalho de pesquisa para um projeto de extensão do Centro Unversitário UFBRA. A ideia era criar uma solução que contribua com o alcance dos ODS da ONU, especificamente o de número 15, e que atenda alguma necessidade da comunidade de São José dos Campos/SP. Para tanto, foi idealizada uma solução que aliasse tecnologia com meio-ambiente, o que culminou com este modelo de IA para dispositivos com menor capacidade computacional. A tecnologia analisa imagens estáticas capturadas por câmeras e detecta a presença de fogo e/ou fumaça nas mesmas.

Nossa contribuição foi uma implementação fullstack mais simples do aplicativo para funcionar em "smartphones". 

### Repo clonado de my-Fire-Detection de https://github.com/lakuoxingkong/my-Fire-Detection e modificado de https://github.com/pedbrgs/Fire-Detection
Nota do autor traduzida por "Copilot":
"My_detect.py foi modificado a partir de detect.py para se tornar especializado no processamento de uma única imagem.
No arquivo interface.py, há uma função de interface escrita que recebe uma imagem original e retorna uma imagem com detecção de caixa e dados de anotação. A tecnologia de análise de séries temporais no repositório original (por exemplo, a tecnologia de persistência temporal adequada para ambientes internos, que analisa quantos quadros consecutivos detectam fogo e decide como verdadeiro ao atingir um determinado limiar, usada para reduzir falsos positivos) é especificamente projetada para vídeos e não pode ser usada em uma única imagem. Portanto, o código relacionado foi removido em my_detect.py. Essa tecnologia pode ser adicionada externamente. O código dessa tecnologia está em detect.py.
yolov5s.pt é o modelo treinado fornecido pelo repositório original, que pode ser usado diretamente para detecção de fogo e fumaça.
fire_000082.jpg é uma imagem de exemplo de incêndio que eu adicionei.
Os outros arquivos foram copiados do repositório original.

Método de Uso
Por exemplo, usar a câmera embutida, adotando a tecnologia de persistência temporal:

detect.py --source 0 --imgsz 640 --weights yolov5s.pt  --temporal persistence

A interface que implementei pessoalmente: a função start_fire_detect() em interface.py."

## Nossas contribuições: README AINDA EM CONSTRUÇÃO...
app.py - 
app.js -
>>>>>>> 1c51fe27535d068d38c84312ba46922312ecf9b4
