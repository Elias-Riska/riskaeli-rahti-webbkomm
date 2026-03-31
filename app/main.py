from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def read_root():
    return { "Moro!": "Rahti2", "v": "0.4" }

@app.get("/api/ip")
def ip(request: Request):
    return { "ip": request.client.host }

@app.get("/ip", response_class=HTMLResponse)
def ip(request: Request):
    return f"<h1>Your IP address is: {request.client.host}</h1> "