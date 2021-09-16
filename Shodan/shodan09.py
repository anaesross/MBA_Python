#!/usr/bin/python

import dns.resolver
import shodan
#inserir Key shodan
shodan_mykey= '####'
shodan_api = shodan.Shodan(shodan_mykey)
shodan_vuln = 'Microsoft-IIS/8.0 country:"BR"' 
shodan_results = shodan_api.search(shodan_vuln) 

print('-' * 70)
print('[+] - Foram encontrados', shodan_results['total'], 'possiveis alvos: ->', shodan_vuln)
print('-' * 70)
print('TOP 100: ')

count = 1

for _result in shodan_results['matches']:
    print('[+] - Possivel alvo no ', count,'IP: ',  _result['ip_str'])

    print('[+] - Descricao ', '\n', _result['data'])
    print('-' * 70)
    
    count = count + 1
