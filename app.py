# app.py
from flask import Flask

from proxmox.proxmox_status import get_proxmox_status

app = Flask(__name__)

@app.route('/')
def index():
    return 'API LEVANTADA'

@app.route('/proxmox_status')
def proxmox_status():
    return get_proxmox_status()
