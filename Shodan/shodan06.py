#!/usr/bin/python

import dns.resolver
import shodan
#inserido Key shodan
shodan_mykey= '###'
shodan_api = shodan.Shodan(shodan_mykey)
shodan_target = '179.191.78.194' 
shodan_host = shodan_api.host(shodan_target) 

def func_shodanbanner():
    for _info in shodan_host['data']:
        print("[+] - Porta: " + str(_info['port']))
        print("[+] - Banner: " + str(_info['data']))
        print('-' * 80)

func_shodanbanner()
