import requests
from bs4 import BeautifulSoup
import re
import colorama
from colorama import Fore
import os

colorama.init()


def limpiar():
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Linux/Unix/Mac
            os.system('clear')





def iniciar():
    
    user = input("Input Your TikTok Username: ")

    # Realizar solicitud GET para obtener el csrf_token inicial
    url_get_token = "https://tikfollowers.com/tiktok-free-followers"
    headers_get_token = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
    }
    response_get_token = requests.get(url_get_token, headers=headers_get_token)

    if response_get_token.status_code == 200:
        # Extraer csrf_token de la URL
        csrf_token_match = re.search(r'&csrf_token=([a-f0-9]+)`', response_get_token.text)
        if csrf_token_match:
            csrf_token_kk = csrf_token_match.group(1)
            #print(csrf_token_kk)

            # Recaptchav3 Token 1
            anchor = "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LeQEj8aAAAAAFdJdhwK42kzFPUDRN7TyNLD3PRN&co=aHR0cHM6Ly90aWtmb2xsb3dlcnMuY29tOjQ0Mw..&hl=es-419&v=khH7Ei3klcvfRI74FvDcfuOo&size=invisible&cb=ant5y7w4mpu"
            reloading = "https://www.google.com/recaptcha/api2/reload?k=6LeQEj8aAAAAAFdJdhwK42kzFPUDRN7TyNLD3PRN"

            # Recaptchav3 Token 1 post
            rq = requests.get(url=anchor)
            resp = rq.text

            inicio = resp.find('input type="hidden" id="recaptcha-token" value="') + 1
            fin = resp.find('">', inicio)
            valor = resp[inicio:fin]
            valore = valor[47:]
            token = valore

            postdata = {
                "v": 'IqA9DpBOUJevxkykws9RiIBs',
                "reason": 'q',
                "c": token
            }

            # Recaptvchav3 Token 2 post
            user_POST = requests.post(url=reloading, data=postdata)
            resp2 = user_POST.text

            inicio = resp2.find('"rresp"') + 1
            fin = resp2.find('["bgdata"', inicio)
            valor = resp2[inicio:fin]
            valore = valor[8:-26]
            token2 = valore
            #print(token2)



    # Realizar solicitud POST para obtener información del usuario
    url_user_info = f"https://tikfollowers.com/api/getUserInfo/?username={user}&csrf_token={csrf_token_kk}"
    headers_user_info = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
    }
    data_user_info = {
        "recaptcha_response":token2
    }
    response_user_info = requests.post(url_user_info, json=data_user_info, headers=headers_user_info)
    #print(response_user_info.text)



    # Verificar el resultado
    if "\"error\":false" in response_user_info.text:
        # Extraer user_id y user_sec_uid
        user_id = response_user_info.json().get("user_id")
        user_sec_uid = response_user_info.json().get("user_sec_uid")


    ##########################
            # Recaptchav3 Token 1
    anchor = "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LeQEj8aAAAAAFdJdhwK42kzFPUDRN7TyNLD3PRN&co=aHR0cHM6Ly90aWtmb2xsb3dlcnMuY29tOjQ0Mw..&hl=es-419&v=khH7Ei3klcvfRI74FvDcfuOo&size=invisible&cb=ant5y7w4mpu"
    reloading = "https://www.google.com/recaptcha/api2/reload?k=6LeQEj8aAAAAAFdJdhwK42kzFPUDRN7TyNLD3PRN"

            # Recaptchav3 Token 1 post
    rq = requests.get(url=anchor)
    resp = rq.text

    inicio = resp.find('input type="hidden" id="recaptcha-token" value="') + 1
    fin = resp.find('">', inicio)
    valor = resp[inicio:fin]
    valore = valor[47:]
    token = valore

    postdata = {
        "v": 'IqA9DpBOUJevxkykws9RiIBs',
        "reason": 'q',
        "c": token
    }

            # Recaptvchav3 Token 2 post
    user_POST = requests.post(url=reloading, data=postdata)
    resp2 = user_POST.text

    inicio = resp2.find('"rresp"') + 1
    fin = resp2.find('["bgdata"', inicio)
    valor = resp2[inicio:fin]
    valore = valor[8:-26]
    token3 = valore
    #print(token3)




    ###################################################



        # Realizar solicitud POST para enviar seguidores
    url_send_followers = f"https://tikfollowers.com/api/sendFollowers?csrf_token={csrf_token_kk}"
    headers_send_followers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
            "Pragma": "no-cache",
            "Accept": "*/*"
        }
    data_send_followers = {
            "user_sec_uid": user_sec_uid,
            "user_id": user_id,
            "recaptcha_response": token3
        }
    response_send_followers = requests.post(url_send_followers, json=data_send_followers, headers=headers_send_followers)
    result = (response_send_followers.text)
    
    if 'error":false' in result:
        print(Fore.GREEN+"Seguidores enviados..."+Fore.RESET)
        input("Enter: Menu")
        menu()
    elif 'error":true' in result:
        print(response_send_followers.text)
        print(Fore.RED+"Debes esperar unos minutos."+Fore.RESET)
        input("Enter: Menu")
        menu()
        




def menu():
    limpiar()
    print(Fore.LIGHTBLACK_EX+"""

    ████████████████████████████████████████████████████████████████████████████████████████████
    █─▄─▄─█▄─▄█▄─█─▄█─▄─▄─█─▄▄─█▄─█─▄███▄─▄▄─█─▄▄─█▄─▄███▄─▄███─▄▄─█▄─█▀▀▀█─▄█▄─▄▄─█▄─▄▄▀█─▄▄▄▄█
    ███─████─███─▄▀████─███─██─██─▄▀█████─▄███─██─██─██▀██─██▀█─██─██─█─█─█─███─▄█▀██─▄─▄█▄▄▄▄─█
    ▀▀▄▄▄▀▀▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▀▀▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
        """+Fore.RESET)
    print(Fore.LIGHTRED_EX+"Telegram-By @Criftcking_Real | @GhostHat_Real"+Fore.RESET+" BTC WALLET: 13MEq6AABjuzHZEprcRWDckS1PijxYNrPN")
    print()
    print(Fore.LIGHTYELLOW_EX+"-----MENU-----"+Fore.RESET)
    print(Fore.LIGHTWHITE_EX+"[1]---> Manual Mode\n[2]---> Exit ^"+Fore.RESET)
    print()
    options = int(input(Fore.YELLOW+"Select options----> "+Fore.RESET))


    #condicion
    if options == 1:
        iniciar()
    else:
        pass
    
menu()
