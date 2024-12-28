from pystyle import Write, Colors
import requests
import webbrowser
from bs4 import BeautifulSoup
import os
import time
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

webbrowser.open("https://t.me/IMPERRORSPROJECT")

url = "http://xn--d1asbbbhie.xn--p1ai/report/"
use_colors = True

smtp_servers = {
    "gmail.com": ("smtp.gmail.com", 587),
    "yandex.ru": ("smtp.yandex.ru", 465),
    "mail.ru": ("smtp.mail.ru", 465),
    "rambler.ru": ("smtp.rambler.ru", 465),
    "yahoo.com": ("smtp.mail.yahoo.com", 465),
    "outlook.com": ("smtp.office365.com", 587),
    "icloud.com": ("smtp.mail.me.com", 587),
    "aol.com": ("smtp.aol.com", 587),
    "zoho.com": ("smtp.zoho.com", 587),
    "protonmail.com": ("smtp.protonmail.com", 587),
    "t-online.de": ("secure.emailsrvr.com", 587),
    "gmx.de": ("mail.gmx.com", 587),
    "hotmail.de": ("smtp.live.com", 587),
    "web.de": ("smtp.web.de", 587),
    "gmx.net": ("mail.gmx.net", 587),
    "posteo.de": ("posteo.de", 587),
    "mailbox.org": ("smtp.mailbox.org", 587),
    "1und1.de": ("smtp.1und1.de", 587),
    "strato.de": ("smtp.strato.de", 465),
    "fastmail.com": ("smtp.fastmail.com", 587),
    "tutanota.com": ("smtp.tutanota.de", 587),
    "runbox.com": ("smtp.runbox.com", 587),
    "hushmail.com": ("smtp.hushmail.com", 587),
    "countermail.com": ("smtp.countermail.com", 465),
    "lavabit.com": ("smtp.lavabit.com", 465),
    "cock.li": ("mail.cock.li", 587),
    "migadu.com": ("smtp.migadu.com", 587),
    "mailfence.com": ("smtp.mailfence.com", 587),
    "kolabnow.com": ("smtp.kolabnow.com", 587),
    "mailnesia.com": ("smtp.mailnesia.com", 587),
    "mailcatch.com": ("smtp.mailcatch.com", 587),
    "mintemail.com": ("smtp.mintemail.com", 587),
    "spamgourmet.com": ("smtp.spamgourmet.com", 587),
    "mytemp.email": ("smtp.mytemp.email", 587),
    "temp-mail.org": ("smtp.temp-mail.org", 587),
    "mailtemp.info": ("smtp.mailtemp.info", 587),
    "fakemail.net": ("smtp.fakemail.net", 587),
    "sharklasers.com": ("smtp.sharklasers.com", 587)
}
#спиздишь - пизды получишь
senders = {
    "huyznaet06@gmail.com": "cyeb pnyi ctpj xxdx",
    "alabuga793@gmail.com": "tzuk rehw syaw ozme",
    "editt1345@gmail.com": "hezf xuel hzvz jzur",
    "dlatt7055@gmail.com": "tpzd nxle odaw uqwf",
    "dlyabravla655@gmail.com": "kprn ihvr bgia vdys",
    "dlatt6677@gmail.com": "usun ruef otzx zcrh",
    "edittendo0@gmail.com": "mzdl lrmx puyq epur",
    "shshsbsbsbwbwvw@gmail.com": "jqrx qivo qxjy jejt",
    "IvanKarma2000@gmail.com": "irlr cggo xksq tlbb",
    "misha28272727@gmail.com": "kgwqxvkgjyccibkm",
    "vladimiradmiralov664@gmail.com": "papq hkip geao rkuz", 
    "qstkennethadams388@gmail.com": "itpz jkrh mtwp escx",
    "usppaullewis171@gmail.com": "lpiy xqwi apmc xzmv",
    "ftkgeorgeanderson367@gmail.com": "okut ecjk hstl nucy",
    "nieedwardbrown533@gmail.com": "wvig utku ovjk appd",
    "h56400139@gmail.com": "byrl egno xguy ksvf",
    "den.kotelnikov220@gmail.com": "xprw tftm lldy ranp",
    "trevorzxasuniga214@gmail.com": "egnr eucw jvxg jatq",
    "dellapreston50@gmail.com": "qoit huon rzsd eewo",
    "neilfdhioley765@gmail.com": "rgco uwiy qrdc gvqh",
    "hhzcharlesbaker201@gmail.com": "mcxq vzgm quxy smhh",
    "samuelmnjassey32@gmail.com": "lgct cjiw nufr zxjg",
    "allisonikse1922@gmail.com": "tozo xrzu qndn mwuq",
    "corysnja1996@gmail.com": "pfjk ocbf augx cgiy",
    "maddietrdk1999@gmail.com": "rhqb ssiz csar cvot",
    "edwardmason@mail.ru": "4oTj43mFWD",
    "wilsonwhitney@gmail.com": "OgZ6*&ASSatqgh5Q",
     "nwest@yahoo.com": "EU7%U@Sdj4c@PlLu",
     "zina.podshivalova.92@mail.ru": "u4CL3YxVutmiuTvmTrbu",
"leha.novitskiy.71@mail.ru": "qQZd1gMqkU906Xk2hgJJ",
"rimma.aleksandrovicha.72@mail.ru": "biL4m6h0h4xQrDB3PnPp",
"polina.karaseva.1987@mail.ru": "mxZUqPPTrZHK99jUfPhB",
"prokhor.sablin.82@mail.ru": "vN7FjmmCmAD0JnQsANyc",
"kade.kostya@mail.ru": "U0hdXu7y3c1AVeT1Vpn9",
"yelizaveta.novokshonova.71@mail.ru": "aKPpgaPDuwaKbX1pbcq3",
"pozdovp@mail.ru": "EGDd20c7s82Z0s9LmrXc",
"siyasinovy@mail.ru": "z2ZdsRL04JvBYZrrjrvv",
"nina.gref.73@mail.ru": "sitw1XTxCVgji061iqj7",
"fil.golubkin.80@mail.ru": "PeaLrzjbn408DEeiqmQq",
"venedikt.babinov.71@mail.ru": "tBewA1HQm29c2Zkira96",
"den.verderevskiy.67@mail.ru": "fndp7qr67dpfXBAu0ePH",
"olga.viranovskaya.92@mail.ru": "50QSPrecgk5cMdk1YsBm", 
"zina.podshivalova.92@mail.ru": "u4CL3YxVutmiuTvmTrbu",
"leha.novitskiy.71@mail.ru": "qQZd1gMqkU906Xk2hgJJ",
"rimma.aleksandrovicha.72@mail.ru": "biL4m6h0h4xQrDB3PnPp",
"polina.karaseva.1987@mail.ru": "mxZUqPPTrZHK99jUfPhB",
"prokhor.sablin.82@mail.ru": "vN7FjmmCmAD0JnQsANyc",
"kade.kostya@mail.ru": "U0hdXu7y3c1AVeT1Vpn9",
"yelizaveta.novokshonova.71@mail.ru": "aKPpgaPDuwaKbX1pbcq3",
"pozdovp@mail.ru": "EGDd20c7s82Z0s9LmrXc",
"siyasinovy@mail.ru": "z2ZdsRL04JvBYZrrjrvv",
"nina.gref.73@mail.ru": "sitw1XTxCVgji061iqj7",
"fil.golubkin.80@mail.ru": "PeaLrzjbn408DEeiqmQq",
"venedikt.babinov.71@mail.ru": "tBewA1HQm29c2Zkira96",
"den.verderevskiy.67@mail.ru": "fndp7qr67dpfXBAu0ePH",
"olga.viranovskaya.92@mail.ru": "50QSPrecgk5cMdk1YsBm",
"sylvain.cavart@airgeneva.org": "cafous",
"tineke.kollenaar@tele2.nl": "albertina1960",
"diego1313@orange.fr": "diego1313",
"mouler@t-online.de": "Bifteki8",
"thiele.jeni94@t-online.de": "WISZ1LB6",
"original@vp.pl": "kingai06",
"pompiceklukasek@email.cz": "satisfakce",
"emmabochhoff@web.de": "ahwwik2310",
"meier.joan@web.de": "Kleve1991",
"piyushumathe2007@rediffmail.com": "sharpraz0r",
"kisa472204@eyou.com": "Kisa472204",
"elisa@studioverde.it": "Studio2016",
"a.rougecarrassat@wanadoo.fr": "alexis",
"subintensiva.alatri@aslfrosinone.it": "subintensiva",
"tim.91@orange.fr": "carcasse91",
"home@oktay-atas.de": "ciyrikli",
"nothingb@seznam.cz": "niceho",
"heinrich.buss1@ewetel.net": "nadja1",
"order@devilskiss.net": "sickness",
"365shop@tele2.nl": "Kayalar61!",
"tetard007@orange.fr": "Code55680%",
"jolad345@gazeta.pl": "pingus1",
"spuk@vwi-magdeburg.de": "spuk1234",
"trasparenza@fattoriadellapiana.it": "fattoria900",
"flex439@web.de": "killa936",
"masalamlyne@wanadoo.fr": "pascal1",
"patryk.radulski@web.de": "rasiak156",
"titeamande@wanadoo.fr": "Alright1",
"alexandra@graciebears.com": "Ve1sheda",
"benkoemakat@rediffmail.com": "739749",
"sylvain-pellieux@wanadoo.fr": "nathoo",
"sonne0007@gmx.de": "Fynn2010",
}

