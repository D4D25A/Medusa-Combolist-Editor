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

latestversion = '1.0.0'
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
        print(str(log())+'Awaiting client version ID...')
        clientversion = str((clientConnected.recv(128)).decode())
        print(str(log())+'Received authentication data from client: '+hwid)
        if hwid in open('./hwid.txt', "r+").read(): 
            auth = True
        else:
            auth = False
        if clientversion == latestversion:
            uptodate = True
        else:
            uptodate = False
        if auth == False and uptodate == True:
            response = str('0').encode()
            clientConnected.sendall(response)
            print(str(log())+f'{clientAddress} failed to authenticate, but is up-to-date. | HWID: {hwid}')
        if auth == True and uptodate == True:
            response = str('1').encode()
            clientConnected.sendall(response)
            print(str(log())+f'{clientAddress} was successfully authenticated, is up-to-date.| HWID: {hwid}')
        if auth == True and uptodate == False:
            response = str('2').encode()
            clientConnected.sendall(response)
            print(str(log())+f'{clientAddress} client authenticated, but not up-to-date. | HWID: {hwid}')
        if auth == False and uptodate == False:
            response = str('3').encode()
            clientConnected.sendall(response)
            print(str(log())+f'{clientAddress} failed to authenticate, and is out-of-date | HWID: {hwid}')
