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
