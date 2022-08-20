<h1>Image Size Reducer</h1>

<h2>This repository assesses the quality of the image and reduces the size using Jpeg Compression</h2>
<h2>System Architecture</h2>
<p align="center">
  <img src="https://user-images.githubusercontent.com/54111420/185749898-6cdc882d-eb72-4e89-89f3-26a8679aeb9e.png" width="550" title="System Architecture">
</p>
<hr>
<ol>
  <li>This System uses Convolutional Neural Network to assess the image quality</li>
  <li>Data set used for training <a href="https://live.ece.utexas.edu/research/quality/subjective.htm"> Live IQA DATASET</a></li>
  <li>Pretrained model is available in the directory FastApi/models
  <li>All the dependencies to run the system are included in the requirements.txt</li>
</ol>
<hr>
To run the system First install all the dependencies using 
`pip install -r requirements.txt` 
 `def myFunction([parameters]):`
After that cd FastApithen run uvicorn main:app At last you can use upload.py to access API which takes image and returns compressed image

 `def myFunction([parameters]):`

