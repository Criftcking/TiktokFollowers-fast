import cloudscraper
cl = cloudscraper.create_scraper()
from bs4 import BeautifulSoup
import time
import re
import colorama
from colorama import Fore
import os
import json
colorama.init()


def limpiar():
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Linux/Unix/Mac
            os.system('clear')



def main():
    limpiar()
    user = str(input("Tiktok Username: "))
    try:
        def iniciar():
            
            while True:
                
                limpiar()
                print("Username: "+Fore.GREEN+f"{user}"+Fore.RESET)
                urltk = "https://tikfollowers.com/free-tiktok-followers"
                
                tkheaders = {
                    "Host": "tikfollowers.com",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Referer": "https://tikfollowers.com/",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "1",
                    "Sec-Fetch-Dest": "document",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-User": "?1"
                }
                
                
                followresponse = cl.get(url=urltk, headers=tkheaders)
                followresponse = followresponse.text
                
                
                inicio = followresponse.find("let csrf_token") + 1
                fin = followresponse.find("let csrf_token", inicio)
                valor = followresponse[inicio:fin]
                valore = valor[17:57]
                csrf_tk = valore
                
                
                posttkurl = "https://tikfollowers.com/api/free"
                
                posttkheaders = {
                    "Host": "tikfollowers.com",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
                    "Accept": "*/*",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Referer": "https://tikfollowers.com/free-tiktok-followers",
                    "Content-Type": "text/plain;charset=UTF-8",
                    "Origin": "https://tikfollowers.com",
                    "Connection": "keep-alive",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin"
                    }
                
                
                postdatatk = {
                    "type": "follow",
                    "q": user,
                    "google_token": "t",
                    "token": csrf_tk,
                    }
                        
                postdata_json = json.dumps(postdatatk)
                getatk = cl.post(url=posttkurl,headers=posttkheaders,data=postdata_json)
                followresponse = getatk.text
                
                
                if 'success":true,"data":"' in followresponse:
                    
                    inicio = followresponse.find('success":true,"data":"') + 1
                    fin = followresponse.find('",', inicio)
                    valor = followresponse[inicio:fin]
                    valore = valor[21:500]
                    csrf_ATK = valore
                    
                    
                    inicio = followresponse.find('success":true,"data":"') + 1  # Encontrar el índice de inicio
                    fin = followresponse.find('</strong><span class=\"d-block text-sm', inicio)  # Encontrar el índice de fin
                    cadena = followresponse[inicio:fin]  # Extraer la cadena entre los índices de inicio y fin
                    separado = cadena[1228:1231]  # Eliminar " Followers " y extraer el número
                    seguidores = separado  # Convertir la cadena a entero

                    print(Fore.LIGHTYELLOW_EX+"Followers:", seguidores+Fore.RESET)
                    
                    
                    
                    
                    urlsendfollowers = "https://tikfollowers.com/api/free/send"
                    
                    usendheaders = {
                        "Host": "tikfollowers.com",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
                        "Accept": "*/*",
                        "Accept-Language": "en-US,en;q=0.5",
                        "Referer": "https://tikfollowers.com/free-tiktok-followers",
                        "Content-Type": "text/plain;charset=UTF-8",
                        "Origin": "https://tikfollowers.com",
                        "Connection": "keep-alive",
                        "Sec-Fetch-Dest": "empty",
                        "Sec-Fetch-Mode": "cors",
                        "Sec-Fetch-Site": "same-origin"
                        }
                    
                    sendfollowdata = {
                        "google_token": "t",
                        "token": csrf_tk,
                        "data": csrf_ATK,
                        "type": "follow"
                        }
                    
                    sendfollowdata_json = json.dumps(sendfollowdata)
                    
                    sendfollowers = cl.post(url=urlsendfollowers, headers=usendheaders,data=sendfollowdata_json)
                    followresponse = sendfollowers.text
                    
                    
                    if 'success":true' in followresponse:
                        print(Fore.LIGHTGREEN_EX+"Followers successfully sent"+Fore.RESET)
                        print(Fore.RED+"Automatically restarts in 5 seconds..."+Fore.RESET)
                        time.sleep(5)
                        
                        
                    elif 'success":false' in followresponse:
                        
                        palabra_extraida = re.search(r'You need to wait for a new transaction\. : \d+ Minutes', followresponse)
                        wait = palabra_extraida.group()
                        wait = wait.replace('You need to wait for a new transaction. : ', 'Try again in ')
                        print(Fore.LIGHTYELLOW_EX+wait+Fore.RESET)
                        print(Fore.RED+"Automatically restarts in 5 seconds..."+Fore.RESET)
                        time.sleep(5)
                    
                    else:
                        print(Fore.LIGHTRED_EX+"User Not Found Or Error"+Fore.RESET)
                        print(Fore.RED+"Automatically restarts in 5 seconds..."+Fore.RESET)
                        time.sleep(5)
                    

                else:
                    print(Fore.LIGHTRED_EX+"User Not Found or Error"+Fore.RESET)
                    print(Fore.RED+"Automatically restarts in 5 seconds..."+Fore.RESET)
                    time.sleep(5)
                    
        iniciar()
            
    except Exception as e:
        print(f"Error an ocurred: {e}")
        print(Fore.LIGHTYELLOW_EX+"\nWait 3 seconds..."+Fore.RESET)
        time.sleep(3)
        iniciar()

        



def menu():
    limpiar()
    print(Fore.LIGHTBLUE_EX+"""
 _____                                                                         _____ 
( ___ )-----------------------------------------------------------------------( ___ )
 |   |                                                                         |   | 
 |   |  _____ _ _    _        _        ___     _ _                             |   | 
 |   | /__   (_) | _| |_ ___ | | __   / __\__ | | | _____      _____ _ __ ___  |   | 
 |   |   / /\/ | |/ / __/ _ \| |/ /  / _\/ _ \| | |/ _ \ \ /\ / / _ \ '__/ __| |   | 
 |   |  / /  | |   <| || (_) |   <  / / | (_) | | | (_) \ V  V /  __/ |  \__ \ |   | 
 |   |  \/   |_|_|\_ \__\___/|_|\_\ \/   \___/|_|_|\___/ \_/\_/ \___|_|  |___/ |   | 
 |___|                                                                         |___| 
(_____)-----------------------------------------------------------------------(_____)
"""+Fore.RESET)
    print(Fore.LIGHTRED_EX+"Github: @Criftcking"+Fore.RESET+" BTC WALLET: 13MEq6AABjuzHZEprcRWDckS1PijxYNrPN")
    print()
    print(Fore.LIGHTYELLOW_EX+"-----MENU-----"+Fore.RESET)
    print(Fore.LIGHTWHITE_EX+"[1]---> Automatic Mode\n[2]---> Exit"+Fore.RESET)
    print()
    options = int(input(Fore.YELLOW+"Select options----> "+Fore.RESET))


    #condicion
    if options == 1:
        main()
    else:
        pass
    
menu()


