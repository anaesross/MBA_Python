#!/usr/bin/python

import dns.resolver
import shodan
shodan_mykey= 'pviD6mHgspJKSkIdHhfQqqtmqQrCZOtn'
shodan_api = shodan.Shodan(shodan_mykey)
#shodan_vuln = 'openSSL/1.01' 
#shodan_vuln = 'Windows 10' 
#shodan_vuln = 'Linux 5.7' 
#shodan_vuln = 'Microsoft-IIS/8.0 country:"BR"' 
shodan_vuln = 'port:21 Anonymous user logged in' 
shodan_results = shodan_api.search(shodan_vuln) 


print('-' * 70)
print('[+] - Foram encontrados', shodan_results['total'], 'possiveis alvos: ->', shodan_vuln)
print('-' * 70)
print('TOP 100: ')

count = 1

for _result in shodan_results['matches']:
    print('[+] - Possivel alvo no ', count,'IP: ',  _result['ip_str'])
    count = count + 1