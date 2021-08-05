from fastapi import FastAPI, Request, WebSocket
from fastapi.templating import Jinja2Templates
from starlette.responses import StreamingResponse

# fungsi convert b64 format to image
from components import b64_to_images, read_video

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/video")
async def video_stream():
    data = StreamingResponse(read_video(), media_type="multipart/x-mixed-replace;boundary=frame")
    return data

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f'Message Text was: {data}')