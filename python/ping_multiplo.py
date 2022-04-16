from ast import dump
import os
import time

with open('host.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:

        print('Verificando o ip: ',ip)
        print("-"*50)

        os.system('ping -n 4 ' + ip)
        print("-"*50)

        time.sleep(5)
        
    