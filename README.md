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
Install All the dependencies using
<pre><code>
pip install -r requirements.txt 
</code></pre>
Then
<pre><code>
cd FastAPI
uvicorn main:app
</code></pre>
After the server starts you can use exposed API which takes Image using post method and returns compressed image as response.
To upload the image run following command
<pre><code>
python upload.py
</code></pre>
<hr>
<h3>This System is deployed on Azure using Flask. You can access deployed flask app <a href='https://imagesizereducer.azurewebsites.net/'>Here</a> and source code is <a href='https://github.com/VaibhavPatil4240/Image-Size-Reducer-Flask'>Here</a></h3>
