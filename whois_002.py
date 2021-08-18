#!/usr/bin/python

import whois
target="google.com"
querywhois = whois.query(target)
print(querywhois.name)
print(querywhois.creation_date)
print(querywhois.expiration_date)
print(querywhois.registrar)
print(querywhois.last_updated)
print(querywhois.name_servers)

for domain in querywhois.name_servers:
    print(domain)
