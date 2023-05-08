#!/usr/bin/python3
import os
import requests
import random
import socket
import getpass
import hashlib 
import colorama
from colorama import Back, Fore, Style
import sys
from datetime import datetime
import scapy.all as scapy
import re


def choice():
    choice = input("Select option >> ")
    match coice:
        case "1":
            hashcrack()
        case "2":
            password_generator()
        case "3":
            Portus()
        case "4":
            Wifi_scan()
        case "5":
            exit()
        case _:
            menu()


def exit():
    os.system("clear")
    print("""   **********************************************************
                *    Do you really wanna exit and close program??        *
                *                                                        *
                *                       [Y/N]                            *
                *                                                        *
                **********************************************************""")
    
    exit = input()
    if exit == "Y" or "y":
        sys.exit()
    elif exit == "N" or "n":
        menu()
    
def menu():
    os.system("clear")

    colorama.init(autoreset=True)

    print(Fore.RED + """          _____                    _____                    _____                    _____          
                                 /\    \                  /\    \                  /\    \                  /\    \         
	                            /::\    \                /::\    \                /::\    \                /::\    \        
                                \:::\    \              /::::\    \              /::::\    \              /::::\    \       
                                 \:::\    \            /::::::\    \            /::::::\    \            /::::::\    \      
                                  \:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     
                                    \:::\    \        /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \    
                                    /::::\    \       \:::\   \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \   
                                   /::::::\    \    ___\:::\   \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \  
                                  /:::/\:::\    \  /\   \:::\   \:::\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\ 
                                 /:::/  \:::\____\/::\   \:::\   \:::\____\/:::/  \:::\   \:::\____\/:::/  \:::\   \:::|    |
                                /:::/    \::/    /\:::\   \:::\   \::/    /\::/    \:::\  /:::/    /\::/   |::::\  /:::|____|
                               /:::/    / \/____/  \:::\   \:::\   \/____/  \/____/ \:::\/:::/    /  \/____|:::::\/:::/    / 
                              /:::/    /            \:::\   \:::\    \               \::::::/    /         |:::::::::/    /  
                             /:::/    /              \:::\   \:::\____\               \::::/    /          |::|\::::/    /   
                             \::/    /                \:::\  /:::/    /               /:::/    /           |::| \::/____/    
                              \/____/                  \:::\/:::/    /               /:::/    /            |::|  ~|          
                                                        \::::::/    /               /:::/    /             |::|   |          
                                                         \::::/    /               /:::/    /              \::|   |          
                                                          \::/    /                \::/    /                \:|   |          
                                                           \/____/                  \/____/                  \|___|  """)        
                                                                                                   
    print("Made by Hiercp1 > version 2.0")

    print ("""CHOOSE TOOL:
    [1]>Hashcrack
    [2]>Password_generator
    [3]>Portus(port scanner)
    [4]>LAN scan
    [5]>Exit



    """)
    choice()

def Wifi_scan():
    os.system("clear")


    print("""    @@@  @@@  @@@  @@@  @@@@@@@@  @@@      @@@@@@    @@@@@@@   @@@@@@   @@@  @@@  
                 @@@  @@@  @@@  @@@  @@@@@@@@  @@@     @@@@@@@   @@@@@@@@  @@@@@@@@  @@@@ @@@  
                 @@!  @@!  @@!  @@!  @@!       @@!     !@@       !@@       @@!  @@@  @@!@!@@@ 
                 !@!  !@!  !@!  !@!  !@!       !@!     !@!       !@!       !@!  @!@  !@!!@!@! 
                 @!!  !!@  @!@  !!@  @!!!:!    !!@     !!@@!!    !@!       @!@!@!@!  @!@ !!@!  
                 !@!  !!!  !@!  !!!  !!!!!:    !!!      !!@!!!   !!!       !!!@!!!!  !@!  !!!  
                 !!:  !!:  !!:  !!:  !!:       !!:          !:!  :!!       !!:  !!!  !!:  !!!  
                 :!:  :!:  :!:  :!:  :!:       :!:         !:!   :!:       :!:  !:!  :!:  !:! 
                 :::: :: :::    ::   ::        ::     :::: ::    ::: :::  ::   :::   ::   ::  
                 :: :  : :      :     :        :       :: : :     :: :: :   :   : :  ::    :""")     

    

    


    ip = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")\
    while True:
        ip2 = input("\nEnter ip adress and range: ")

        if ip.search(ip2):

            print(f"{ip2} is valid ip address range")
            break



    arp_result = scapy.arping(ip2)

