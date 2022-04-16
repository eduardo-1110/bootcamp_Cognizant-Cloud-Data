import ipaddress

ip = '192.168.0.0/24'

end = ipaddress.ip_network  (ip)

for ip in end:
    print(ip)