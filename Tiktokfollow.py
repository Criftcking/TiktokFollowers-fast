import requests
import os
import json
import colorama
from colorama import Fore, Style
import time

colorama.init()
os.system("cls")

def manual():
    urltoken = 'https://tikfollowers.com/tiktok-free-followers'
    gettoken = requests.get(url=urltoken)
    
    resptk = gettoken.text
    
    inicio = resptk.find('csrf_token=') + 1
    fin = resptk.find("',", inicio)
    valor = resptk[inicio:fin]
    valore = valor[10:50]
    csrf = valore
    
    
    usr = input("Input Your Tiktok Username: ")

    def limpiar_terminal():
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Linux/Unix/Mac
            os.system('clear')

    limpiar_terminal()

    anchor = "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LeQEj8aAAAAAFdJdhwK42kzFPUDRN7TyNLD3PRN&co=aHR0cHM6Ly90aWtmb2xsb3dlcnMuY29tOjQ0Mw..&hl=es-419&v=x19joXI_IeQnFJ7YnfDapSZq&size=invisible&cb=js3unrge84u6"
    reloading = "https://www.google.com/recaptcha/api2/reload?k=6LeQEj8aAAAAAFdJdhwK42kzFPUDRN7TyNLD3PRN"

    #Recaptchav3 Token 1 post
    rq = requests.get(url=anchor)
    resp = (rq.text)


    inicio = resp.find('input type="hidden" id="recaptcha-token" value="') + 1
    fin = resp.find('">', inicio)
    valor = resp[inicio:fin]
    valore = valor[47:]
    token = valore

    

    postdata = {
        "v":'IqA9DpBOUJevxkykws9RiIBs',
        "reason":'q',
        "c":token
    }

    #Recaptvchav3 Token 2 post
    user_POST = requests.post(url=reloading, data=postdata)
    resp2 = (user_POST.text)


    inicio = resp2.find('"rresp"') + 1
    fin = resp2.find('["bgdata"', inicio)
    valor = resp2[inicio:fin]
    valore = valor[8:-26]
    token2 = valore
    
    #####################################################################
    
    url = f'https://tikfollowers.com/api/getUserInfo/?username={usr}&csrf_token={csrf}'

    data = {
        
        "recaptcha_response": token2
        }
    
    headers = {
        "Host": "tikfollowers.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
        "Accept-Language": "es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Origin": "https://tikfollowers.com",
        "DNT": "1",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "Referer": "https://tikfollowers.com/tiktok-free-followers",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
        }
    
    getinfo = requests.post(url=url,headers=headers,data=json.dumps(data))
    
    inforesp = getinfo.text
    
    
    
    data = json.loads(inforesp)

# Imprimir el valor de cada campo
    ("error:", data["error"])
    print("username:", data["username"])
    ("user_id:", data["user_id"])
    ("user_sec_uid:", data["user_sec_uid"])
    ("profile_pic:", data["profile_pic"])
    print("follower_count:", data["follower_count"])
    print("following_count:", data["following_count"])
    print()
    uid = data["user_id"]
    secid = data["user_sec_uid"]

    
    ##################################################################################
    rq = requests.get(url=anchor)
    resp = (rq.text)


    inicio = resp.find('input type="hidden" id="recaptcha-token" value="') + 1
    fin = resp.find('">', inicio)
    valor = resp[inicio:fin]
    valore = valor[47:]
    token = valore

    

    postdata = {
        "v":'IqA9DpBOUJevxkykws9RiIBs',
        "reason":'q',
        "c":token
    }

    #Recaptvchav3 Token 2 post
    user_POST = requests.post(url=reloading, data=postdata)
    resp2 = (user_POST.text)


    inicio = resp2.find('"rresp"') + 1
    fin = resp2.find('["bgdata"', inicio)
    valor = resp2[inicio:fin]
    valore = valor[8:-26]
    token2 = valore
    ############################################################################
    
    url = f'https://tikfollowers.com/api/sendFollowers?csrf_token={csrf}'
    
    
    data = {
        
        "user_sec_uid": secid,
        "user_id": uid,
        "recaptcha_response": token2
        
    }
    
    headers = {
        "Host": "tikfollowers.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
        "Accept-Language": "es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Referer": "https://tikfollowers.com/tiktok-free-followers",
        "Content-Type": "application/json",
        "Origin": "https://tikfollowers.com",
        "DNT": "1",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
        }
    
    
    send = requests.post(url=url, data=json.dumps(data), headers=headers)
    
    result = send.text
    print(result)
    
    if 'message":"Wait for' in result:
        print(Fore.RED+"Seguidores enviados, debes esperar unos minutos para volver a intentarlo"+Fore.RESET)
    elif 'follow":"ok"' in result:
        print(Fore.GREEN+"STATIUS: OK - SEGUIDORES ENVIADOS"+Fore.RESET)

    
    
    






