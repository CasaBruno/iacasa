# app.py

from proxmox.proxmox_status import get_proxmox_status

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return 'API LEVANTADA'

@app.get('/proxmox_status')
def proxmox_status():
    return get_proxmox_status()
