import requests,bs4,json,os,sys,random,datetime,time
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.panel import Panel as nel
from rich import print as cetak
from rich.columns import Columns as col
from rich import print as rprint
from rich.text import Text as tekz
#-------------------------------------------#
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m'
h = '\x1b[1;92m'
hh = '\033[32m'
u = '\033[95m'
kk = '\033[33m'
b = '\33[1;96m'
p = '\x1b[0;34m'
boki = random.choice([m,k,h,u,b])
#----------------------------------------------#
def clear():
    os.system('clear')
#----------------------------------------------#
def kiki(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.05)
#----------------------------------------------#
def anu(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.3)
#----------------------------------------------#
def bokk():
    clear()
    time.sleep(3)
    anu('Halo Sobbb')
    kiki(f'[{k}Perkenalkan Nama Saya Kiki Wijaya{x}]\n\n{x}- {k}Asal Saya Dari Palembang\n\n{x}-{k} Umur Saya 18Tahun\n\n{x}-{k} Hobi Saya Memancing\n\n{x}-------------------------------')
    input(f'{m}Press Enter To Continue.......{x}')
    time.sleep(3)
    pertanyaan()
#---------------------------------------------#
def pertanyaan():
    clear()
    cetak(nel('Apakah Anda Ingin Berkenalan Lebih Dekat Dengan Saya? ([green]Y[white]/[red]T[white]) ? '))
    wijaya = input('Jawab Ngab ? ')
    if wijaya in ['y','Y']:
        anu(f'({h}!{x}) Anda Akan Diarah Kan Ke {h}Whatsapp{x}')
        time.sleep(3)
        os.system('xdg-open https://wa.me/6281383127594?text=Assalamualaikum+Bang+Kiki+Yang+Ganteng:)')
        input(f'{m}Press Enter To Continue...........{x}')
        clear()
        mulai()
    elif wijaya in ['t','T']:
        kiki('Anjing Lu:v')
        time.sleep(3)
        clear()
        mulai()
#-------------------------------------------#
def mulai():
    anu('\tTENTANG SCRIPT INI')
    time.sleep(2)
    cetak(nel('   Saya Membuat Script Ini Karena Gabut Ngab\nLalu Saya BerInspirasi Untuk Membuat Script Ini\nYa Maaf Kalo Masih Ngak Rapi Aokawokwa\n\tTanks To All:)'))
    input('Press Enter To Continue.....')
    time.sleep(2)
    kiki(f'- Apakah Anda Ingin Masuk Mode Hengker Wibu Tzy ? ({h}Y{x}/{m}T{x})')
    slebew = input('Jawab Om : ')
    if slebew in ['y','Y']:
        mode()
    elif slebew in ['t','T']:
        kiki(f'Oke Terima Kasih Ngab:v')
        time.sleep(1)
        anu('Good By Dadah Muachhhh:v')
        time.sleep(3)
        clear()
        exit()
def mode():
    anu(f'{h}Mode Hengker:v')
    time.sleep(2)
    os.system('apt install cmatrix')
    clear()
    os.system('pkg install cmatrix')
    os.system('cmatrix')

if __name__=='__main__':
    bokk()