def automatic():
    
    usr = input("Input Your Tiktok Username: ")
    while True:
        
        urltoken = 'https://tikfollowers.com/tiktok-free-followers'
        gettoken = requests.get(url=urltoken)
        
        resptk = gettoken.text
        
        inicio = resptk.find('csrf_token=') + 1
        fin = resptk.find("',", inicio)
        valor = resptk[inicio:fin]
        valore = valor[10:50]
        csrf = valore
        
        


        def limpiar_terminal():
            if os.name == 'nt':  # Windows
                os.system('cls')
            else:  # Linux/Unix/Mac
                os.system('clear')

        limpiar_terminal()

        anchor = "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LeQEj8aAAAAAFdJdhwK42kzFPUDRN7TyNLD3PRN&co=aHR0cHM6Ly90aWtmb2xsb3dlcnMuY29tOjQ0Mw..&hl=es-419&v=x19joXI_IeQnFJ7YnfDapSZq&size=invisible&cb=js3unrge84u6"
        reloading = "https://www.google.com/recaptcha/api2/reload?k=6LeQEj8aAAAAAFdJdhwK42kzFPUDRN7TyNLD3PRN"

        #Recaptchav3 Token 1 post
        rq = requests.get(url=anchor)
        resp = (rq.text)


        inicio = resp.find('input type="hidden" id="recaptcha-token" value="') + 1
        fin = resp.find('">', inicio)
        valor = resp[inicio:fin]
        valore = valor[47:]
        token = valore

        

        postdata = {
            "v":'IqA9DpBOUJevxkykws9RiIBs',
            "reason":'q',
            "c":token
        }

        #Recaptvchav3 Token 2 post
        user_POST = requests.post(url=reloading, data=postdata)
        resp2 = (user_POST.text)


        inicio = resp2.find('"rresp"') + 1
        fin = resp2.find('["bgdata"', inicio)
        valor = resp2[inicio:fin]
        valore = valor[8:-26]
        token2 = valore
        
        #####################################################################
        
        url = f'https://tikfollowers.com/api/getUserInfo/?username={usr}&csrf_token={csrf}'

        data = {
            
            "recaptcha_response": token2
            }
        
        headers = {
            "Host": "tikfollowers.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
            "Accept-Language": "es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3",
            "Origin": "https://tikfollowers.com",
            "DNT": "1",
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "Referer": "https://tikfollowers.com/tiktok-free-followers",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin"
            }
        
        getinfo = requests.post(url=url,headers=headers,data=json.dumps(data))
        
        inforesp = getinfo.text
        
        
        
        data = json.loads(inforesp)

    # Imprimir el valor de cada campo
        ("error:", data["error"])
        print("username:", data["username"])
        ("user_id:", data["user_id"])
        ("user_sec_uid:", data["user_sec_uid"])
        ("profile_pic:", data["profile_pic"])
        print("follower_count:", data["follower_count"])
        print("following_count:", data["following_count"])
        print()
        uid = data["user_id"]
        secid = data["user_sec_uid"]

        
        ##################################################################################
        rq = requests.get(url=anchor)
        resp = (rq.text)


        inicio = resp.find('input type="hidden" id="recaptcha-token" value="') + 1
        fin = resp.find('">', inicio)
        valor = resp[inicio:fin]
        valore = valor[47:]
        token = valore

        

        postdata = {
            "v":'IqA9DpBOUJevxkykws9RiIBs',
            "reason":'q',
            "c":token
        }

        #Recaptvchav3 Token 2 post
        user_POST = requests.post(url=reloading, data=postdata)
        resp2 = (user_POST.text)


        inicio = resp2.find('"rresp"') + 1
        fin = resp2.find('["bgdata"', inicio)
        valor = resp2[inicio:fin]
        valore = valor[8:-26]
        token2 = valore
        ############################################################################
        
        url = f'https://tikfollowers.com/api/sendFollowers?csrf_token={csrf}'
        
        
        data = {
            
            "user_sec_uid": secid,
            "user_id": uid,
            "recaptcha_response": token2
            
        }
        
        headers = {
            "Host": "tikfollowers.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
            "Accept-Language": "es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3",
            "Referer": "https://tikfollowers.com/tiktok-free-followers",
            "Content-Type": "application/json",
            "Origin": "https://tikfollowers.com",
            "DNT": "1",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin"
            }
        
        
        send = requests.post(url=url, data=json.dumps(data), headers=headers)
        
        result = send.text
        print(result)
        
        if 'message":"Wait for' in result:
            print(Fore.RED+"Seguidores enviados, debes esperar unos minutos para volver a intentarlo"+Fore.RESET)
        elif 'follow":"ok"' in result:
            print(Fore.GREEN+"STATIUS: OK - SEGUIDORES ENVIADOS"+Fore.RESET)
            
    
        





print(Fore.LIGHTBLACK_EX+"""

████████████████████████████████████████████████████████████████████████████████████████████
█─▄─▄─█▄─▄█▄─█─▄█─▄─▄─█─▄▄─█▄─█─▄███▄─▄▄─█─▄▄─█▄─▄███▄─▄███─▄▄─█▄─█▀▀▀█─▄█▄─▄▄─█▄─▄▄▀█─▄▄▄▄█
███─████─███─▄▀████─███─██─██─▄▀█████─▄███─██─██─██▀██─██▀█─██─██─█─█─█─███─▄█▀██─▄─▄█▄▄▄▄─█
▀▀▄▄▄▀▀▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▀▀▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
      """+Fore.RESET)
print(Fore.LIGHTRED_EX+"Telegram-By @Criftcking_Real | @GhostHat_Real"+Fore.RESET+" BTC WALLET: 13MEq6AABjuzHZEprcRWDckS1PijxYNrPN")
print()
print(Fore.LIGHTYELLOW_EX+"-----MENU-----"+Fore.RESET)
print(Fore.LIGHTWHITE_EX+"[1]---> Manual Mode\n[2]---> Automatic Mode 'Recomended'\n[3]---> Exit ^"+Fore.RESET)
print()
options = int(input(Fore.YELLOW+"Select options----> "+Fore.RESET))


#condicion
if options == 1:
    manual()
elif options == 2:
    automatic()
else:
    pass
    
    