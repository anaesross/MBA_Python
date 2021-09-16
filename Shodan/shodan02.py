#!/usr/bin/python

import shodan
#inserir Key shodan
shodan_mykey= '###'
shodan_api = shodan.Shodan(shodan_mykey)
#shodan_target = '149.56.244.87' 
shodan_target = '179.191.78.194' 
shodan_host = shodan_api.host(shodan_target) 



def shodan_infotarget(shodan_host):
    print("IP alvo:", shodan_host['ip_str'])
    print("Organizacao:", shodan_host.get('org','n/a'))
    print("Sistema operacional:", shodan_host.get('os','n/a'))


shodan_infotarget(shodan_host)
