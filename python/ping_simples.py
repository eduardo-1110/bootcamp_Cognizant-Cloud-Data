import os 

print("#"*50)

ip_ou_host = input("Digite o Ip ou host a ser verificado: ")

print("-"*50)
os.system('ping -n 6 {}'.format(ip_ou_host))
print("-"*50)

