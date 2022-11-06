""""

Lisenced to @ZeemiBhai - @AnonCyberWarrior 
Don't Share without credits

"""

# Importing Libraries

import requests
from bs4 import BeautifulSoup
from slowprint.slowprint import *

# Crearting links.txt for saving result
try:
    with open('links.txt','w') as f:
        pass
except:
    pass

#Printing Logo

logo =""" ______                   _ ____  _           _ 
 |___  /                  (_)  _ \| |         (_)
    / / ___  ___ _ __ ___  _| |_) | |__   __ _ _ 
   / / / _ \/ _ \ '_ ` _ \| |  _ <| '_ \ / _` | |
  / /_|  __/  __/ | | | | | | |_) | | | | (_| | |
 /_____\___|\___|_| |_| |_|_|____/|_| |_|\__,_|_|   
 """
slowprint("Lisenced to @ZeemiBhai",0.5)
slowprint(logo,0.05)
slowprint("\t\t\t\t\tt.me/AnonCyberWarrior",0.5)

# Taking Input
list = input("Enter dork list : ")
pages = 10 # as default set for 10 you can increase further

#Headers to decrease the chance of detection
headers = {

"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

"Accept-Encoding": "gzip, deflate",

"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",

"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}

links = []
with open(list,'r') as f:
    dorks = f.readlines()

# Logic goes here 
for dork in dorks:
    for page in range(pages):
        try : 
            url = f'https://www.google.com/search?q={dork}&sxsrf=ALiCzsaiJ_WME2nAKWXLuZIWTYx8xatGxw:1667558411030&ei=CuxkY-fONvj97_UP8eCVwA0&start={page}0&sa=N&filter=0&ved=2ahUKEwjn--SVq5T7AhX4_rsIHXFwBdgQ8tMDegQIBRAE&biw=1536&bih=722&dpr=1.25'
            # print(url)
            r = requests.get(url,headers=headers)
            # print(r.content.decode('utf-8'))
            soup = BeautifulSoup(r.content,'html.parser')
            aclass = soup.find_all('div',class_="yuRUbf")
            for classs in aclass:
                for link in classs.findAll('a'):
                    link = link.get('href')
                    links.append(link)
                    print(link)
                    with open('links.txt','a') as f:
                        f.writelines((link+"\n"))
        except:
            pass # Handling if there is error or page does not exist


