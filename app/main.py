from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return { "Moro!": "Rahti2", "v": "0.4" }

@app.get("/api/ip")
def ip(request: Request):
    return { "ip": request.client.host }