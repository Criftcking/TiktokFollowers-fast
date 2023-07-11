import requests
import os
import json
import colorama
from colorama import Fore, Style
import time

colorama.init()
os.system("cls")

def manual():
    
    usr = input("Input Your Tiktok Username: ")

    def limpiar_terminal():
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Linux/Unix/Mac
            os.system('clear')

    limpiar_terminal()

    anchor = "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LeQEj8aAAAAAFdJdhwK42kzFPUDRN7TyNLD3PRN&co=aHR0cHM6Ly90aWtmb2xsb3dlcnMuY29tOjQ0Mw..&hl=es-419&v=khH7Ei3klcvfRI74FvDcfuOo&size=invisible&cb=ant5y7w4mpu"
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

    urlfollow = "https://tikfollowers.com/Freeusername"

    datafollow = f'username={usr}&captchaKey=&userID=&userName=&secUid=&steep=&follower_count=1000&token={token2}'

    headfollow = {
        "Host": "tikfollowers.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
        "Accept-Language": "es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://tikfollowers.com",
        "DNT": "1",
        "Alt-Used": "tikfollowers.com",
        "Connection": "keep-alive",
        "Referer": "https://tikfollowers.com/tiktok-free-followers",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers"
    }

    enviar = requests.post(url=urlfollow,data=datafollow, headers=headfollow)
    if "your account not found try again" in enviar.text:
        print("Account Not Found or Error 'Please try Again'")
    else:
        print()
        js = enviar.text

        datos = json.loads(js)

        # Acceder al valor de "Current Followers"
        current_followers = datos['html'].split('Crurrent Followers: ')[1].split('</div>')[0]
        user_id = datos['userID']
        userName = datos['userName']
        secUid = datos['secUid']
        print("secUid:", secUid)
        print("userName:", userName)
        print("UserID:", user_id)
        print("Current Followers:", current_followers)


        #########################################################################

        anchor = "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LeQEj8aAAAAAFdJdhwK42kzFPUDRN7TyNLD3PRN&co=aHR0cHM6Ly90aWtmb2xsb3dlcnMuY29tOjQ0Mw..&hl=es-419&v=khH7Ei3klcvfRI74FvDcfuOo&size=invisible&cb=ant5y7w4mpu"
        reloading = "https://www.google.com/recaptcha/api2/reload?k=6LeQEj8aAAAAAFdJdhwK42kzFPUDRN7TyNLD3PRN"

        #Recaptchav3 Token 1 post
        rq = requests.get(url=anchor)
        resp = (rq.text)


        inicio = resp.find('input type="hidden" id="recaptcha-token" value="') + 1
        fin = resp.find('">', inicio)
        valor = resp[inicio:fin]
        valore = valor[47:]
        token4 = valore
        



        postdata = {
            "v":'khH7Ei3klcvfRI74FvDcfuOo',
            "reason":'q',
            "c":token4
        }

        #Recaptvchav3 Token 2 post
        user_POST = requests.post(url=reloading, data=postdata)
        resp2 = (user_POST.text)


        inicio = resp2.find('"rresp"') + 1
        fin = resp2.find('["bgdata"', inicio)
        valor = resp2[inicio:fin]
        valore = valor[8:-26]
        token3 = valore
        
        
        #Send Followers
        sendfollowurl = 'https://tikfollowers.com/Freeusername'
        
        send_data = f'username={usr}&captchaKey=&userID={user_id}&userName={userName}&secUid={secUid}&steep=follow&follower_count=&token={token3}'
        
        
        send_headers = {
            "Host": "tikfollowers.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
            "Accept-Language": "es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://tikfollowers.com",
            "DNT": "1",
            "Alt-Used": "tikfollowers.com",
            "Connection": "keep-alive",
            "Referer": "https://tikfollowers.com/tiktok-free-followers",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin"
            }


        
        try:
            sendfollowpost = requests.post(url=sendfollowurl,headers=send_headers,data=send_data, timeout=10)
            sf = sendfollowpost.text
            print()
            print()
            
            
            inicio = sf.find('status":"error","message":"') + 1
            fin = sf.find('"}', inicio)
            valor = sf[inicio:fin]
            valore = valor[26:]
            print()
            wait = valore
            print(wait)
            
        except:
            print()
            print("STATUS: Send followers SUCCESS\nERROR: Timeout")











