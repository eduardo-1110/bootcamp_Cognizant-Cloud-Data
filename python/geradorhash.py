import hashlib

string = input('Digite o texto a ser gerado o hash: ')

menu = int(input('Escolha o tipo de hash a ser gerado!! \n 1- md5 \n 2- sha1 \n 3- sha256 \n 4- sha512 \n'))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print('A hash md5 da string: ',string,'é: ',resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('A hash sha1 da string: ',string,'é: ',resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('A hash sha256 da string: ',string,'é: ',resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('A hash sha512 da string: ',string,'é: ',resultado.hexdigest())
else:
    print('Algo de errado!!')