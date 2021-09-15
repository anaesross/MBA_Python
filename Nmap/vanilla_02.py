#!/usr/bin/python

import nmap3
#import json

target = "11.11.11.171"


pynmap = nmap3.NmapScanTechniques()

#Faz a varredura do alvo
vanilla = pynmap.nmap_tcp_scan(target)
#formata para json - melhor visualizacao
#vanilla_json = json.dumps(vanilla, indent = 6)

#print(vanilla_json)

for info in vanilla[target]:
    print(info['portid'],info['protocol'],info['state'],info['reason'])
#    print('\n')
