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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
