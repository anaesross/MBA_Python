#!/usr/bin/python

import nmap3
import json
from datetime import datetime
from termcolor import colored

#adiciona cor ao texto e pisca
msg1=colored('+','green', attrs=['blink'])
msg2=colored('+','cyan')
#captura o tempo do inicio da execucao
nmap_start = datetime.now()
print('Tempo inicio: ', nmap_start)


target = "11.11.11.171"


pynmap = nmap3.Nmap()

#Faz a varredura do alvo
version_scan = pynmap.nmap_version_detection(target)
#formata para json - melhor visualizacao
version_json = json.dumps(version_scan, indent = 6)

#print(vanilla_json)

for info in version_scan:
    print('['+ msg1 + ']',info['port'],info['protocol'],info['state'],info['reason'])
    #percorrer o dict(service) dentro do dict principal
    for chave, valor in info['service'].items():
        print('---['+ msg2 +']', chave, valor)
    
    print()


#captura tempo de agora - subtrai do inicial e printa tempo final
nmap_end = datetime.now()
nmap_time = nmap_end - nmap_start
print('[' + msg1 + ']', 'Tempo de execucao: ', nmap_time)

print('\n')






