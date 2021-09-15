#!/usr/bin/python

import nmap3
from datetime import datetime
from termcolor import colored

#adiciona cor ao texto e pisca
msg1=colored('+','green', attrs=['blink'])
#captura o tempo do inicio da execucao
nmap_start = datetime.now()
print('Tempo inicio: ', nmap_start)


target = "11.11.11.171"


pynmap = nmap3.NmapScanTechniques()

#Faz a varredura do alvo
vanilla = pynmap.nmap_tcp_scan(target)
#formata para json - melhor visualizacao
#vanilla_json = json.dumps(vanilla, indent = 6)

#print(vanilla_json)

for info in vanilla[target]:
    print('['+ msg1 + ']',info['portid'],info['protocol'],info['state'],info['reason'])

#captura tempo de agora - subtrai do inicial e printa tempo final
nmap_end = datetime.now()
nmap_time = nmap_end - nmap_start
print('[' + msg1 + ']', 'Tempo de execucao: ', nmap_time)

print('\n')

for chave, valor in vanilla['runtime'].items():
    if chave == 'timestr':
        time = valor
        print('Time: ',time)
    elif chave == 'summary':
        summary = valor
        print('Summary: ',summary)
    else:
        print('------------------')





