#!/usr/bin/python

import shodan
#inserir Key shodan
shodan_mykey= '####'
shodan_api = shodan.Shodan(shodan_mykey)
shodan_target = '179.191.78.194' 
shodan_host = shodan_api.host(shodan_target) 


def shodan_infotarget(shodan_host):
    print("[*] -  Informacoes sobre o alvo")
    print("IP alvo:", shodan_host['ip_str'])
    print("Organizacao:", shodan_host.get('org','n/a'))
    print("Sistema operacional:", shodan_host.get('os','n/a'))
    print("#" * 30)

def shodan_portscan(shodan_host):
    print("[*] -  Identificacao de portas ativas")

    for _ports in shodan_host['data']:
        print("[+] - Portas Abertas:", _ports['port'])
    
    print("#" * 30)

shodan_infotarget(shodan_host)
shodan_portscan(shodan_host)