def Portus():
    os.system("clear")
 print("""  ▄███████▄  ▄██████▄     ▄████████     ███     ███    █▄     ▄████████ 
            ███     ███ ███    ███   ███    ███ ▀█████████▄ ███   ███   ███    ███ 
            ███    ███ ███    ███   ███    ███    ▀███▀▀██ ███    ███   ███    █▀  
            ███    ███ ███    ███  ▄███▄▄▄▄██▀     ███   ▀ ███    ███   ███        
            ▀█████████▀  ███    ███ ▀▀███▀▀▀▀▀       ███     ███    ███ ▀███████████ 
            ███        ███    ███ ▀███████████     ███     ███    ███          ███ 
            ███        ███    ███   ███    ███     ███     ███    ███    ▄█    ███ 
            ▄████▀       ▀██████▀    ███    ███    ▄████▀   ████████▀   ▄████████▀""")  
    

    
    target = input("Type target (IP ADRESS) to scan: ")
    port_min = input("scan port from: ")
    port_max = input ("scan port to: ")


    try:
        for port in range(int(port_min),int(port_max)):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            result = s.connect_ex((target,port))
            if result == 0:
                print("[*] port is open: " + str(port))
            elif result !=0:
                print("[*] port is closed: " + str(port))
            s.close()
            
               
    except KeyboardInterrupt:
        print("\n EXIT")
        choice4 = input("Again [y/n]: ")
        if choice4 == "y":
            Portus()
        else:
            menu()
        
    except socket.error:
        print("host not responding")
        menu()
    
 def password_generator():
    os.system("clear")
    print("""                                                                           ___                                                             ___
                                                                                        | $$                                                            | $$          
                 ______   ______   _______  _______ __   __   __  ______   ______   ____| $$        ______   ______  _______   ______   ______  ______ _| $$_    ______   ______   
                /      \ |      \ /       \/       |  \ |  \ |  \/      \ /      \ /      $$       /      \ /      \|       \ /      \ /      \|      |   $$ \  /      \ /      \  
                |  $$$$$$\ \$$$$$$|  $$$$$$|  $$$$$$| $$ | $$ | $|  $$$$$$|  $$$$$$|  $$$$$$$      |  $$$$$$|  $$$$$$| $$$$$$$|  $$$$$$|  $$$$$$\\$$$$$$\$$$$$$ |  $$$$$$|  $$$$$$\ 
                | $$  | $$/      $$\$$    \ \$$    \| $$ | $$ | $| $$  | $| $$   \$| $$  | $$      | $$  | $| $$    $| $$  | $| $$    $| $$   \$/      $$| $$ __| $$  | $| $$   \$$ 
                | $$__/ $|  $$$$$$$_\$$$$$$\_\$$$$$$| $$_/ $$_/ $| $$__/ $| $$     | $$__| $$      | $$__| $| $$$$$$$| $$  | $| $$$$$$$| $$    |  $$$$$$$| $$|  | $$__/ $| $$       
                | $$    $$\$$    $|       $|       $$\$$   $$   $$\$$    $| $$      \$$    $$______ \$$    $$\$$     | $$  | $$\$$     | $$     \$$    $$ \$$  $$\$$    $| $$       
                | $$$$$$$  \$$$$$$$\$$$$$$$ \$$$$$$$  \$$$$$\$$$$  \$$$$$$ \$$       \$$$$$$|      \_\$$$$$$$ \$$$$$$$\$$   \$$ \$$$$$$$\$$      \$$$$$$$  \$$$$  \$$$$$$ \$$       
                | $$                                                                         \$$$$$|  \__| $$                                                                       
                | $$                                                                                \$$    $$                                                                       
                \$$                                                                                 \$$$$$$""") 
    
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()_-=+[{]}:;|"

    password = random.sample(characters, k=32)
    newpassword = "".join(password)
    print("this is your password: " + newpassword)

    choice2 = input("Again [y/n]\n")
    if choice2 == "y" or "Y":
        password_generator()
    else:
        menu()
    
 def hashcrack():
    os.system("clear")
    flag = 0

    print(""" _   _   ___   _____ _   _   _____ ______  ___  _____  _   __
             | | | | / _ \ /  ___| | | | /  __ \| ___ \/ _ \/  __ \| | / /
             | |_| |/ /_\ \\  `--.| |_| | | /  \/| |_/ / /_\ \ /  \/| |/ /
             |  _  ||  _  | `--. \  _  | | |    |    /|  _  | |    |    \
             | | | || | | |/\__/ / | | | | \__/\| |\ \| | | | \__/\| |\  \
             \_| |_/\_| |_/\____/\_| |_/  \____/\_| \_\_| |_/\____/\_| \_/""")
    
    hashx = input("please.enter.md5.hash: ")

    wordlist = input("please.enter.wordlist: ")

    try:
        filex = open (wordlist, "r")
    except:
        print("error.no.wordlist.found")
        quit()

    for x in filex:

        enc_wrd = x.encode('utf-8')
        make = hashlib.md5(enc_wrd.strip()).hexdigest()

        if make == hashx:
            print("password.found")
            print("password.is " + x)
            flag = 1
            vyber = input("Again [y/n]\n")
            if vyber == "y" or "Y":
                hashcrack()
            else:
                menu()
            break

    if flag == 0:
        print("password.is.not.in.the.list")
        vyber = input("Again [y/n]\n")
        if vyber == "y" or "Y":
            hashcrack()
        else:
            menu()
            
            
            
            
            
            
            
            
if __name__ == "__main__":
    menu()
#MADE BY MARTIN RAJNOCH
