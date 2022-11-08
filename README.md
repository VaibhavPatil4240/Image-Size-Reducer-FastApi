<h1>Image Size Reducer</h1>

<h2>This repository assesses the quality of the image and reduces the size using Jpeg Compression</h2>
<h2>System Architecture</h2>
<p align="center">
  <img src="https://user-images.githubusercontent.com/54111420/185777202-2528c280-911c-40c2-b83d-aea4625ea2f5.png" width="550" title="System Architecture">
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
<h3>You can use flask web app with same system. Source code of flask app is here <a href='https://github.com/VaibhavPatil4240/Image-Size-Reducer-Flask'>Here</a></h3>
