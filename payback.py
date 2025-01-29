import colorama
from colorama import Fore
import socket 
import pyfiglet
import os
import platform
import requests
import geopy
import json
import urllib.request as req 
import time 

titulo = pyfiglet.figlet_format(text='PaYbAcK', font= 'larry3d')  #Título(usa o pyfiglet, põe entre parêntese oq ce quer usa fonte e pé na tabua)

print(colorama.Fore.LIGHTRED_EX + titulo + Fore.RESET) #printa o título
print(colorama.Fore.LIGHTGREEN_EX + 'Selecione a Opção desejada:') #printa a frase de seleção de opções 

opç1 = print(colorama.Fore.LIGHTBLUE_EX + '1) Seu Ip') #A opção para deixar as strings coloridas(colorama.Fore) só precisa ser usada uma vez para dizer que tudo em baixo deva ficar dql cor em específico(para terminar é so usar Fore.RESET)
opç2 = print('2) Seu OS')
opç3 = print('3) Geolocalização por IP')
opç4 = print(colorama.Fore.LIGHTYELLOW_EX + '4) INFORMAÇÕES DO CRIADOR' + Fore.RESET)
sair = print(colorama.Fore.LIGHTBLUE_EX + '99) Sair')



while True: # Funções de cada opção
    user = os.getlogin()
    perg = input(colorama.Fore.LIGHTCYAN_EX + f'\n{user}>') #O input fica dentro do while para o script poder entender que assim que vc digite a opção ele já volte para o input de novo(já que é um loop, então ele irá sempre repetir o input assim q vc selecione oq quer), caso contrario ele ficaria printando o ip infinitamente
   
    if perg == '1':

        #Obter IP(público) e Ipv4(local)  
        Host = socket.gethostname()
        IP = socket.gethostbyname(Host)
        publicip = requests.get('https://api.ipify.org').text 

        print(f'Seu Ipv4(local) é {IP}')
        print(f'Seu IP público é {publicip}')

    elif perg == '2':

        user = os.getlogin()#pegar o nome da máquina
        mysystem = platform.uname()#definir "mysystem" como o método do módulo platform para pegar os dados do OS
 

        print(f"O tipo de Máquina é {mysystem.machine}")
        print(f'O nome de rede do OS é {mysystem.node}')
        print(f'O Sistema é {mysystem.system}')
        print(f'O Processador é {mysystem.processor}')
        print(f'A Versão do sistem é {mysystem.release}')

    elif perg == '3':
        url = "https://extreme-ip-lookup.com/json/?key=VWDleikyfGmgAaU2k2I2"
        ip = json.load(req.urlopen(url))
        print('Informações apuradas:\n')
        for param, val in ip.items():
            print(f"{param.upper()}{' ' * (15 - len(param))}: {val if len(val) != 0 else 'Não encontrado/existe'}")

    elif perg == '4':
        print('Olá, pode me chamar de Sr. F!OAK3R, ainda estou começando no âmbito da progamação e hacking, \nainda sim decidi criar esse menu(bem básico eu sei, mas tudo tem um começo né kkkk)\nfica abaixo a minha chave pix para caso queira dar uma ajuda(AINDA A ADICIONAR POR MOTIVOS DE SEGURANÇA)')

    elif perg == '99': #elif é usado para estruturas condicionais com 3 ou mais situações(já que usando somente if e else para mais de duas condições o else só se ligaria ao ultimo if e assim o primeiro if e o else seriam printados juntos)
        t = 0.2
        colorama.Fore.RESET
        for i in range(2):
            os.system('cls')
            print('Até a próxima |')
            time.sleep(t)
            os.system('cls')
            print('Até a próxima /')
            time.sleep(t)
            os.system('cls')
            print('Até a próxima -')
            time.sleep(t)
            os.system('cls')
            print('Até a próxima \\')
            time.sleep(t)
            os.system('cls')
            
        break

    else:
        print(colorama.Fore.LIGHTRED_EX +'\nDigite uma opção válida')