baner = """
██╗███╗   ███╗██████╗ ███████╗██████╗  ██████╗ ██████╗ ███████╗
██║████╗ ████║██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗██╔════╝
██║██╔████╔██║██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝███████╗
██║██║╚██╔╝██║██╔═══╝ ██╔══╝  ██╔══██╗██║   ██║██╔══██╗╚════██║
██║██║ ╚═╝ ██║██║     ███████╗██║  ██║╚██████╔╝██║  ██║███████║
╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
                                                               
██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗     
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝     
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║        
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║        
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║        
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝                            
•@web3tweak        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  """

proxies = [
    "http://123.45.67.89:8080",
    "http://98.76.54.32:80",
    "http://111.222.33.44:80"
]	# сюда добавить новые норм прокси с 80 или 8080 

user_agents = [
     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.6900.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/59.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.6232.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/45.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.6601.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/105.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.7252.0 Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/32.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.3745.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.8312.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/74', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.7859.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/62.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/83.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/107.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/87.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/98.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/89.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/99.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/39.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/68.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.1093.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/95', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/31.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.1717.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.1639.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/84.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/82', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.6195.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.3017.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.3335.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.4466.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.4905.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/70.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.5389.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/106.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.3074.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/89', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/33.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/102.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.1499.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.8932.0 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/82.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/44', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.6515.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3933.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/86.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/36.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/40.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.3634.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.3570.0 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.4896.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/49.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/98.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.1496.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/107.0.0.0 Safari/605.1.15', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.9879.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.4786.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.3647.0 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/44.0 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/37', 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5 Build/OPR6.170623.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.9729.0 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2112.0 Safari/537.36',
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_proxy():
    return random.choice(proxies)

def get_csrf_token():
    for _ in range(len(proxies)):
        proxy = get_random_proxy()
        headers = {"User-Agent": random.choice(user_agents)}
        try:
            response = requests.get(url, headers=headers, proxies={'http': proxy, 'https': proxy}, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.find('input', {'name': '_token'})['value']
        except:
            continue
    raise Exception("Не удалось получить CSRF токен. Проверьте список прокси.")

def get_institutions():
    for _ in range(len(proxies)):
        proxy = get_random_proxy()
        headers = {"User-Agent": random.choice(user_agents)}
        try:
            response = requests.get(url, headers=headers, proxies={'http': proxy, 'https': proxy}, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            institutions = soup.find('select', {'name': 'institution'}).find_all('option')
            return [(option['value'], option.text.strip()) for option in institutions]
        except:
            continue
    raise Exception("Не удалось получить список ведомств. Проверьте список прокси.")

def send_report(csrf_token, institution, body, is_anonymous, name='', email='', phone=''):
    for _ in range(len(proxies)):
        proxy = get_random_proxy()
        headers = {"User-Agent": random.choice(user_agents)}
        try:
            data = {
                '_token': csrf_token,
                'institution': institution,
                'body': body,
                'name': name,
                'email': email,
                'phone': phone,
                'anonymously': 'on' if is_anonymous else '',
                'allow_publish': 'on'
            }
            response = requests.post(url, headers=headers, data=data, proxies={'http': proxy, 'https': proxy}, timeout=5)
            return response.status_code == 200
        except:
            continue
    raise Exception("Не удалось отправить донос. Проверьте список прокси.")

def send_email(receiver, subject, body):
    for sender_email, sender_password in senders.items():
        domain = sender_email.split('@')[1]
        if domain not in smtp_servers:
            if use_colors:
                Write.Print(f"  Неизвестный домен почты {sender_email}.\n", Colors.red, interval=0.0001)
            else:
                print(f"  Неизвестный домен почты {sender_email}.")
            continue

        smtp_server, smtp_port = smtp_servers[domain]

        for _ in range(len(proxies)):
            proxy = get_random_proxy()
            try:
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))

                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(sender_email, sender_password)
                    server.sendmail(sender_email, receiver, msg.as_string())
                    time.sleep(3)

                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if use_colors:
                    Write.Print(f"  Письмо успешно отправлено с {sender_email} на {receiver} в {current_time}.\n", Colors.green, interval=0.0001)
                else:
                    print(f"  Письмо успешно отправлено с {sender_email} на {receiver} в {current_time}.")
                return True
            except smtplib.SMTPAuthenticationError:
                if use_colors:
                    Write.Print(f"  Ошибка аутентификации для почты {sender_email}. Попытка следующей почты.\n", Colors.red, interval=0.0001)
                else:
                    print(f"  Ошибка аутентификации для почты {sender_email}. Попытка следующей почты.")
                continue
            except Exception as e:
                if use_colors:
                    Write.Print(f"  Ошибка при отправке письма с {sender_email}: {e}\n", Colors.red, interval=0.0001)
                else:
                    print(f"  Ошибка при отправке письма с {sender_email}: {e}")
                continue
    raise Exception("Не удалось отправить письмо. Проверьте список прокси, почт и их пароли.")

def print_colored(text, color, interval=0.0001):
    if use_colors:
        Write.Print(text, color, interval=interval)
    else:
        print(text)

def input_colored(prompt, color, interval=0.0001):
    if use_colors:
        return Write.Input(prompt, color, interval=interval)
    else:
        return input(prompt)

main = """
1. Отправить донос сайт
2. Отправить донос письмо 
3. Включить/Выключить цвета
4. Выход
"""

def main_menu():
    global use_colors
    while True:
        clear_screen()
        print_colored(baner, Colors.black_to_red, interval=0.0001)
        print_colored(main, Colors.black_to_red, interval=0.0001)
        choice = input_colored("Выберите действие: ", Colors.black_to_red, interval=0.0001)

        if choice == '1':
            try:
                csrf_token = get_csrf_token()
                institution_list = get_institutions()
                print_colored("Выберите ведомство:\n", Colors.black_to_red, interval=0.0001)
                for i, (value, name) in enumerate(institution_list, 1):
                    print_colored(f"{i}. {name}\n", Colors.black_to_red, interval=0.0001)
                institution_index = int(input_colored("Введите номер ведомства: ", Colors.black_to_red, interval=0.0001)) - 1
                institution = institution_list[institution_index][0]
                body = input_colored("Введите текст доноса: ", Colors.black_to_red, interval=0.0001)
                is_anonymous = input_colored("Анонимно? (да/нет): ", Colors.black_to_red, interval=0.0001).lower() == 'да'

                if not is_anonymous:
                    name = input_colored("Введите ФИО: ", Colors.black_to_red, interval=0.0001)
                    email = input_colored("Введите Email: ", Colors.black_to_red, interval=0.0001)
                    phone = input_colored("Введите Телефон: ", Colors.black_to_red, interval=0.0001)
                else:
                    name = email = phone = ''

                if send_report(csrf_token, institution, body, is_anonymous, name, email, phone):
                    print_colored("Донос успешно отправлен!\n", Colors.black_to_green, interval=0.0001)
                else:
                    print_colored("Ошибка при отправке доноса.\n", Colors.black_to_red, interval=0.0001)

                input_colored("Нажмите Enter для возврата в меню...", Colors.black_to_red, interval=0.0001)
                clear_screen()
            except Exception as e:
                print_colored(f"Ошибка: {e}\n", Colors.black_to_red, interval=0.0001)
                input_colored("Нажмите Enter для возврата в меню...", Colors.black_to_red, interval=0.0001)
                clear_screen()

        elif choice == '2':
            try:
                receiver = input_colored("Введите почту получателя: ", Colors.black_to_red, interval=0.0001)
                subject = input_colored("Введите тему письма: ", Colors.black_to_red, interval=0.0001)
                body = input_colored("Введите текст письма: ", Colors.black_to_red, interval=0.0001)

                if send_email(receiver, subject, body):
                    print_colored("Письмо успешно отправлено!\n", Colors.black_to_green, interval=0.0001)
                else:
                    print_colored("Ошибка при отправке письма.\n", Colors.black_to_red, interval=0.0001)

                input_colored("Нажмите Enter для возврата в меню...", Colors.black_to_red, interval=0.0001)
                clear_screen()
            except Exception as e:
                print_colored(f"Ошибка: {e}\n", Colors.black_to_red, interval=0.0001)
                input_colored("Нажмите Enter для возврата в меню...", Colors.black_to_red, interval=0.0001)
                clear_screen()

        elif choice == '3':
            use_colors = not use_colors
            print_colored("Цвета " + ("включены" if use_colors else "выключены") + "\n", Colors.black_to_red, interval=0.0001)
            input_colored("Нажмите Enter для возврата в меню...", Colors.black_to_red, interval=0.0001)
            clear_screen()

        elif choice == '4':
            break

if __name__ == "__main__":
    main_menu()
