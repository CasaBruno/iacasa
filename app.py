# app.py

from proxmox.proxmox_status import get_proxmox_status

from fastapi import FastAPI, Request

app = FastAPI()

@app.get('/')
def index():
    return 'API LEVANTADA'

@app.get('/proxmox_status')
def proxmox_status():
    return get_proxmox_status()

@app.get('/status')
def status(request: Request):
    header = "Bruno-Header"
    header_value = "Bruno-Value"
    headers = request.headers
    if header not in headers:
        return {'status': 'error', 'message': 'Header not found'}, 400
    
    if headers[header] != header_value:
        return {'status': 'error', 'message': 'Header value not valid'}, 400
    

    
    return {'status': 'header ok'}, 200