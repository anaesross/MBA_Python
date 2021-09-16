#!/usr/bin/python

import dns.resolver
import shodan
import time

shodan_mykey= 'pviD6mHgspJKSkIdHhfQqqtmqQrCZOtn'
shodan_api = shodan.Shodan(shodan_mykey)
#shodan_target = '149.56.244.87' 
shodan_target = '179.191.78.194' 
shodan_host = shodan_api.host(shodan_target) 


print('-' * 70)
for item in shodan_host['vulns']:
    time.sleep(0.3)
    CVE = item.replace('!','')
    print('-' * 70)
    print('Vulns: ', item)
    exploits = shodan_api.exploits.search(CVE)

    for item in exploits['matches']:
        if item.get('cve')[0] == CVE:
            print( '[+] - Vulnerabilidade/ CvE',item.get('description'))

print('-' * 70)
print('-' * 70)