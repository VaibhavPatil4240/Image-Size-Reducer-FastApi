import requests
import os

image_extensions=('png','PNG','jpg','jpeg','JPG','JPEG')
url = 'http://127.0.0.1:8000/upload'
path=input("Enter path to image: ")
if(not os.path.isfile(path)):
    print("Specified path is not a file...")
    exit(0)
extention=path.split('.')[-1]
if(extention in image_extensions):
    file = {'file': open(path, 'rb')}
    resp = requests.post(url=url, files=file)
    filename=resp.headers.get("Content-Disposition").split("filename=")[1].replace('"',"")
    resp.raise_for_status()
    with open(filename, 'wb') as f:
        for chunk in resp.iter_content(): 
            f.write(chunk)
else:
    print("Unsupported file...\nSupported files: png, jpg, jpeg")