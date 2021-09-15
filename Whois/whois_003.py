#!/usr/bin/python

import whois

target="google.com"

def func_whois(domain):
    querywhois = whois.query(domain)
    print("Nome: ", querywhois.name)
    print("Data Criacao: ",querywhois.creation_date)
    print("Data de Expiracao: ",querywhois.expiration_date)
    print("Servidor registrado: ",querywhois.registrar)
    print("Data atualizacao: ",querywhois.last_updated)
    print("Nomes servidores - lista",querywhois.name_servers)

    for domain in querywhois.name_servers:
        print("Servidor de Nomes: ", domain)

func_whois(target)
