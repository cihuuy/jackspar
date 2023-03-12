import os
import time

# Fica em loop para minerar a criptomoeda
while True:
    # Executa o comando de mineração
    os.system("nohup minerd -a sha256 -o stratum+tcp://us.mining.prohashing.com:3335 -u sbj.workername -p a=sha-256 &")

    # Dorme por 1 hora antes de reiniciar a mineração
    time.sleep(3600)
