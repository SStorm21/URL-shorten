from pyshorteners import Shortener
from colorama import Fore, Style, init
import time
import os
import pyshorteners.exceptions
import ping3
import random
init()

def tip():
    global t
    first  = 'Better use Tor     '
    second = 'UrBan is kinda good'
    third  = 'CEH is trash!      '
    forth  = 's7ee7 is Trash!    '
    fith   = 'UI or CLI ?        '
    Tip = [first,second,third,forth,fith]
    t = random.choice(Tip)
def colors():
    global c , c2
    blue  = Fore.BLUE
    purple= Fore.MAGENTA
    red = Fore.RED
    green = Fore.GREEN
    cyan = Fore.CYAN
    colors = [purple,blue,red,green,cyan]
    c = random.choice(colors)
    c2= random.choice(colors)

tip()
colors()
while 1==1:
    try:
        print(c+'''
                 ______________________________________________________________________________________
                |                                                                                      | 
                |  U   U RRRR  L       SSSS   H   H   OOO   RRRR   TTTTT  EEEEE  NN   N  EEEEE  RRRR_  | 
                |  U   U R   R L       S      H   H  O   O  R   R    T    E      N N  N  E      R   R  |
                |  U   U RRRR  L        SSS   HHHHH  O   O  RRRR     T    EEEE   N  N N  EEEE   RRRR+  |
                |  U   U R  R  L           S  H   H  O   O  R  R     T    E      N   NN  E      R  R   |
                |   UUU  R   R LLLLL   SSSS   H   H   OOO   R   R    T    EEEEE  N    N  EEEEE  R   R  |  
                |______________________________________________________________________________________|
                | Discord / .6_g /Get More Tools at '''+c2+''' https://github.com/Storm290  5.10.2024            |             
                |______________________________________________________________________________________|
                |   '''+c+'''  '''+t+'''                                                              |            
                +______________________________________________________________________________________+''' + '\n')
        link = input(Fore.LIGHTBLUE_EX + '[?] Link : > ' + Style.RESET_ALL)
        link = str(link)
        def ping(link):
            try:
                return ping3.ping(link)
            except ping3.errors.Timeout:
                return None
            except PermissionError:
                return " [ ! ] Permission denied. Please run the script as administrator/root [ ! ] "

        result = ping(link)
        try :
            if result == False:
                print(Fore.RED+f" [ ! ] Ping to {link} failed [ ! ]\n (i) The host appears to be offline or there may be an issue with the link provided "+Style.RESET_ALL)
                print(Fore.RED+f" [R] Restarting .."+Style.RESET_ALL)
                time.sleep(5)
                os.system('clear')
                os.system('cls')
                continue
            else:
                print(Fore.GREEN+f" [ ! ] Ping to {link} successful, URL is Alive! [ ! ]"+Style.RESET_ALL)
                pass
            shortener = Shortener()
            short_url = shortener.tinyurl.short(link)
        except ConnectionError as e:
            print(' [ ! ] ERROR! [ ! ] '+'\n'+e)
            break
        except pyshorteners.exceptions.BadAPIResponseException:
            print(' [ ! ] ERROR! [ ! ] '+'\n'+e)
            break
        except pyshorteners.exceptions.BadURLException:
            print('[ ! ] ERROR! [ ! ]'+'\n'+e)
        print(Fore.BLUE+'[+] Shortened Link : '+Fore.LIGHTMAGENTA_EX + short_url + Style.RESET_ALL) 
        time.sleep(5)
        continue
    except pyshorteners.exceptions.ShorteningErrorException as e:
        print(Fore.RED+'[!] Error: Your request has been blocked [!]'+Style.RESET_ALL+'\n[?] How to fix it?\n[*] Use Tor or VPN')
        print('Error is:'+e)
        time.sleep(5)
        os.system('clear')
        os.system('cls')

    except KeyboardInterrupt:
        print(Fore.RED+"\n    <*> Quit! <*>  "+Style.RESET_ALL)
        quit()
