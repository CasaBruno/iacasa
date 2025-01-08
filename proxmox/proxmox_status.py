import requests
 
# URL de la API de Proxmox
base_url = 'https://192.168.0.150:8006/api2/json'


def get_proxmox_status():

    # Autenticación
    auth_data = {
    'username': 'root@pam',
    'password': 'Brunito213'
    }
    response = requests.post(f'{base_url}/access/ticket', data=auth_data, verify=False)
    data = response.json()['data']
    ticket = data['ticket']
    csrf_token = data['CSRFPreventionToken']
    
    # Obtener información del nodo
    headers = {
    'Cookie': f'PVEAuthCookie={ticket}',
    'CSRFPreventionToken': csrf_token
    }

    response = requests.get(f'{base_url}/nodes', headers=headers, verify=False)
    return response.json()