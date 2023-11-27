#!/usr/bin/python3

import os 

host_file  = '/etc/hosts'

def block_website(domain):
    with open(host_file,'r')as r:
        content = r.read()
        if domain in content:
            print(f'[-] {domain} is already blocked\n')
            return
    
    with open(host_file,'a') as f:
        f.write(f"\n127.0.0.1\t{domain}")
        print(f'[+] {domain} is blocked now\n')



try:
    while True:
        domain = input('Enter website link without http/https \nExample (www.example.com): ')
        block_website(domain)
except KeyboardInterrupt:
    print('\ngood by....')