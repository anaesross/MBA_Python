#!/usr/bin/python
import argparse
import whois

#target="google.com"
msg_usage = "\n Use assim: ./whois_004.py -d <dominio alvo> \n"
msg_domain = "Informe o nome do dominio alvo: "

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


def func_main():
    option = argparse.ArgumentParser(description=msg_usage)
    option.add_argument("-d","--domain",action="store",dest="domain",help=msg_domain)
    option_args = option.parse_args()

    if option_args.domain == None:
        print("Description: ",option.description)

    domain_target = option_args.domain
    func_whois(str(domain_target))

if __name__ == '__main__':
    func_main() 

