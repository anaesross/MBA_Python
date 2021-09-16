#!/usr/bin/python

import nmap3
from datetime import datetime
from termcolor import colored

#adiciona cor ao texto e pisca
msg1=colored('+','green', attrs=['blink'])
msg2=colored('+','cyan')
#captura o tempo do inicio da execucao
nmap_start = datetime.now()
print('Tempo inicio: ', nmap_start)


target = "11.11.11.171"


pynmap = nmap3.NmapScanTechniques()

#Faz a varredura do alvo
fin_scan = pynmap.nmap_fin_scan(target)

print('Porta: ', fin_scan['ports']['portid'])
print('Protocol: ',fin_scan['ports']['protocol'])
print('Service: ', fin_scan['ports']['service']['name'])
print('State: ', fin_scan['ports']['state']['state'])


nmap_end = datetime.now()
nmap_time = nmap_end - nmap_start
print('[' +msg2 + ']', 'Tempo de execucao: ', nmap_time)


