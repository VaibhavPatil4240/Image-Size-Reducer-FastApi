import uvicorn
from fastapi import File, UploadFile, FastAPI 
from fastapi.responses import FileResponse
import image_score
app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        with open('uploads/'+file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error while uploading the file"}
    finally:
        await file.close()
    reduced_file=image_score.reduce_size(file.filename)
    return FileResponse(path="uploads/"+reduced_file, filename=reduced_file, media_type="image/jpg")

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
