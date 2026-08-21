import psutil
from datetime import datetime
import time

print("Programa Iniciado.")

nome = input("Insira o nome de usuario: ")

print(f"Olá {nome}, aqui estão os dados da sua máquina(aguarde 15 seg):")

with open('./coleta1.csv', 'a', newline='') as csvfile:
    csvfile.write("Usuario, CPU (%),Disco (%),Memoria (%),Net (Mbps), Data e hora local\n")

for i in range(3):

    cpu = psutil.cpu_percent(interval=1)
    disc = psutil.disk_usage("/").percent
    mem = psutil.virtual_memory().percent
    net_inicio = psutil.net_io_counters()
    time.sleep(10)
    net_fim = psutil.net_io_counters()
    upload_mbps = f"{(net_fim.bytes_sent - net_inicio.bytes_sent) * 8 / 1_000_000:.3f}"
    data_hora = datetime.now().replace(microsecond=0)

    with open('./coleta1.csv', 'a', newline='') as csvfile:
        csvfile.write(f"{nome}, {cpu}, {disc}, {mem}, {upload_mbps}, {data_hora}\n")

    time.sleep(4)

    print(f"Usuario: {nome}")
    print(f"CPU: {cpu}%")
    print(f"Disco: {disc}%")
    print(f"Memória: {mem}%")
    print(f"Net: {upload_mbps} Mbps")
    print("Data e hora local:", data_hora)
    print("---------------------------------------------")

print("Programa encerrado.")