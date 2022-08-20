import requests
import os
url = 'http://127.0.0.1:8000/upload'
path=input("Path of image or directory containing multiple images")

if(os.path.isdir(path)):
    for file_name in os.listdir(path):
        file = {'file': open(path+"/"+file_name, 'rb')}
        resp = requests.post(url=url, files=file)
        filename=resp.headers.get("Content-Disposition").split("filename=")[1].replace('"',"")
        resp.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in resp.iter_content(): 
                f.write(chunk)
else:
    file = {'file': open(path, 'rb')}
    resp = requests.post(url=url, files=file)
    filename=resp.headers.get("Content-Disposition").split("filename=")[1].replace('"',"")
    resp.raise_for_status()
    with open(filename, 'wb') as f:
        for chunk in resp.iter_content(): 
            f.write(chunk)