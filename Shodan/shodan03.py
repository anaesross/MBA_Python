#!/usr/bin/python

import shodan
shodan_mykey= 'pviD6mHgspJKSkIdHhfQqqtmqQrCZOtn'
shodan_api = shodan.Shodan(shodan_mykey)
shodan_target = '179.191.78.194' 
shodan_host = shodan_api.host(shodan_target) 

def shodan_portscan(shodan_host):
    for _ports in shodan_host['data']:
        print("[+] - Portas Abertas:", _ports['port'])

shodan_portscan(shodan_host)