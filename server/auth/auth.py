import socket
import random, os
from time import gmtime, strftime
from colorama import init
from colorama import Fore, Back, Style
from ast import literal_eval
from psutil import virtual_memory
from datetime import datetime

init()
def log():
    return ((Fore.MAGENTA+'['+Style.RESET_ALL+(strftime("%Y-%m-%d %H:%M:%S", gmtime()))+Fore.MAGENTA+'] '+Style.RESET_ALL))


mem = virtual_memory()
mem.total  # total physical memory available

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 56420        # Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while(True):
        (clientConnected, clientAddress) = s.accept()
        print(str(log())+"Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]))
        print(str(log())+'Awaiting HWID login request from client...')
        hwid = str((clientConnected.recv(128)).decode())
        print(str(log())+'Received authentication data from client: '+hwid)
        if hwid in open('./hwid.txt', "r+").read():
            auth = True
        else:
            auth = False
        if auth == True:
            response = str('1').encode()
            clientConnected.sendall(response)
            print(str(log())+f'{clientAddress} was successfully authenticated | HWID: {hwid}')
        if auth == False:
            response = str('0').encode()
            clientConnected.sendall(response)
            print(str(log())+f'{clientAddress} failed to authenticate. | HWID: {hwid}')