#AUTO
def automatic():
    
    usr = input("Input Your Tiktok Username: ")

    while True:
        
        def limpiar_terminal():
            if os.name == 'nt':  # Windows
                os.system('cls')
            else:  # Linux/Unix/Mac
                os.system('clear')

        limpiar_terminal()
        
        anchor = "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LeQEj8aAAAAAFdJdhwK42kzFPUDRN7TyNLD3PRN&co=aHR0cHM6Ly90aWtmb2xsb3dlcnMuY29tOjQ0Mw..&hl=es-419&v=khH7Ei3klcvfRI74FvDcfuOo&size=invisible&cb=ant5y7w4mpu"
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

        urlfollow = "https://tikfollowers.com/Freeusername"

        datafollow = f'username={usr}&captchaKey=&userID=&userName=&secUid=&steep=&follower_count=1000&token={token2}'

        headfollow = {
            "Host": "tikfollowers.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
            "Accept-Language": "es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://tikfollowers.com",
            "DNT": "1",
            "Alt-Used": "tikfollowers.com",
            "Connection": "keep-alive",
            "Referer": "https://tikfollowers.com/tiktok-free-followers",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "TE": "trailers"
        }

        enviar = requests.post(url=urlfollow,data=datafollow, headers=headfollow)
        if "your account not found try again" in enviar.text:
            print("Account Not Found or Error 'Please try Again'")
        else:
            print()
            js = enviar.text

            datos = json.loads(js)

            # Acceder al valor de "Current Followers"
            current_followers = datos['html'].split('Crurrent Followers: ')[1].split('</div>')[0]
            user_id = datos['userID']
            userName = datos['userName']
            secUid = datos['secUid']
            print("secUid:", secUid)
            print("userName:", userName)
            print("UserID:", user_id)
            print("Current Followers:", current_followers)


            #########################################################################

            anchor = "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LeQEj8aAAAAAFdJdhwK42kzFPUDRN7TyNLD3PRN&co=aHR0cHM6Ly90aWtmb2xsb3dlcnMuY29tOjQ0Mw..&hl=es-419&v=khH7Ei3klcvfRI74FvDcfuOo&size=invisible&cb=ant5y7w4mpu"
            reloading = "https://www.google.com/recaptcha/api2/reload?k=6LeQEj8aAAAAAFdJdhwK42kzFPUDRN7TyNLD3PRN"

            #Recaptchav3 Token 1 post
            rq = requests.get(url=anchor)
            resp = (rq.text)


            inicio = resp.find('input type="hidden" id="recaptcha-token" value="') + 1
            fin = resp.find('">', inicio)
            valor = resp[inicio:fin]
            valore = valor[47:]
            token4 = valore
            



            postdata = {
                "v":'khH7Ei3klcvfRI74FvDcfuOo',
                "reason":'q',
                "c":token4
            }

            #Recaptvchav3 Token 2 post
            user_POST = requests.post(url=reloading, data=postdata)
            resp2 = (user_POST.text)


            inicio = resp2.find('"rresp"') + 1
            fin = resp2.find('["bgdata"', inicio)
            valor = resp2[inicio:fin]
            valore = valor[8:-26]
            token3 = valore
            
            
            #Send Followers
            sendfollowurl = 'https://tikfollowers.com/Freeusername'
            
            send_data = f'username={usr}&captchaKey=&userID={user_id}&userName={userName}&secUid={secUid}&steep=follow&follower_count=&token={token3}'
            
            
            send_headers = {
                "Host": "tikfollowers.com",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
                "Accept-Language": "es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "X-Requested-With": "XMLHttpRequest",
                "Origin": "https://tikfollowers.com",
                "DNT": "1",
                "Alt-Used": "tikfollowers.com",
                "Connection": "keep-alive",
                "Referer": "https://tikfollowers.com/tiktok-free-followers",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin"
                }


            
            try:
                sendfollowpost = requests.post(url=sendfollowurl,headers=send_headers,data=send_data, timeout=10)
                sf = sendfollowpost.text
                print()
                print()
                
                
                inicio = sf.find('status":"error","message":"') + 1
                fin = sf.find('"}', inicio)
                valor = sf[inicio:fin]
                valore = valor[26:]
                print()
                wait = valore
                print(wait)
                time.sleep(2)
                
            except:
                print()
                print("STATUS: Send followers SUCCESS\nERROR: Timeout")
                time.sleep(2)




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
