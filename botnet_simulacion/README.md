Simulación de Botnet Avanzada Tipo Mirai
Este proyecto simula una botnet avanzada similar a Mirai en un entorno controlado y seguro. Se incluyen varios componentes:
	•	Un servidor C2 (Comando y Control).
	•	Bots que pueden ser controlados por el C2.
	•	Un escáner masivo para buscar dispositivos vulnerables.
	•	Un servidor web vulnerable para ser atacado por los bots.
Requisitos
Antes de ejecutar la simulación, asegúrate de tener los siguientes requisitos:
1. Requisitos de Software
	•	Python 3: Se necesita Python para ejecutar los scripts de los bots y el servidor C2.
	•	Masscan: Se utiliza para hacer escaneos masivos de la red y encontrar dispositivos vulnerables.
	•	Flask: Framework de Python para la creación del servidor C2.
	•	SCP: Para transferir archivos entre dispositivos, como el malware o el script del bot.
2. Requisitos de Hardware
	•	Varias máquinas o instancias: Una para el servidor C2, otra para el servidor web vulnerable, y al menos una para los bots.
	•	Esto puede ser en máquinas virtuales, contenedores o instancias en la nube como AWS.
Instalación y Configuración
1. Clonar el Repositorio
Primero, clona este repositorio a tu máquina local o servidor:
git clone https://github.com/tu-usuario/botnet-avanzada.git
cd botnet-avanzada
2. Instalar Dependencias de Python
Este proyecto requiere ciertas bibliotecas de Python. Instálalas usando pip:
pip install -r requirements.txt
3. Configurar el Servidor Web Vulnerable
En tu máquina de destino, ejecuta el script server_setup.sh para configurar un servidor Apache web vulnerable. Esto simula un servidor web que será atacado por la botnet:
sudo bash target/server_setup.sh
Este script instalará Apache y abrirá el puerto 80. Luego, se colocará una página de prueba en /var/www/html/index.html que será utilizada como un “objetivo” en el ataque DDoS.
4. Iniciar el Servidor C2
En la máquina que actuará como el servidor C2, ejecuta el siguiente comando para iniciar el servidor Flask que controlará los bots:
python c2_server/c2_server.py
Este servidor escuchará en el puerto 8080 y permitirá registrar los bots, enviarles comandos y monitorear su actividad.
5. Iniciar los Bots
En una máquina (o varias, si deseas una simulación más grande), ejecuta los bots que se conectarán al servidor C2 y recibirán instrucciones.
python bot/bot.py
Cada bot se registrará automáticamente en el servidor C2 y comenzará a estar listo para recibir comandos, como un ataque DDoS.
6. Realizar un Escaneo de Red (Opcional)
Si deseas que los bots escaneen redes en busca de dispositivos vulnerables, ejecuta el siguiente comando para usar Masscan:
python bot/masscan_scanner.py
Este script buscará dispositivos vulnerables en una red específica. Modifica la dirección IP en el script según tu red o utiliza masscan manualmente con configuraciones personalizadas.
Cómo Funciona el Proyecto
1. Arquitectura del Sistema
	•	Servidor C2: Es el corazón de la botnet, controlando las acciones de los bots. Permite enviar comandos como iniciar ataques DDoS o escanear redes.
	•	Bots: Son las “máquinas zombies” que reciben comandos del servidor C2 y realizan ataques o tareas específicas, como escanear redes, atacar servidores web o propagar malware.
	•	Servidor Web Vulnerable: Es el objetivo de los ataques DDoS realizados por los bots. Este servidor está configurado con Apache y es accesible en el puerto 80.
	•	Escáner de Red: Los bots pueden buscar otros dispositivos vulnerables en la red utilizando Masscan, lo que les permite expandir la botnet.
2. Flujo de la Simulación
	1.	Registro de Bots: Cuando ejecutas los bots, estos se registran automáticamente en el servidor C2 y esperan recibir comandos.
	2.	Envió de Comandos: Desde el C2, puedes enviar comandos a los bots para realizar acciones, como atacar el servidor web vulnerable o escanear la red.
	3.	Ataque DDoS: Los bots comenzarán a realizar solicitudes repetitivas hacia el servidor web vulnerable (especificado en bot.py) para simular un ataque DDoS.
	4.	Escaneo de Red: Los bots pueden realizar escaneos para encontrar otros dispositivos vulnerables en la red, propagando el malware.
Modificar el Proyecto
Si deseas personalizar el comportamiento o agregar nuevas funcionalidades, aquí te dejo algunas sugerencias de modificaciones.
1. Cambiar los Objetivos de los Bots
En el archivo bot/bot.py, puedes modificar el código para cambiar el objetivo del ataque DDoS. Cambia la variable target_ip para apuntar a otros servidores.
target_ip = "http://192.168.1.100"
2. Agregar Más Funciones en el Servidor C2
Puedes agregar más comandos al servidor C2 para que los bots hagan más cosas. Por ejemplo, agregar un comando para “obtener información del sistema” en los bots.
En c2_server/c2_server.py, puedes agregar algo como:
@app.route('/get_system_info', methods=['POST'])
def get_system_info():
    bot_ip = request.form['ip']
    info = get_system_info_from_bot(bot_ip)  # Función que ejecuta comandos en el bot
    return jsonify(info)
3. Expandir el Escáner de Red
Actualmente, los bots pueden escanear una red local con masscan. Si deseas realizar escaneos más específicos, puedes modificar el script bot/masscan_scanner.py para utilizar otros puertos o rangos de IP.
def perform_masscan():
    """Realiza un escaneo masivo usando Masscan."""
    print("Iniciando escaneo masivo con Masscan...")
    command = "masscan 192.168.1.0/24 -p80,443,8080,22 --rate=1000"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    print("Resultados del escaneo:\n")
    print(result.stdout.decode())
    return result.stdout.decode()
4. Agregar Autenticación de Bot
Si deseas que los bots se registren con algún tipo de autenticación, puedes agregar un sistema simple de tokens o claves secretas en c2_server/c2_server.py. Aquí te dejo un ejemplo básico:
@app.route('/register', methods=['POST'])
def register_bot():
    bot_ip = request.form['ip']
    bot_token = request.form['token']
    if bot_token != "<TOKEN_SECRETO>":
        return "Acceso Denegado", 403
    add_bot_to_list(bot_ip)
    return "Bot registrado con éxito", 200
Posibles Mejoras
Este proyecto es una simulación básica, pero se pueden agregar muchas otras funcionalidades para hacerlo más realista o complejo. Algunas ideas:
	1.	Incorporar múltiples tipos de ataques: Agregar diferentes tipos de ataques DDoS como SYN Flood, UDP Flood, HTTP Flood, etc.
	2.	Agregación de nuevas técnicas de propagación: Hacer que los bots puedan propagarse mediante vulnerabilidades conocidas como Shellshock o EternalBlue.
	3.	Interfaz web para el C2: Crear una interfaz de usuario basada en web usando Flask o Django para facilitar el control de los bots.
	4.	Manejo de logs: Implementar un sistema de logs para registrar todas las acciones realizadas por los bots y el servidor C2.
Conclusión
Este proyecto te proporciona una base sólida para simular una botnet similar a Mirai en un entorno seguro y controlado. Aunque está diseñado con fines educativos y de prueba, es importante tener en cuenta que realizar este tipo de actividades en redes no autorizadas o sin 

