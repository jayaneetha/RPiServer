from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from RPiServer.platform import initialize_platform, forward, backward, change_speed, stop, right, left, \
    shutdown_platform

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
async def startup_event():
    initialize_platform()


@app.on_event("shutdown")
def shutdown_event():
    shutdown_platform()


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/forward")
def forward_endpoint():
    forward()
    return "DONE"


@app.get("/backward")
def backward_endpoint():
    backward()
    return "DONE"


@app.get("/left")
def left_endpoint():
    left()
    return "DONE"


@app.get("/right")
def right_endpoint():
    right()
    return "DONE"


@app.get("/stop")
def stop_endpoint():
    stop()
    return "DONE"


@app.post("/speed")
def set_speed(speed: int):
    change_speed(speed)
    return f"DONE {speed}"
