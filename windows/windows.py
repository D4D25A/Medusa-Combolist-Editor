import sys,time,os,send,random,requests,chardet,subprocess,shutil,psutil,ctypes,fileinput,textwrap,itertools,socket,re,tkinter,threading,msvcrt,pygame
from time import gmtime, strftime
from ast import literal_eval
from datetime import datetime
from pygame import mixer
from tkinter import filedialog
from tkinter import *

os.system('cls' if os.name == 'nt' else 'clear')
sys.stdout.write("\x1b]2;Medusa - Made by kyle-import\x07")

def checkIfProcessRunning(processName): # Check if there is any running process that contains the given name processName.
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def securityrun():
    if checkIfProcessRunning('Fiddler'):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('A network sniffing tool is detected, exitting.')
        time.sleep(3)
        sys.exit(0)
    else:
        pass

    if checkIfProcessRunning('Wireshark'):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('A network sniffing tool is detected, exitting.')
        time.sleep(3)
        sys.exit(0)
    else:
        pass

    if checkIfProcessRunning('Npcap'):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('A network sniffing tool is detected, exitting.')
        time.sleep(3)
        sys.exit(0)
    else:
        pass

    if checkIfProcessRunning('WinDump'):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('A network sniffing tool is detected, exitting.')
        time.sleep(3)
        sys.exit(0)
    else:
        pass

    if checkIfProcessRunning('NetworkMiner'):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('A network sniffing tool is detected, exitting.')
        time.sleep(3)
        sys.exit(0)
    else:
        pass

securityrun()
os.system("mode con cols=100 lines=35")

localhwid = 'test' # set to 'test' to allow for seamless development
# localhwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip() # a working way to get a constant unique hardware identifier on windows for hwid authentication purposes


tk = Tk()
tk.withdraw()

os.system('cls' if os.name == 'nt' else 'clear')

home = os.path.expanduser('~')
user_profile = home+'/Medusa'
stamp = user_profile+'/footprint.txt'
settings = user_profile+'/settings.txt'
music = user_profile+'/music.wav'
tkicon =  user_profile+'/icon.ico'

class bcolors:
    HEADER = '\033[95m'
    CYAN = '\u001b[36m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    MAGENTA = '\u001b[35m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

securitycheck = False
def securityloader():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if securitycheck:
            break
        sys.stdout.write('\rSecurity Checks... '+c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=securityloader)
t.start()

time.sleep(2)
securitycheck = True
print(f'\rSecurity Checks... {bcolors.OKGREEN}DONE{bcolors.ENDC}')
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')

loaddone = False
def animateload():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if loaddone:
            break
        sys.stdout.write('\rLoading '+c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=animateload)
t.start()

time.sleep(5)
loaddone = True

if not os.path.exists(user_profile):
    os.makedirs(user_profile)

with open(stamp,'w') as output:
  output.write("Medusa was here.")
os.system('cls' if os.name == 'nt' else 'clear')
print(f'Downloading {bcolors.OKGREEN}dependencies{bcolors.ENDC}...')
mp3file = requests.get("https://medusa.tools/music/music.wav") # remote medusa music files
with open(music,'wb') as output:
  output.write(mp3file.content)
print(f'Downloaded {bcolors.OKGREEN}dependencies{bcolors.ENDC}...')
try: 
    mixer.init()
    medusamusic=mixer.Sound(music)
    medusamusic.set_volume(0.15)
    medusamusic.play(-1)
except pygame.error:
    musicerror = True
    pass

error = """
                         ______
 _________        .---"""      """---.
:______.-':      :  .--------------.  :
| ______  |      | :                : |
|:______B:|      | |  Oops:         | |
|:______B:|      | |                | |
|:______B:|      | |  Une erreur    | |
|         |      | |  est survenue. | |
|:_____:  |      | |                | |
|    ==   |      | :                : |
|       O |      :  '--------------'  :
|       o |      :'---...______...---'
|       o |-._.-i___/'             \._
|'-.____o_|   '-.   '-...______...-'  `-._
:_________:      `.____________________   `-.___.-.
                 .'.qwertyeeeeeeeeeeee.'.      :___:
    fsc        .'.eeasdeeeeeeeeeeeeeeeee.'.
              :____________________________:
        """



def localcomboedits():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(centered)
    securityrun() 
    try: 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
            HOST = '127.0.0.1'  # The server's hostname or IP address - currently set to medusa's listener running on localhost
            PORT = 56420        # The port used by the server - currently set to medusa's listener running on localhost
            s.connect((HOST, PORT)) # connects to medusa authentication server
            s.send((localhwid.encode())) # sends hwid to medusa authentication server
            authvalue = s.recv(128).decode() # receives authentication reponse from medusa authentication server
            if authvalue == '1': # verifies medusa authentication response as successful
                logged = (f"Successfully authenticated client.\n{bcolors.ENDC}")
            if authvalue == '0':
                os.system('cls' if os.name == 'nt' else 'clear')
                print(error)
                print("\n")
                print("\n")
                print("\n")
                print("Your HWID is not authenticated or there was an error connecting to the hwid authentication server.")
                input("\nPress enter to close...")
                sys.exit(0)

            print(logged)
            def localeditone():
                print(f"{bcolors.UNDERLINE}Mass Combolist Editing:{bcolors.ENDC}")
                print(f"{bcolors.CYAN}[{bcolors.ENDC}Q{bcolors.CYAN}]{bcolors.ENDC} UHQ Editor - 3, 6, 7, 8 [EMAIL:PASS]\n")
                print(f"{bcolors.UNDERLINE}Combolist Tools:{bcolors.ENDC}")
                print(f"{bcolors.CYAN}[{bcolors.ENDC}1{bcolors.CYAN}]{bcolors.ENDC} Email to Username [EMAIL:PASS]")
                print(f"{bcolors.CYAN}[{bcolors.ENDC}2{bcolors.CYAN}]{bcolors.ENDC} Username to Email [USERNAME:PASS]")
                print(f"{bcolors.CYAN}[{bcolors.ENDC}3{bcolors.CYAN}]{bcolors.ENDC} Change Email to multiple Email Providers [EMAIL:PASS]")
                print(f"{bcolors.CYAN}[{bcolors.ENDC}4{bcolors.CYAN}]{bcolors.ENDC} Remove Special Characters from Passwords [*]")
                print(f"{bcolors.CYAN}[{bcolors.ENDC}5{bcolors.CYAN}]{bcolors.ENDC} Non-Numeric Username to Password Swap [USERNAME:PASS]")
                print(f"{bcolors.CYAN}[{bcolors.ENDC}6{bcolors.CYAN}]{bcolors.ENDC} Non-Numeric Email to Password Swap [EMAIL:PASS]")
                print(f"{bcolors.CYAN}[{bcolors.ENDC}7{bcolors.CYAN}]{bcolors.ENDC} Append Special Characters to Passwords [*]")
                print(f"{bcolors.CYAN}[{bcolors.ENDC}8{bcolors.CYAN}]{bcolors.ENDC} Invert Capitalization within Passwords [x/X]")
                print(f"\n{bcolors.UNDERLINE}Navigation Options:{bcolors.ENDC}")
                print(f"{bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.ENDC} Back to Main Menu")
                print(f"\n{bcolors.OKGREEN}What would you like to do today? {bcolors.ENDC}")

                def emailpassuhq():
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(centered)
                    if authvalue == '1':
                        etulogged = (f"Successfully authenticated.\n{bcolors.ENDC}")
                        print(etulogged)
                        time.sleep(1)
                    else:
                        print(f"{bcolors.CYAN}The safeguards state that you are {bcolors.FAIL}not authenticated{bcolors.CYAN} to use Medusa's Local Editting features.{bcolors.ENDC}")
                        print(f"{bcolors.WARNING}If you believe this is a mistake please join our support Discord Server and create a ticket.{bcolors.ENDC}")
                        print(f"\n{bcolors.OKGREEN}Press {bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.OKGREEN} to go back return to the main menu.")
                        loop = True
                        while loop:
                            failcommand = (msvcrt.getch()).decode("utf-8")
                            if failcommand.upper() == "B":
                                mainui()
                                loop = False
                            else:
                                print('Please enter a correct input.')
                                time.sleep(1)
                                emailpassuhq()


                    

                    title='Select a combolist file'
                    filetypes=['*.txt']
                    default='*.txt'
                    securityrun()
                    windowicon = requests.get("https://medusa.tools/icons/icon.ico") # remote medusa icon files
                    with open(tkicon,'wb') as output:
                        output.write(windowicon.content)
                    tk.iconbitmap(tkicon)
                    combofullpath = filedialog.askopenfilename(title = "Select a combolist file.",filetypes = (("Combolist File","*.txt"),("All files","*.*")))
                    try:
                        combopath = os.path.dirname(combofullpath)
                        comboname = os.path.basename(combopath)
                        dumpcombopath = ((os.path.splitext(combofullpath)[0])+'_dump.txt')
                        newcombopath = ((os.path.splitext(combofullpath)[0])+'_editted.txt')
                        combobytes = open(combofullpath, "rb").read(); comboencoding = chardet.detect(combobytes).get('encoding')
                        combolinesno = (sum(1 for line in open(combofullpath, encoding=comboencoding)))
                    except FileNotFoundError:
                        emailpassuhq()
                    print(f'{bcolors.OKGREEN}'+str(combolinesno)+f' {bcolors.CYAN}lines in combolist{bcolors.ENDC}')
                    with open(combofullpath,"r") as q:
                        startedit = time.time()
                        print(f'\n{bcolors.OKGREEN}Reading {bcolors.CYAN}combolist...{bcolors.ENDC}')
                        texts = q.read()
                        comboline = texts.split("\n")
                        print(f'\n{bcolors.OKGREEN}Making {bcolors.CYAN}[{bcolors.WARNING}EMAIL{bcolors.CYAN}:{bcolors.WARNING}PASS{bcolors.CYAN}] combolist UHQ...{bcolors.ENDC}')
                        combo = []
                        for i in range(combolinesno):
                            try:
                                combopair = comboline[i]
                                email, password = combopair.split(":")
                                user, domain = email.split("@")

                                titlecombopair = (email+password.title())
                                user, domain = email.split("@")
                                newemailone = str(user)+'@gmail.com'
                                newemailtwo = str(user)+'@outlook.com'
                                newemailthree = str(user)+'@yahoo.com'
                                newemailfour = str(user)+'@hotmail.com'
                                newemailfive = str(user)+'@icloud.com'
                                newusercomboone = (newemailone+':'+password)
                                newusercombotwo = (newemailtwo+':'+password)
                                newusercombothree = (newemailthree+':'+password)
                                newusercombofour = (newemailfour+':'+password)
                                newusercombofive = (newemailfive+':'+password)
                                titlenewusercomboone = (newemailone+':'+password.title())
                                titlenewusercombotwo = (newemailtwo+':'+password.title())
                                titlenewusercombothree = (newemailthree+':'+password.title())
                                titlenewusercombofour = (newemailfour+':'+password.title())
                                titlenewusercombofive = (newemailfive+':'+password.title())

                                cleanedpass = re.sub(r'[0-9]+', '', user)
                                nonnumusertopass = (email+':'+cleanedpass)
                                titlenonnumusertopass = (email+':'+cleanedpass.title())
                                #0
                                newemailpairone = str(combopair)+'@'
                                newemailpairtwo = str(combopair)+'!'
                                newemailpairthree = str(combopair)+'#'
                                newemailpairfour = str(combopair)+'$'
                                newemailpairfive = str(combopair)+'%'
                                newemailpairsix = str(combopair)+'&'
                                newemailpairseven = str(combopair)+'*'
                                #1
                                newonecomboone = str(newusercomboone)+'@'
                                newonecombotwo = str(newusercomboone)+'!'
                                newonecombothree = str(newusercomboone)+'#'
                                newonecombofour = str(newusercomboone)+'$'
                                newonecombofive = str(newusercomboone)+'%'
                                newonecombosix = str(newusercomboone)+'&'
                                newonecomboseven = str(newusercomboone)+'*'
                                #2
                                newtwocomboone = str(newusercombotwo)+'@'
                                newtwocombotwo = str(newusercombotwo)+'!'
                                newtwocombothree = str(newusercombotwo)+'#'
                                newtwocombofour = str(newusercombotwo)+'$'
                                newtwocombofive = str(newusercombotwo)+'%'
                                newtwocombosix = str(newusercombotwo)+'&'
                                newtwocomboseven = str(newusercombotwo)+'*'
                                #3
                                newthreecomboone = str(newusercombothree)+'@'
                                newthreecombotwo = str(newusercombothree)+'!'
                                newthreecombothree = str(newusercombothree)+'#'
                                newthreecombofour = str(newusercombothree)+'$'
                                newthreecombofive = str(newusercombothree)+'%'
                                newthreecombosix = str(newusercombothree)+'&'
                                newthreecomboseven = str(newusercombothree)+'*'
                                #4
                                newfourcomboone = str(newusercombofour)+'@'
                                newfourcombotwo = str(newusercombofour)+'!'
                                newfourcombothree = str(newusercombofour)+'#'
                                newfourcombofour = str(newusercombofour)+'$'
                                newfourcombofive = str(newusercombofour)+'%'
                                newfourcombosix = str(newusercombofour)+'&'
                                newfourcomboseven = str(newusercombofour)+'*'
                                #5
                                newfivecomboone = str(newusercombofive)+'@'
                                newfivecombotwo = str(newusercombofive)+'!'
                                newfivecombothree = str(newusercombofive)+'#'
                                newfivecombofive = str(newusercombofive)+'$'
                                newfivecombofive = str(newusercombofive)+'%'
                                newfivecombosix = str(newusercombofive)+'&'
                                newfivecomboseven = str(newusercombofive)+'*'

                                combo.append(newonecomboone)
                                combo.append(combopair)
                                combo.append(newonecombotwo)
                                combo.append(newonecombothree)
                                combo.append(newonecombofour)
                                combo.append(newonecombofive)
                                combo.append(newonecombosix)
                                combo.append(newonecomboseven)

                                combo.append(newtwocomboone)
                                combo.append(newtwocombotwo)
                                combo.append(newtwocombothree)
                                combo.append(newtwocombofour)
                                combo.append(newtwocombofive)
                                combo.append(newtwocombosix)
                                combo.append(newtwocomboseven)

                                combo.append(newthreecomboone)
                                combo.append(newthreecombotwo)
                                combo.append(newthreecombothree)
                                combo.append(newthreecombofour)
                                combo.append(newthreecombofive)
                                combo.append(newthreecombosix)
                                combo.append(newthreecomboseven)

                                combo.append(newemailpairone)
                                combo.append(newemailpairtwo)
                                combo.append(newemailpairthree)
                                combo.append(newemailpairfour)
                                combo.append(newemailpairfive)
                                combo.append(newemailpairsix)
                                combo.append(newemailpairseven)

                                combo.append(nonnumusertopass)
                                combo.append(newusercomboone)
                                combo.append(newusercombotwo)
                                combo.append(newusercombothree)
                                combo.append(newusercombofour)
                                combo.append(newusercombofive)

                                #x2
                                #0
                                titlenewemailpairone = str(titlecombopair)+'@'
                                titlenewemailpairtwo = str(titlecombopair)+'!'
                                titlenewemailpairthree = str(titlecombopair)+'#'
                                titlenewemailpairfour = str(titlecombopair)+'$'
                                titlenewemailpairfive = str(titlecombopair)+'%'
                                titlenewemailpairsix = str(titlecombopair)+'&'
                                titlenewemailpairseven = str(titlecombopair)+'*'
                                #1
                                titlenewonecomboone = str(titlenewusercomboone)+'@'
                                titlenewonecombotwo = str(titlenewusercomboone)+'!'
                                titlenewonecombothree = str(titlenewusercomboone)+'#'
                                titlenewonecombofour = str(titlenewusercomboone)+'$'
                                titlenewonecombofive = str(titlenewusercomboone)+'%'
                                titlenewonecombosix = str(titlenewusercomboone)+'&'
                                titlenewonecomboseven = str(titlenewusercomboone)+'*'
                                #2
                                titlenewtwocomboone = str(titlenewusercombotwo)+'@'
                                titlenewtwocombotwo = str(titlenewusercombotwo)+'!'
                                titlenewtwocombothree = str(titlenewusercombotwo)+'#'
                                titlenewtwocombofour = str(titlenewusercombotwo)+'$'
                                titlenewtwocombofive = str(titlenewusercombotwo)+'%'
                                titlenewtwocombosix = str(titlenewusercombotwo)+'&'
                                titlenewtwocomboseven = str(titlenewusercombotwo)+'*'
                                #3
                                titlenewthreecomboone = str(titlenewusercombothree)+'@'
                                titlenewthreecombotwo = str(titlenewusercombothree)+'!'
                                titlenewthreecombothree = str(titlenewusercombothree)+'#'
                                titlenewthreecombofour = str(titlenewusercombothree)+'$'
                                titlenewthreecombofive = str(titlenewusercombothree)+'%'
                                titlenewthreecombosix = str(titlenewusercombothree)+'&'
                                titlenewthreecomboseven = str(titlenewusercombothree)+'*'
                                #4
                                titlenewfourcomboone = str(titlenewusercombofour)+'@'
                                titlenewfourcombotwo = str(titlenewusercombofour)+'!'
                                titlenewfourcombothree = str(titlenewusercombofour)+'#'
                                titlenewfourcombofour = str(titlenewusercombofour)+'$'
                                titlenewfourcombofive = str(titlenewusercombofour)+'%'
                                titlenewfourcombosix = str(titlenewusercombofour)+'&'
                                titlenewfourcomboseven = str(titlenewusercombofour)+'*'
                                #5
                                titlenewfivecomboone = str(titlenewusercombofive)+'@'
                                titlenewfivecombotwo = str(titlenewusercombofive)+'!'
                                titlenewfivecombothree = str(titlenewusercombofive)+'#'
                                titlenewfivecombofive = str(titlenewusercombofive)+'$'
                                titlenewfivecombofive = str(titlenewusercombofive)+'%'
                                titlenewfivecombosix = str(titlenewusercombofive)+'&'
                                titlenewfivecomboseven = str(titlenewusercombofive)+'*'

                                combo.append(titlenewonecomboone)
                                combo.append(titlecombopair)
                                combo.append(titlenewonecombotwo)
                                combo.append(titlenewonecombothree)
                                combo.append(titlenewonecombofour)
                                combo.append(titlenewonecombofive)
                                combo.append(titlenewonecombosix)
                                combo.append(titlenewonecomboseven)

                                combo.append(titlenewtwocomboone)
                                combo.append(titlenewtwocombotwo)
                                combo.append(titlenewtwocombothree)
                                combo.append(titlenewtwocombofour)
                                combo.append(titlenewtwocombofive)
                                combo.append(titlenewtwocombosix)
                                combo.append(titlenewtwocomboseven)

                                combo.append(titlenewthreecomboone)
                                combo.append(titlenewthreecombotwo)
                                combo.append(titlenewthreecombothree)
                                combo.append(titlenewthreecombofour)
                                combo.append(titlenewthreecombofive)
                                combo.append(titlenewthreecombosix)
                                combo.append(titlenewthreecomboseven)

                                combo.append(titlenewemailpairone)
                                combo.append(titlenewemailpairtwo)
                                combo.append(titlenewemailpairthree)
                                combo.append(titlenewemailpairfour)
                                combo.append(titlenewemailpairfive)
                                combo.append(titlenewemailpairsix)
                                combo.append(titlenewemailpairseven)

                                combo.append(titlenonnumusertopass)
                                combo.append(titlenewusercomboone)
                                combo.append(titlenewusercombotwo)
                                combo.append(titlenewusercombothree)
                                combo.append(titlenewusercombofour)
                                combo.append(titlenewusercombofive)
                            except ValueError:
                                pass

                        endedit = time.time()
                        startcleanshuffle = time.time()
                        print(f'\n{bcolors.OKGREEN}Cleaning {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        cleanedcombo = list(dict.fromkeys(combo))
                        print(f'\n{bcolors.OKGREEN}Shuffling {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        shuffledcombo = random.sample(cleanedcombo, len(cleanedcombo))
                        print(f'\n{bcolors.OKGREEN}Saving {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        with open(newcombopath, mode='wt', encoding='utf-8') as myfile:
                            myfile.write('\n'.join(shuffledcombo))
                            myfile.write('\n')
                        endcleanshuffle = time.time()

                        timetakenedit = endedit - startedit
                        timetakencleanshuffle = endcleanshuffle - startcleanshuffle
                        newcombolinesno = (sum(1 for line in open(newcombopath)))
                        print(f'{bcolors.OKGREEN}\nSuccess!{bcolors.CYAN} made a [{bcolors.WARNING}EMAIL{bcolors.CYAN}:{bcolors.WARNING}PASS{bcolors.CYAN}] {bcolors.OKGREEN}'+str(combolinesno)+f'{bcolors.CYAN} lines combo into a {bcolors.CYAN}[{bcolors.WARNING}EMAIL{bcolors.CYAN}:{bcolors.WARNING}PASS{bcolors.CYAN}] {bcolors.OKGREEN}'+str(newcombolinesno)+f'{bcolors.CYAN} lines UHQ combo.{bcolors.ENDC}\n')
                        print(f'{bcolors.OKGREEN}Editting{bcolors.CYAN} the combolist took {bcolors.OKGREEN}'+str(timetakenedit)+f' seconds.{bcolors.ENDC}')
                        print(f'{bcolors.OKGREEN}Cleaning & shuffling{bcolors.CYAN} the combolist took{bcolors.OKGREEN} '+str(timetakencleanshuffle)+f' seconds.{bcolors.ENDC}')
                        print(f'{bcolors.CYAN}\nYour new UHQ [{bcolors.WARNING}EMAIL{bcolors.CYAN}:{bcolors.WARNING}PASS{bcolors.CYAN}] combolist can be found at: {bcolors.WARNING}'+str(newcombopath)+f'{bcolors.ENDC}\n')
                        time.sleep(2)
                        print(f"{bcolors.UNDERLINE}Navigation Options:{bcolors.ENDC}")
                        print(f"{bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.ENDC} Back to Local Combolist Edit Options")
                        print(f"{bcolors.CYAN}[{bcolors.ENDC}M{bcolors.CYAN}]{bcolors.ENDC} Back to Main Menu")
                        print(f"\n{bcolors.OKGREEN}What would you like to do today? {bcolors.ENDC}"); emailtouserpreference = (msvcrt.getch()).decode("utf-8")

                        if emailtouserpreference.upper() == "B":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(centered)
                            if authvalue == '1':
                                etulogged = (f"Successfully authenticated.\n{bcolors.ENDC}")
                                print(etulogged)
                                time.sleep(1)
                            else:
                                print(f"{bcolors.CYAN}The safeguards state that you are {bcolors.FAIL}not authenticated{bcolors.CYAN} to use Medusa's Local Editting features.{bcolors.ENDC}")
                                print(f"{bcolors.WARNING}If you believe this is a mistake please join our support Discord Server and create a ticket.{bcolors.ENDC}")
                                print(f"\n{bcolors.OKGREEN}Press {bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.OKGREEN} to go back return to the main menu.")
                                loop = True
                                while loop:
                                    failcommand = (msvcrt.getch()).decode("utf-8")
                                    if failcommand.upper() == "B":
                                        mainui()
                                        loop = False
                                    else:
                                        print('Please enter a correct input.')
                                        time.sleep(1)
                            localcomboedits()
                        else:
                            pass

                        if emailtouserpreference.upper() == "M":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(centered)
                            if authvalue == '1':
                                etulogged = (f"Successfully authenticated.\n{bcolors.ENDC}")
                                print(etulogged)
                                time.sleep(1)
                            else:
                                print(f"{bcolors.CYAN}The safeguards state that you are {bcolors.FAIL}not authenticated{bcolors.CYAN} to use Medusa's Local Editting features.{bcolors.ENDC}")
                                print(f"{bcolors.WARNING}If you believe this is a mistake please join our support Discord Server and create a ticket.{bcolors.ENDC}")
                                print(f"\n{bcolors.OKGREEN}Press {bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.OKGREEN} to go back return to the main menu.")
                                loop = True
                                while loop:
                                    failcommand = (msvcrt.getch()).decode("utf-8")
                                    if failcommand.upper() == "B":
                                        mainui()
                                        loop = False
                                    else:
                                        print('Please enter a correct input.')
                                        time.sleep(1)
                            mainui()
                        else:
                            pass

                def emailtouser():
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(centered)
                    if authvalue == '1':
                        etulogged = (f"Successfully authenticated.\n{bcolors.ENDC}")
                        print(etulogged)
                        time.sleep(1)
                    else:
                        print(f"{bcolors.CYAN}The safeguards state that you are {bcolors.FAIL}not authenticated{bcolors.CYAN} to use Medusa's Local Editting features.{bcolors.ENDC}")
                        print(f"{bcolors.WARNING}If you believe this is a mistake please join our support Discord Server and create a ticket.{bcolors.ENDC}")
                        print(f"\n{bcolors.OKGREEN}Press {bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.OKGREEN} to go back return to the main menu.")
                        loop = True
                        while loop:
                            failcommand = (msvcrt.getch()).decode("utf-8")
                            if failcommand.upper() == "B":
                                mainui()
                                loop = False
                            else:
                                print('Please enter a correct input.')
                                time.sleep(1)

                    

                    title='Select a combolist file'
                    filetypes=['*.txt']
                    default='*.txt'
                    securityrun()
                    windowicon = requests.get("https://medusa.tools/icons/icon.ico") # remote medusa icon files
                    with open(tkicon,'wb') as output:
                        output.write(windowicon.content)
                    tk.iconbitmap(tkicon)
                    combofullpath = filedialog.askopenfilename(title = "Select a combolist file.",filetypes = (("Combolist File","*.txt"),("All files","*.*")))
                    try:
                        combopath = os.path.dirname(combofullpath)
                        comboname = os.path.basename(combopath)
                        dumpcombopath = ((os.path.splitext(combofullpath)[0])+'_dump.txt')
                        newcombopath = ((os.path.splitext(combofullpath)[0])+'_editted.txt')
                        combobytes = open(combofullpath, "rb").read(); comboencoding = chardet.detect(combobytes).get('encoding')
                        combolinesno = (sum(1 for line in open(combofullpath, encoding=comboencoding)))
                    except FileNotFoundError:
                        emailtouser()
                    print(f'{bcolors.OKGREEN}'+str(combolinesno)+f' {bcolors.CYAN}lines in combolist{bcolors.ENDC}')
                    with open(combofullpath,"r") as q:
                        startedit = time.time()
                        print(f'\n{bcolors.OKGREEN}Reading {bcolors.CYAN}combolist...{bcolors.ENDC}')
                        texts = q.read()
                        comboline = texts.split("\n")
                        print(f'\n{bcolors.OKGREEN}Exchanging {bcolors.CYAN}combolist from {bcolors.CYAN}[{bcolors.WARNING}EMAIL{bcolors.CYAN}:{bcolors.WARNING}PASS{bcolors.CYAN}] {bcolors.CYAN}to [{bcolors.WARNING}USER{bcolors.CYAN}:{bcolors.WARNING}PASS{bcolors.CYAN}]...{bcolors.ENDC}')
                        combo = []
                        for i in range(combolinesno):
                            try:
                                combopair = comboline[i]
                                email, password = combopair.split(":")
                                emailuser, emaildomain = email.split("@")
                                newusercombo = (str(emailuser)+':'+str(password))
                                combo.append(newusercombo)
                            except ValueError:
                                pass

                        endedit = time.time()
                        startcleanshuffle = time.time()
                        print(f'\n{bcolors.OKGREEN}Cleaning {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        cleanedcombo = list(dict.fromkeys(combo))
                        print(f'\n{bcolors.OKGREEN}Shuffling {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        shuffledcombo = random.sample(cleanedcombo, len(cleanedcombo))
                        print(f'\n{bcolors.OKGREEN}Saving {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        with open(newcombopath, mode='wt', encoding='utf-8') as myfile:
                            myfile.write('\n'.join(shuffledcombo))
                            myfile.write('\n')
                        endcleanshuffle = time.time()

                        timetakenedit = endedit - startedit
                        timetakencleanshuffle = endcleanshuffle - startcleanshuffle
                        newcombolinesno = (sum(1 for line in open(newcombopath)))
                        print(f'{bcolors.OKGREEN}\nSuccess!{bcolors.CYAN} editted a [{bcolors.WARNING}EMAIL{bcolors.CYAN}:{bcolors.WARNING}PASS{bcolors.CYAN}] {bcolors.OKGREEN}'+str(combolinesno)+f'{bcolors.CYAN} lines combo into a {bcolors.CYAN}[{bcolors.WARNING}USER{bcolors.CYAN}:{bcolors.WARNING}PASS{bcolors.CYAN}] {bcolors.OKGREEN}'+str(newcombolinesno)+f'{bcolors.CYAN} lines combo.{bcolors.ENDC}\n')
                        print(f'{bcolors.OKGREEN}Editting{bcolors.CYAN} the combolist took {bcolors.OKGREEN}'+str(timetakenedit)+f' seconds.{bcolors.ENDC}')
                        print(f'{bcolors.OKGREEN}Cleaning & shuffling{bcolors.CYAN} the combolist took{bcolors.OKGREEN} '+str(timetakencleanshuffle)+f' seconds.{bcolors.ENDC}')
                        print(f'{bcolors.CYAN}\nYour new [{bcolors.WARNING}USER{bcolors.CYAN}:{bcolors.WARNING}PASS{bcolors.CYAN}] combolist can be found at: {bcolors.WARNING}'+str(newcombopath)+f'{bcolors.ENDC}\n')
                        time.sleep(2)
                        print(f"{bcolors.UNDERLINE}Navigation Options:{bcolors.ENDC}")
                        print(f"{bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.ENDC} Back to Local Combolist Edit Options")
                        print(f"{bcolors.CYAN}[{bcolors.ENDC}M{bcolors.CYAN}]{bcolors.ENDC} Back to Main Menu")
                        print(f"\n{bcolors.OKGREEN}What would you like to do today? {bcolors.ENDC}"); emailtouserpreference = (msvcrt.getch()).decode("utf-8")

                        if emailtouserpreference.upper() == "M":
                            mainui()
                        else:
                            pass

                        if emailtouserpreference.upper() == "B":
                            localcomboedits()
                        else:
                            pass

                def addemailstoemail():
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(centered)
                    if authvalue == '1':
                        etulogged = (f"Successfully authenticated.\n{bcolors.ENDC}")
                        print(etulogged)
                        time.sleep(1)
                    else:
                        print(f"{bcolors.CYAN}The safeguards state that you are {bcolors.FAIL}not authenticated{bcolors.CYAN} to use Medusa's Local Editting features.{bcolors.ENDC}")
                        print(f"{bcolors.WARNING}If you believe this is a mistake please join our support Discord Server and create a ticket.{bcolors.ENDC}")
                        print(f"\n{bcolors.OKGREEN}Press {bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.OKGREEN} to go back return to the main menu.")
                        loop = True
                        while loop:
                            failcommand = (msvcrt.getch()).decode("utf-8")
                            if failcommand.upper() == "B":
                                mainui()
                                loop = False
                            else:
                                print('Please enter a correct input.')
                                time.sleep(1)
                                addemailstoemail()

                    

                    title='Select a combolist file'
                    filetypes=['*.txt']
                    default='*.txt'
                    securityrun()
                    windowicon = requests.get("https://medusa.tools/icons/icon.ico") # remote medusa icon files
                    with open(tkicon,'wb') as output:
                        output.write(windowicon.content)


                    tk.iconbitmap(tkicon)
                    combofullpath = filedialog.askopenfilename(title = "Select a combolist file.",filetypes = (("Combolist File","*.txt"),("All files","*.*")))
                    try:
                        combopath = os.path.dirname(combofullpath)
                        comboname = os.path.basename(combopath)
                        dumpcombopath = ((os.path.splitext(combofullpath)[0])+'_dump.txt')
                        newcombopath = ((os.path.splitext(combofullpath)[0])+'_editted.txt')
                        combobytes = open(combofullpath, "rb").read(); comboencoding = chardet.detect(combobytes).get('encoding')
                        combolinesno = (sum(1 for line in open(combofullpath, encoding=comboencoding)))
                    except FileNotFoundError:
                        addemailstoemail()
                    print(f'{bcolors.OKGREEN}'+str(combolinesno)+f' {bcolors.CYAN}lines in combolist{bcolors.ENDC}')
                    with open(combofullpath,"r") as f:
                        startedit = time.time()
                        print(f'\n{bcolors.OKGREEN}Reading {bcolors.CYAN}combolist...{bcolors.ENDC}')
                        texts = f.read()
                        comboline = texts.split("\n")
                        print(f'\n{bcolors.OKGREEN}Adding {bcolors.CYAN}multiple email providers to a {bcolors.CYAN}[{bcolors.WARNING}EMAIL{bcolors.CYAN}:{bcolors.WARNING}PASS{bcolors.CYAN}] combolist...{bcolors.ENDC}')
                        combo = []
                        for i in range(combolinesno):
                            try:
                                combopair = comboline[i]
                                email, password = combopair.split(":")
                                emailuser, emaildomain = email.split("@")
                                newemailone = str(emailuser)+'@gmail.com'
                                newemailtwo = str(emailuser)+'@outlook.com'
                                newemailthree = str(emailuser)+'@yahoo.com'
                                newemailfour = str(emailuser)+'@hotmail.com'
                                newemailfive = str(emailuser)+'@icloud.com'
                                newusercomboone = (newemailone+':'+password)
                                newusercombotwo = (newemailtwo+':'+password)
                                newusercombothree = (newemailthree+':'+password)
                                newusercombofour = (newemailfour+':'+password)
                                newusercombofive = (newemailfive+':'+password)
                                combo.append(newusercomboone)
                                combo.append(newusercombotwo)
                                combo.append(newusercombothree)
                                combo.append(newusercombofour)
                                combo.append(newusercombofive)
                            except ValueError:
                                pass
                        endedit = time.time()
                        startcleanshuffle = time.time()
                        print(f'\n{bcolors.OKGREEN}Cleaning {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        cleanedcombo = list(dict.fromkeys(combo))
                        print(f'\n{bcolors.OKGREEN}Shuffling {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        shuffledcombo = random.sample(cleanedcombo, len(cleanedcombo))
                        print(f'\n{bcolors.OKGREEN}Saving {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        with open(newcombopath, mode='wt', encoding='utf-8') as myfile:
                            myfile.write('\n'.join(shuffledcombo))
                            myfile.write('\n')
                        endcleanshuffle = time.time()

                        timetakenedit = endedit - startedit
                        timetakencleanshuffle = endcleanshuffle - startcleanshuffle
                        newcombolinesno = (sum(1 for line in open(newcombopath)))
                        print(f'{bcolors.OKGREEN}\nSuccess!{bcolors.CYAN} added multiple email providers to a [{bcolors.WARNING}EMAIL{bcolors.CYAN}:{bcolors.WARNING}PASS{bcolors.CYAN}] {bcolors.OKGREEN}'+str(combolinesno)+f'{bcolors.CYAN} lines combo, turning it into a {bcolors.CYAN}[{bcolors.WARNING}EMAIL{bcolors.CYAN}:{bcolors.WARNING}PASS{bcolors.CYAN}] {bcolors.OKGREEN}'+str(newcombolinesno)+f'{bcolors.CYAN} lines combo.{bcolors.ENDC}\n')
                        print(f'{bcolors.OKGREEN}Editting{bcolors.CYAN} the combolist took {bcolors.OKGREEN}'+str(timetakenedit)+f' seconds.{bcolors.ENDC}')
                        print(f'{bcolors.OKGREEN}Cleaning & shuffling{bcolors.CYAN} the combolist took{bcolors.OKGREEN} '+str(timetakencleanshuffle)+f' seconds.{bcolors.ENDC}')
                        print(f'{bcolors.CYAN}\nYour new [{bcolors.WARNING}EMAIL{bcolors.CYAN}:{bcolors.WARNING}PASS{bcolors.CYAN}] combolist can be found at: {bcolors.WARNING}'+str(newcombopath)+f'{bcolors.ENDC}\n')
                        time.sleep(2)
                        print(f"{bcolors.UNDERLINE}Navigation Options:{bcolors.ENDC}")
                        print(f"{bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.ENDC} Back to Local Combolist Edit Options")
                        print(f"{bcolors.CYAN}[{bcolors.ENDC}M{bcolors.CYAN}]{bcolors.ENDC} Back to Main Menu")
                        print(f"\n{bcolors.OKGREEN}What would you like to do today? {bcolors.ENDC}"); usertoemailpreference = (msvcrt.getch()).decode("utf-8")

                        if usertoemailpreference.upper() == "M":
                            mainui()
                        else:
                            pass

                        if usertoemailpreference.upper() == "B":
                            localcomboedits()
                        else:
                            pass

                def usertoemail():
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(centered)
                    if authvalue == '1':
                        etulogged = (f"Successfully authenticated.\n{bcolors.ENDC}")
                        print(etulogged)
                        time.sleep(1)
                    else:
                        print(f"{bcolors.CYAN}The safeguards state that you are {bcolors.FAIL}not authenticated{bcolors.CYAN} to use Medusa's Local Editting features.{bcolors.ENDC}")
                        print(f"{bcolors.WARNING}If you believe this is a mistake please join our support Discord Server and create a ticket.{bcolors.ENDC}")
                        print(f"\n{bcolors.OKGREEN}Press {bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.OKGREEN} to go back return to the main menu.")
                        loop = True
                        while loop:
                            failcommand = (msvcrt.getch()).decode("utf-8")
                            if failcommand.upper() == "B":
                                mainui()
                                loop = False
                            else:
                                print('Please enter a correct input.')
                                time.sleep(1)
                                usertoemail()

                    

                    title='Select a combolist file'
                    filetypes=['*.txt']
                    default='*.txt'

                    securityrun()
                    windowicon = requests.get("https://medusa.tools/icons/icon.ico") # remote medusa icon files
                    with open(tkicon,'wb') as output:
                        output.write(windowicon.content)
                    tk.iconbitmap(tkicon)
                    combofullpath = filedialog.askopenfilename(title = "Select a combolist file.",filetypes = (("Combolist File","*.txt"),("All files","*.*")))
                    try:
                        combopath = os.path.dirname(combofullpath)
                        comboname = os.path.basename(combopath)
                        dumpcombopath = ((os.path.splitext(combofullpath)[0])+'_dump.txt')
                        newcombopath = ((os.path.splitext(combofullpath)[0])+'_editted.txt')
                        combobytes = open(combofullpath, "rb").read(); comboencoding = chardet.detect(combobytes).get('encoding')
                        combolinesno = (sum(1 for line in open(combofullpath, encoding=comboencoding)))
                    except FileNotFoundError:
                        usertoemail()
                    print(f'{bcolors.OKGREEN}'+str(combolinesno)+f' {bcolors.CYAN}lines in combolist{bcolors.ENDC}')
                    with open(combofullpath,"r") as q:
                        startedit = time.time()
                        print(f'\n{bcolors.OKGREEN}Reading {bcolors.CYAN}combolist...{bcolors.ENDC}')
                        texts = q.read()
                        comboline = texts.split("\n")
                        print(f'\n{bcolors.OKGREEN}Exchanging {bcolors.CYAN}combolist from {bcolors.CYAN}[{bcolors.WARNING}USER{bcolors.CYAN}:{bcolors.WARNING}PASS{bcolors.CYAN}] {bcolors.CYAN}to [{bcolors.WARNING}EMAIL{bcolors.CYAN}:{bcolors.WARNING}PASS{bcolors.CYAN}]...{bcolors.ENDC}')
                        combo = []
                        for i in range(combolinesno):
                            try:
                                combopair = comboline[i]
                                user, password = combopair.split(":")
                                newemailone = str(user)+'@gmail.com'
                                newemailtwo = str(user)+'@outlook.com'
                                newemailthree = str(user)+'@yahoo.com'
                                newemailfour = str(user)+'@hotmail.com'
                                newemailfive = str(user)+'@icloud.com'
                                newusercomboone = (newemailone+':'+password)
                                newusercombotwo = (newemailtwo+':'+password)
                                newusercombothree = (newemailthree+':'+password)
                                newusercombofour = (newemailfour+':'+password)
                                newusercombofive = (newemailfive+':'+password)
                                combo.append(newusercomboone)
                                combo.append(newusercombotwo)
                                combo.append(newusercombothree)
                                combo.append(newusercombofour)
                                combo.append(newusercombofive)
                            except ValueError:
                                pass

                        endedit = time.time()
                        startcleanshuffle = time.time()
                        print(f'\n{bcolors.OKGREEN}Cleaning {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        cleanedcombo = list(dict.fromkeys(combo))
                        print(f'\n{bcolors.OKGREEN}Shuffling {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        shuffledcombo = random.sample(cleanedcombo, len(cleanedcombo))
                        print(f'\n{bcolors.OKGREEN}Saving {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        with open(newcombopath, mode='wt', encoding='utf-8') as myfile:
                            myfile.write('\n'.join(shuffledcombo))
                            myfile.write('\n')
                        endcleanshuffle = time.time()

                        timetakenedit = endedit - startedit
                        timetakencleanshuffle = endcleanshuffle - startcleanshuffle
                        newcombolinesno = (sum(1 for line in open(newcombopath)))
                        print(f'{bcolors.OKGREEN}\nSuccess!{bcolors.CYAN} editted a [{bcolors.WARNING}USER{bcolors.CYAN}:{bcolors.WARNING}PASS{bcolors.CYAN}] {bcolors.OKGREEN}'+str(combolinesno)+f'{bcolors.CYAN} lines combo into a {bcolors.CYAN}[{bcolors.WARNING}EMAIL{bcolors.CYAN}:{bcolors.WARNING}PASS{bcolors.CYAN}] {bcolors.OKGREEN}'+str(newcombolinesno)+f'{bcolors.CYAN} lines combo.{bcolors.ENDC}\n')
                        print(f'{bcolors.OKGREEN}Editting{bcolors.CYAN} the combolist took {bcolors.OKGREEN}'+str(timetakenedit)+f' seconds.{bcolors.ENDC}')
                        print(f'{bcolors.OKGREEN}Cleaning & shuffling{bcolors.CYAN} the combolist took{bcolors.OKGREEN} '+str(timetakencleanshuffle)+f' seconds.{bcolors.ENDC}')
                        print(f'{bcolors.CYAN}\nYour new [{bcolors.WARNING}USER{bcolors.CYAN}:{bcolors.WARNING}PASS{bcolors.CYAN}] combolist can be found at: {bcolors.WARNING}'+str(newcombopath)+f'{bcolors.ENDC}\n')
                        time.sleep(2)
                        print(f"{bcolors.UNDERLINE}Navigation Options:{bcolors.ENDC}")
                        print(f"{bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.ENDC} Back to Local Combolist Edit Options")
                        print(f"{bcolors.CYAN}[{bcolors.ENDC}M{bcolors.CYAN}]{bcolors.ENDC} Back to Main Menu")
                        print(f"\n{bcolors.OKGREEN}What would you like to do today? {bcolors.ENDC}"); emailtouserpreference = (msvcrt.getch()).decode("utf-8")

                        if emailtouserpreference.upper() == "M":
                            mainui()
                        else:
                            pass

                        if emailtouserpreference.upper() == "B":
                            localcomboedits()
                        else:
                            pass


                def removespecialchars():
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(centered)
                    if authvalue == '1':
                        etulogged = (f"Successfully authenticated.\n{bcolors.ENDC}")
                        print(etulogged)
                        time.sleep(1)
                    else:
                        print(f"{bcolors.CYAN}The safeguards state that you are {bcolors.FAIL}not authenticated{bcolors.CYAN} to use Medusa's Local Editting features.{bcolors.ENDC}")
                        print(f"{bcolors.WARNING}If you believe this is a mistake please join our support Discord Server and create a ticket.{bcolors.ENDC}")
                        print(f"\n{bcolors.OKGREEN}Press {bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.OKGREEN} to go back return to the main menu.")
                        loop = True
                        while loop:
                            failcommand = (msvcrt.getch()).decode("utf-8")
                            if failcommand.upper() == "B":
                                mainui()
                                loop = False
                            else:
                                print('Please enter a correct input.')
                                time.sleep(1)
                                removespecialchars()

                    

                    title='Select a combolist file'
                    filetypes=['*.txt']
                    default='*.txt'
                    securityrun()
                    windowicon = requests.get("https://medusa.tools/icons/icon.ico") # remote medusa icon files
                    with open(tkicon,'wb') as output:
                        output.write(windowicon.content)
                    tk.iconbitmap(tkicon)
                    combofullpath = filedialog.askopenfilename(title = "Select a combolist file.",filetypes = (("Combolist File","*.txt"),("All files","*.*")))
                    try:
                        combopath = os.path.dirname(combofullpath)
                        comboname = os.path.basename(combopath)
                        dumpcombopath = ((os.path.splitext(combofullpath)[0])+'_dump.txt')
                        newcombopath = ((os.path.splitext(combofullpath)[0])+'_editted.txt')
                        combobytes = open(combofullpath, "rb").read(); comboencoding = chardet.detect(combobytes).get('encoding')
                        combolinesno = (sum(1 for line in open(combofullpath, encoding=comboencoding)))
                    except FileNotFoundError:
                        removespecialchars()
                    print(f'{bcolors.OKGREEN}'+str(combolinesno)+f' {bcolors.CYAN}lines in combolist{bcolors.ENDC}')
                    with open(combofullpath,"r") as q:
                        startedit = time.time()
                        print(f'\n{bcolors.OKGREEN}Reading {bcolors.CYAN}combolist...{bcolors.ENDC}')
                        texts = q.read()
                        comboline = texts.split("\n")
                        print(f'\n{bcolors.OKGREEN}Removing {bcolors.CYAN}any special characters within passwords inside of this combolist... {bcolors.ENDC}')
                        combo = []
                        for i in range(combolinesno):
                            try:
                                combopair = comboline[i]
                                email, password = combopair.split(":")
                                cleanedpass = re.sub('[^a-zA-Z0-9 \n\.]', '', password)
                                newcomboline = (email+':'+cleanedpass)
                                combo.append(newcomboline)
                            except ValueError:
                                pass

                        endedit = time.time()
                        startcleanshuffle = time.time()
                        print(f'\n{bcolors.OKGREEN}Cleaning {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        cleanedcombo = list(dict.fromkeys(combo))
                        print(f'\n{bcolors.OKGREEN}Shuffling {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        shuffledcombo = random.sample(cleanedcombo, len(cleanedcombo))
                        print(f'\n{bcolors.OKGREEN}Saving {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        with open(newcombopath, mode='wt', encoding='utf-8') as myfile:
                            myfile.write('\n'.join(shuffledcombo))
                            myfile.write('\n')
                        endcleanshuffle = time.time()

                        timetakenedit = endedit - startedit
                        timetakencleanshuffle = endcleanshuffle - startcleanshuffle
                        newcombolinesno = (sum(1 for line in open(newcombopath)))
                        print(f'{bcolors.OKGREEN}\nSuccess!{bcolors.CYAN} removed any special characters within passwords inside of the {bcolors.OKGREEN}'+str(combolinesno)+f'{bcolors.CYAN} lines combo, turning it into a {bcolors.OKGREEN}'+str(newcombolinesno)+f'{bcolors.CYAN} lines combo.{bcolors.ENDC}\n')
                        print(f'{bcolors.OKGREEN}Editting{bcolors.CYAN} the combolist took {bcolors.OKGREEN}'+str(timetakenedit)+f' seconds.{bcolors.ENDC}')
                        print(f'{bcolors.OKGREEN}Cleaning & shuffling{bcolors.CYAN} the combolist took{bcolors.OKGREEN} '+str(timetakencleanshuffle)+f' seconds.{bcolors.ENDC}')
                        print(f'{bcolors.CYAN}\nYour new combolist can be found at: {bcolors.WARNING}'+str(newcombopath)+f'{bcolors.ENDC}\n')
                        time.sleep(2)
                        print(f"{bcolors.UNDERLINE}Navigation Options:{bcolors.ENDC}")
                        print(f"{bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.ENDC} Back to Local Combolist Edit Options")
                        print(f"{bcolors.CYAN}[{bcolors.ENDC}M{bcolors.CYAN}]{bcolors.ENDC} Back to Main Menu")
                        print(f"\n{bcolors.OKGREEN}What would you like to do today? {bcolors.ENDC}"); emailtouserpreference = (msvcrt.getch()).decode("utf-8")

                        if emailtouserpreference.upper() == "M":
                            mainui()
                        else:
                            pass

                        if emailtouserpreference.upper() == "B":
                            localcomboedits()
                        else:
                            pass

                def nonnumericuser():
                    
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(centered)
                    if authvalue == '1':
                        etulogged = (f"Successfully authenticated.\n{bcolors.ENDC}")
                        print(etulogged)
                        time.sleep(1)
                    else:
                        print(f"{bcolors.CYAN}The safeguards state that you are {bcolors.FAIL}not authenticated{bcolors.CYAN} to use Medusa's Local Editting features.{bcolors.ENDC}")
                        print(f"{bcolors.WARNING}If you believe this is a mistake please join our support Discord Server and create a ticket.{bcolors.ENDC}")
                        print(f"\n{bcolors.OKGREEN}Press {bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.OKGREEN} to go back return to the main menu.")
                        loop = True
                        while loop:
                            failcommand = (msvcrt.getch()).decode("utf-8")
                            if failcommand.upper() == "B":
                                mainui()
                                loop = False
                            else:
                                print('Please enter a correct input.')
                                time.sleep(1)
                                nonnumericuser()

                    

                    title='Select a combolist file'
                    filetypes=['*.txt']
                    default='*.txt'
                    securityrun()
                    windowicon = requests.get("https://medusa.tools/icons/icon.ico") # remote medusa icon files
                    with open(tkicon,'wb') as output:
                        output.write(windowicon.content)
                    tk.iconbitmap(tkicon)
                    combofullpath = filedialog.askopenfilename(title = "Select a combolist file.",filetypes = (("Combolist File","*.txt"),("All files","*.*")))
                    try:
                        combopath = os.path.dirname(combofullpath)
                        comboname = os.path.basename(combopath)
                        dumpcombopath = ((os.path.splitext(combofullpath)[0])+'_dump.txt')
                        newcombopath = ((os.path.splitext(combofullpath)[0])+'_editted.txt')
                        combobytes = open(combofullpath, "rb").read(); comboencoding = chardet.detect(combobytes).get('encoding')
                        combolinesno = (sum(1 for line in open(combofullpath, encoding=comboencoding)))
                    except FileNotFoundError:
                        nonnumericuser()
                    print(f'{bcolors.OKGREEN}'+str(combolinesno)+f' {bcolors.CYAN}lines in combolist{bcolors.ENDC}')
                    with open(combofullpath,"r") as q:
                        startedit = time.time()
                        print(f'\n{bcolors.OKGREEN}Reading {bcolors.CYAN}combolist...{bcolors.ENDC}')
                        texts = q.read()
                        comboline = texts.split("\n")
                        print(f'\n{bcolors.OKGREEN}Exchanging {bcolors.CYAN}non-numeric {bcolors.WARNING}usernames{bcolors.CYAN} to passwords within this [{bcolors.WARNING}USER{bcolors.CYAN}:{bcolors.WARNING}PASS{bcolors.CYAN}] combolist...{bcolors.ENDC}')
                        combo = []
                        for i in range(combolinesno):
                            try:
                                combopair = comboline[i]
                                username, password = combopair.split(":")
                                cleanedpass = re.sub(r'[0-9]+', '', username)
                                newcomboline = (username+':'+cleanedpass)
                                combo.append(newcomboline)
                            except ValueError:
                                pass

                        endedit = time.time()
                        startcleanshuffle = time.time()
                        print(f'\n{bcolors.OKGREEN}Cleaning {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        cleanedcombo = list(dict.fromkeys(combo))
                        print(f'\n{bcolors.OKGREEN}Shuffling {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        shuffledcombo = random.sample(cleanedcombo, len(cleanedcombo))
                        print(f'\n{bcolors.OKGREEN}Saving {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        with open(newcombopath, mode='wt', encoding='utf-8') as myfile:
                            myfile.write('\n'.join(shuffledcombo))
                            myfile.write('\n')
                        endcleanshuffle = time.time()

                        timetakenedit = endedit - startedit
                        timetakencleanshuffle = endcleanshuffle - startcleanshuffle
                        newcombolinesno = (sum(1 for line in open(newcombopath)))
                        print(f'{bcolors.OKGREEN}\nSuccess!{bcolors.CYAN} exchanged {bcolors.CYAN}non-numeric {bcolors.WARNING}usernames{bcolors.CYAN} to passwords within this [{bcolors.WARNING}USER{bcolors.CYAN}:{bcolors.WARNING}PASS{bcolors.CYAN}] {bcolors.OKGREEN}'+str(combolinesno)+f'{bcolors.CYAN} lines combo, turning it into a {bcolors.OKGREEN}'+str(newcombolinesno)+f'{bcolors.CYAN} lines combo.{bcolors.ENDC}\n')
                        print(f'{bcolors.OKGREEN}Editting{bcolors.CYAN} the combolist took {bcolors.OKGREEN}'+str(timetakenedit)+f' seconds.{bcolors.ENDC}')
                        print(f'{bcolors.OKGREEN}Cleaning & shuffling{bcolors.CYAN} the combolist took{bcolors.OKGREEN} '+str(timetakencleanshuffle)+f' seconds.{bcolors.ENDC}')
                        print(f'{bcolors.CYAN}\nYour new combolist can be found at: {bcolors.WARNING}'+str(newcombopath)+f'{bcolors.ENDC}\n')
                        time.sleep(2)
                        print(f"{bcolors.UNDERLINE}Navigation Options:{bcolors.ENDC}")
                        print(f"{bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.ENDC} Back to Local Combolist Edit Options")
                        print(f"{bcolors.CYAN}[{bcolors.ENDC}M{bcolors.CYAN}]{bcolors.ENDC} Back to Main Menu")
                        print(f"\n{bcolors.OKGREEN}What would you like to do today? {bcolors.ENDC}"); emailtouserpreference = (msvcrt.getch()).decode("utf-8")

                        if emailtouserpreference.upper() == "M":
                            mainui()
                        else:
                            pass

                        if emailtouserpreference.upper() == "B":
                            localcomboedits()
                        else:
                            pass


                def nonnumericemail():
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(centered)
                    if authvalue == '1':
                        etulogged = (f"Successfully authenticated.\n{bcolors.ENDC}")
                        print(etulogged)
                        time.sleep(1)
                    else:
                        print(f"{bcolors.CYAN}The safeguards state that you are {bcolors.FAIL}not authenticated{bcolors.CYAN} to use Medusa's Local Editting features.{bcolors.ENDC}")
                        print(f"{bcolors.WARNING}If you believe this is a mistake please join our support Discord Server and create a ticket.{bcolors.ENDC}")
                        print(f"\n{bcolors.OKGREEN}Press {bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.OKGREEN} to go back return to the main menu.")
                        loop = True
                        while loop:
                            failcommand = (msvcrt.getch()).decode("utf-8")
                            if failcommand.upper() == "B":
                                mainui()
                                loop = False
                            else:
                                print('Please enter a correct input.')
                                time.sleep(1)
                                nonnumericemail()

                    

                    title='Select a combolist file'
                    filetypes=['*.txt']
                    default='*.txt'
                    securityrun()
                    windowicon = requests.get("https://medusa.tools/icons/icon.ico") # remote medusa icon files
                    with open(tkicon,'wb') as output:
                        output.write(windowicon.content)
                    tk.iconbitmap(tkicon)
                    combofullpath = filedialog.askopenfilename(title = "Select a combolist file.",filetypes = (("Combolist File","*.txt"),("All files","*.*")))
                    try:
                        combopath = os.path.dirname(combofullpath)
                        comboname = os.path.basename(combopath)
                        dumpcombopath = ((os.path.splitext(combofullpath)[0])+'_dump.txt')
                        newcombopath = ((os.path.splitext(combofullpath)[0])+'_editted.txt')
                        combobytes = open(combofullpath, "rb").read(); comboencoding = chardet.detect(combobytes).get('encoding')
                        combolinesno = (sum(1 for line in open(combofullpath, encoding=comboencoding)))
                    except FileNotFoundError:
                        nonnumericemail()
                    print(f'{bcolors.OKGREEN}'+str(combolinesno)+f' {bcolors.CYAN}lines in combolist{bcolors.ENDC}')
                    with open(combofullpath,"r") as q:
                        startedit = time.time()
                        print(f'\n{bcolors.OKGREEN}Reading {bcolors.CYAN}combolist...{bcolors.ENDC}')
                        texts = q.read()
                        comboline = texts.split("\n")
                        print(f'\n{bcolors.OKGREEN}Exchanging {bcolors.CYAN}non-numeric {bcolors.WARNING}email usernames{bcolors.CYAN} to passwords within this [{bcolors.WARNING}EMAIL{bcolors.CYAN}:{bcolors.WARNING}PASS{bcolors.CYAN}] combolist...{bcolors.ENDC}')
                        combo = []
                        for i in range(combolinesno):
                            try:
                                combopair = comboline[i]
                                email, password = combopair.split(":")
                                emailuser, emaildomain = email.split("@")
                                cleanedpass = re.sub(r'[0-9]+', '', emailuser)
                                newcomboline = (email+':'+cleanedpass)
                                combo.append(newcomboline)
                            except ValueError:
                                pass

                        endedit = time.time()
                        startcleanshuffle = time.time()
                        print(f'\n{bcolors.OKGREEN}Cleaning {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        cleanedcombo = list(dict.fromkeys(combo))
                        print(f'\n{bcolors.OKGREEN}Shuffling {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        shuffledcombo = random.sample(cleanedcombo, len(cleanedcombo))
                        print(f'\n{bcolors.OKGREEN}Saving {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        with open(newcombopath, mode='wt', encoding='utf-8') as myfile:
                            myfile.write('\n'.join(shuffledcombo))
                            myfile.write('\n')
                        endcleanshuffle = time.time()

                        timetakenedit = endedit - startedit
                        timetakencleanshuffle = endcleanshuffle - startcleanshuffle
                        newcombolinesno = (sum(1 for line in open(newcombopath)))
                        print(f'{bcolors.OKGREEN}\nSuccess!{bcolors.CYAN} exchanged {bcolors.CYAN}non-numeric {bcolors.WARNING}email usernames{bcolors.CYAN} to passwords within this [{bcolors.WARNING}EMAIL{bcolors.CYAN}:{bcolors.WARNING}PASS{bcolors.CYAN}] {bcolors.OKGREEN}'+str(combolinesno)+f'{bcolors.CYAN} lines combo, turning it into a {bcolors.OKGREEN}'+str(newcombolinesno)+f'{bcolors.CYAN} lines combo.{bcolors.ENDC}\n')
                        print(f'{bcolors.OKGREEN}Editting{bcolors.CYAN} the combolist took {bcolors.OKGREEN}'+str(timetakenedit)+f' seconds.{bcolors.ENDC}')
                        print(f'{bcolors.OKGREEN}Cleaning & shuffling{bcolors.CYAN} the combolist took{bcolors.OKGREEN} '+str(timetakencleanshuffle)+f' seconds.{bcolors.ENDC}')
                        print(f'{bcolors.CYAN}\nYour new combolist can be found at: {bcolors.WARNING}'+str(newcombopath)+f'{bcolors.ENDC}\n')
                        time.sleep(2)
                        print(f"{bcolors.UNDERLINE}Navigation Options:{bcolors.ENDC}")
                        print(f"{bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.ENDC} Back to Local Combolist Edit Options")
                        print(f"{bcolors.CYAN}[{bcolors.ENDC}M{bcolors.CYAN}]{bcolors.ENDC} Back to Main Menu")
                        print(f"\n{bcolors.OKGREEN}What would you like to do today? {bcolors.ENDC}"); emailtouserpreference = (msvcrt.getch()).decode("utf-8")

                        if emailtouserpreference.upper() == "M":
                            mainui()
                        else:
                            pass

                        if emailtouserpreference.upper() == "B":
                            localcomboedits()
                        else:
                            pass


                def appendspecialpass():
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(centered)
                    if authvalue == '1':
                        etulogged = (f"Successfully authenticated.\n{bcolors.ENDC}")
                        print(etulogged)
                        time.sleep(1)
                    else:
                        print(f"{bcolors.CYAN}The safeguards state that you are {bcolors.FAIL}not authenticated{bcolors.CYAN} to use Medusa's Local Editting features.{bcolors.ENDC}")
                        print(f"{bcolors.WARNING}If you believe this is a mistake please join our support Discord Server and create a ticket.{bcolors.ENDC}")
                        print(f"\n{bcolors.OKGREEN}Press {bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.OKGREEN} to go back return to the main menu.")
                        loop = True
                        while loop:
                            failcommand = (msvcrt.getch()).decode("utf-8")
                            if failcommand.upper() == "B":
                                mainui()
                                loop = False
                            else:
                                print('Please enter a correct input.')
                                time.sleep(1)
                                appendspecialpass()

                    

                    title='Select a combolist file'
                    filetypes=['*.txt']
                    default='*.txt'
                    securityrun()
                    windowicon = requests.get("https://medusa.tools/icons/icon.ico") # remote medusa icon files
                    with open(tkicon,'wb') as output:
                        output.write(windowicon.content)
                    tk.iconbitmap(tkicon)
                    combofullpath = filedialog.askopenfilename(title = "Select a combolist file.",filetypes = (("Combolist File","*.txt"),("All files","*.*")))
                    try:
                        combopath = os.path.dirname(combofullpath)
                        comboname = os.path.basename(combopath)
                        dumpcombopath = ((os.path.splitext(combofullpath)[0])+'_dump.txt')
                        newcombopath = ((os.path.splitext(combofullpath)[0])+'_editted.txt')
                        combobytes = open(combofullpath, "rb").read(); comboencoding = chardet.detect(combobytes).get('encoding')
                        combolinesno = (sum(1 for line in open(combofullpath, encoding=comboencoding)))
                    except FileNotFoundError:
                        appendspecialpass()
                    print(f'{bcolors.OKGREEN}'+str(combolinesno)+f' {bcolors.CYAN}lines in combolist{bcolors.ENDC}')
                    with open(combofullpath,"r") as q:
                        startedit = time.time()
                        print(f'\n{bcolors.OKGREEN}Reading {bcolors.CYAN}combolist...{bcolors.ENDC}')
                        texts = q.read()
                        comboline = texts.split("\n")
                        print(f'\n{bcolors.OKGREEN}Appending {bcolors.CYAN}special characters to the end of passwords within this combolist...{bcolors.ENDC}')
                        combo = []
                        for i in range(combolinesno):
                            try:
                                combopair = comboline[i]
                                useremail, password = combopair.split(":")
                                newemailone = str(combopair)+'@'
                                newemailtwo = str(combopair)+'!'
                                newemailthree = str(combopair)+'#'
                                newemailfour = str(combopair)+'$'
                                newemailfive = str(combopair)+'%'
                                newemailsix = str(combopair)+'&'
                                newemailseven = str(combopair)+'*'
                                combo.append(newemailone)
                                combo.append(newemailtwo)
                                combo.append(newemailthree)
                                combo.append(newemailfour)
                                combo.append(newemailfive)
                                combo.append(newemailsix)
                                combo.append(newemailseven)
                                combo.append(combopair)
                            except ValueError:
                                pass

                        endedit = time.time()
                        startcleanshuffle = time.time()
                        print(f'\n{bcolors.OKGREEN}Cleaning {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        cleanedcombo = list(dict.fromkeys(combo))
                        print(f'\n{bcolors.OKGREEN}Shuffling {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        shuffledcombo = random.sample(cleanedcombo, len(cleanedcombo))
                        print(f'\n{bcolors.OKGREEN}Saving {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        with open(newcombopath, mode='wt', encoding='utf-8') as myfile:
                            myfile.write('\n'.join(shuffledcombo))
                            myfile.write('\n')
                        endcleanshuffle = time.time()

                        timetakenedit = endedit - startedit
                        timetakencleanshuffle = endcleanshuffle - startcleanshuffle
                        newcombolinesno = (sum(1 for line in open(newcombopath)))
                        print(f'{bcolors.OKGREEN}\nSuccess!{bcolors.CYAN} appended special characters to the end of password within your {bcolors.OKGREEN}'+str(combolinesno)+f'{bcolors.CYAN} lines combo making it into a {bcolors.OKGREEN}'+str(newcombolinesno)+f'{bcolors.CYAN} lines combo.{bcolors.ENDC}\n')
                        print(f'{bcolors.OKGREEN}Editting{bcolors.CYAN} the combolist took {bcolors.OKGREEN}'+str(timetakenedit)+f' seconds.{bcolors.ENDC}')
                        print(f'{bcolors.OKGREEN}Cleaning & shuffling{bcolors.CYAN} the combolist took{bcolors.OKGREEN} '+str(timetakencleanshuffle)+f' seconds.{bcolors.ENDC}')
                        print(f'{bcolors.CYAN}\nYour new combolist can be found at: {bcolors.WARNING}'+str(newcombopath)+f'{bcolors.ENDC}\n')
                        time.sleep(2)
                        print(f"{bcolors.UNDERLINE}Navigation Options:{bcolors.ENDC}")
                        print(f"{bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.ENDC} Back to Local Combolist Edit Options")
                        print(f"{bcolors.CYAN}[{bcolors.ENDC}M{bcolors.CYAN}]{bcolors.ENDC} Back to Main Menu")
                        print(f"\n{bcolors.OKGREEN}What would you like to do today? {bcolors.ENDC}"); emailtouserpreference = (msvcrt.getch()).decode("utf-8")

                        if emailtouserpreference.upper() == "M":
                            mainui()
                        else:
                            pass

                        if emailtouserpreference.upper() == "B":
                            localcomboedits()
                        else:
                            pass

                def invertcap():
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(centered)
                    if authvalue == '1':
                        etulogged = (f"Successfully authenticated.\n{bcolors.ENDC}")
                        print(etulogged)
                        time.sleep(1)
                    else:
                        print(f"{bcolors.CYAN}The safeguards state that you are {bcolors.FAIL}not authenticated{bcolors.CYAN} to use Medusa's Local Editting features.{bcolors.ENDC}")
                        print(f"{bcolors.WARNING}If you believe this is a mistake please join our support Discord Server and create a ticket.{bcolors.ENDC}")
                        print(f"\n{bcolors.OKGREEN}Press {bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.OKGREEN} to go back return to the main menu.")
                        loop = True
                        while loop:
                            failcommand = (msvcrt.getch()).decode("utf-8")
                            if failcommand.upper() == "B":
                                mainui()
                                loop = False
                            else:
                                print('Please enter a correct input.')
                                time.sleep(1)
                                invertcap()

                    

                    title='Select a combolist file'
                    filetypes=['*.txt']
                    default='*.txt'
                    securityrun()
                    windowicon = requests.get("https://medusa.tools/icons/icon.ico") # remote medusa icon files
                    with open(tkicon,'wb') as output:
                        output.write(windowicon.content)
                    tk.iconbitmap(tkicon)
                    combofullpath = filedialog.askopenfilename(title = "Select a combolist file.",filetypes = (("Combolist File","*.txt"),("All files","*.*")))
                    try:
                        combopath = os.path.dirname(combofullpath)
                        comboname = os.path.basename(combopath)
                        dumpcombopath = ((os.path.splitext(combofullpath)[0])+'_dump.txt')
                        newcombopath = ((os.path.splitext(combofullpath)[0])+'_editted.txt')
                        combobytes = open(combofullpath, "rb").read(); comboencoding = chardet.detect(combobytes).get('encoding')
                        combolinesno = (sum(1 for line in open(combofullpath, encoding=comboencoding)))
                    except FileNotFoundError:
                        invertcap()
                    print(f'{bcolors.OKGREEN}'+str(combolinesno)+f' {bcolors.CYAN}lines in combolist{bcolors.ENDC}')
                    with open(combofullpath,"r") as q:
                        startedit = time.time()
                        print(f'\n{bcolors.OKGREEN}Reading {bcolors.CYAN}combolist...{bcolors.ENDC}')
                        texts = q.read()
                        comboline = texts.split("\n")
                        print(f'\n{bcolors.OKGREEN}Inverting {bcolors.CYAN}capitalization of passwords within this combolist...{bcolors.ENDC}')
                        combo = []
                        for i in range(combolinesno):
                            try:
                                combopair = comboline[i]
                                useremail, password = combopair.split(":")
                                newpass = password.swapcase()
                                newcombo = (useremail+':'+newpass)
                                combo.append(newcombo)
                                combo.append(combopair)
                            except ValueError:
                                pass

                        endedit = time.time()
                        startcleanshuffle = time.time()
                        print(f'\n{bcolors.OKGREEN}Cleaning {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        cleanedcombo = list(dict.fromkeys(combo))
                        print(f'\n{bcolors.OKGREEN}Shuffling {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        shuffledcombo = random.sample(cleanedcombo, len(cleanedcombo))
                        print(f'\n{bcolors.OKGREEN}Saving {bcolors.CYAN}editted combolist...{bcolors.ENDC}')
                        with open(newcombopath, mode='wt', encoding='utf-8') as myfile:
                            myfile.write('\n'.join(shuffledcombo))
                            myfile.write('\n')
                        endcleanshuffle = time.time()

                        timetakenedit = endedit - startedit
                        timetakencleanshuffle = endcleanshuffle - startcleanshuffle
                        newcombolinesno = (sum(1 for line in open(newcombopath)))
                        print(f'{bcolors.OKGREEN}\nSuccess!{bcolors.CYAN} inverted capitalization of passwords within your {bcolors.OKGREEN}'+str(combolinesno)+f'{bcolors.CYAN} lines combo making it into a {bcolors.OKGREEN}'+str(newcombolinesno)+f'{bcolors.CYAN} lines combo.{bcolors.ENDC}\n')
                        print(f'{bcolors.OKGREEN}Editting{bcolors.CYAN} the combolist took {bcolors.OKGREEN}'+str(timetakenedit)+f' seconds.{bcolors.ENDC}')
                        print(f'{bcolors.OKGREEN}Cleaning & shuffling{bcolors.CYAN} the combolist took{bcolors.OKGREEN} '+str(timetakencleanshuffle)+f' seconds.{bcolors.ENDC}')
                        print(f'{bcolors.CYAN}\nYour new combolist can be found at: {bcolors.WARNING}'+str(newcombopath)+f'{bcolors.ENDC}\n')
                        time.sleep(2)
                        print(f"{bcolors.UNDERLINE}Navigation Options:{bcolors.ENDC}")
                        print(f"{bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.ENDC} Back to Local Combolist Edit Options")
                        print(f"{bcolors.CYAN}[{bcolors.ENDC}M{bcolors.CYAN}]{bcolors.ENDC} Back to Main Menu")
                        print(f"\n{bcolors.OKGREEN}What would you like to do today? {bcolors.ENDC}"); emailtouserpreference = (msvcrt.getch()).decode("utf-8")

                        if emailtouserpreference.upper() == "M":
                            mainui()
                        else:
                            pass

                        if emailtouserpreference.upper() == "B":
                            localcomboedits()
                        else:
                            pass



                loop = True
                while loop:
                    localeditonepreference = (msvcrt.getch()).decode("utf-8")
                    if localeditonepreference.upper() == "B":
                        mainui()
                        loop=False
                    else:
                        pass
                    if localeditonepreference.upper() == "Q":
                        emailpassuhq()
                        loop=False
                    else:
                        pass
                    if localeditonepreference.upper() == "1":
                        emailtouser()
                        loop=False
                    else:
                        pass

                    if localeditonepreference.upper() == "2":
                        usertoemail()
                        loop=False
                    else:
                        pass

                    if localeditonepreference.upper() == "3":
                        addemailstoemail()
                        loop=False
                    else:
                        pass

                    if localeditonepreference.upper() == "4":
                        removespecialchars()
                        loop=False
                    else:
                        pass

                    if localeditonepreference.upper() == "5":
                        nonnumericuser()
                        loop=False
                    else:
                        pass

                    if localeditonepreference.upper() == "6":
                        nonnumericemail()
                        loop=False
                    else:
                        pass

                    if localeditonepreference.upper() == "7":
                        appendspecialpass()
                        loop=False
                    else:
                        pass

                    if localeditonepreference.upper() == "8":
                        invertcap()
                        loop=False
                    else:
                        print('Please enter a correct input.')
                        time.sleep(1)
                        loop=False
                        os.system('cls' if os.name == 'nt' else 'clear')
                        localcomboedits()


            localeditone()


    except ConnectionRefusedError:
       print(f'{bcolors.UNDERLINE}{bcolors.FAIL}Connection failed to Medusa Authentication servers failed.{bcolors.ENDC}')
       input('Press enter to exit...')
       sys.exit(0)

def remotecomboedits():
    try: 
        log = (f'\n{bcolors.CYAN}[{bcolors.ENDC}'+(strftime("%Y-%m-%d %H:%M:%S", gmtime()))+f'{bcolors.CYAN}] {bcolors.ENDC}')
        HOST = '127.0.0.1'  # The server's hostname or IP address - currently set to medusa's listener running on localhost
        PORT = 34280        # The port used by the server - currently set to medusa's listener running on localhost
        os.system('cls' if os.name == 'nt' else 'clear')
        print(centered)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print(f'{bcolors.UNDERLINE}{bcolors.OKGREEN}Connection Success.{bcolors.ENDC}')

            print(f"{bcolors.UNDERLINE}Mass Remote Combolist Editing:{bcolors.ENDC}")
            print(f"{bcolors.CYAN}[{bcolors.ENDC}Q{bcolors.CYAN}]{bcolors.ENDC} UHQ Editor - 3, 6, 7, 8 [EMAIL:PASS]\n")
            print(f"{bcolors.UNDERLINE}Combolist Tools:{bcolors.ENDC}")
            print(f"{bcolors.CYAN}[{bcolors.ENDC}1{bcolors.CYAN}]{bcolors.ENDC} Email to Username [EMAIL:PASS]")
            print(f"{bcolors.CYAN}[{bcolors.ENDC}2{bcolors.CYAN}]{bcolors.ENDC} Username to Email [USERNAME:PASS]")
            print(f"{bcolors.CYAN}[{bcolors.ENDC}3{bcolors.CYAN}]{bcolors.ENDC} Change Email to multiple Email Providers [EMAIL:PASS]")
            print(f"{bcolors.CYAN}[{bcolors.ENDC}4{bcolors.CYAN}]{bcolors.ENDC} Remove Special Characters from Passwords [*]")
            print(f"{bcolors.CYAN}[{bcolors.ENDC}5{bcolors.CYAN}]{bcolors.ENDC} Non-Numeric Username to Password Swap [USERNAME:PASS]")
            print(f"{bcolors.CYAN}[{bcolors.ENDC}6{bcolors.CYAN}]{bcolors.ENDC} Non-Numeric Email to Password Swap [EMAIL:PASS]")
            print(f"{bcolors.CYAN}[{bcolors.ENDC}7{bcolors.CYAN}]{bcolors.ENDC} Append Special Characters to Passwords [*]")
            print(f"{bcolors.CYAN}[{bcolors.ENDC}8{bcolors.CYAN}]{bcolors.ENDC} Invert Capitalization within Passwords [x/X]")
            print(f"\n{bcolors.OKGREEN}What would you like to do today? {bcolors.ENDC}")

            loop = True
            while loop:
                preference = (msvcrt.getch()).decode("utf-8")
                if preference.upper() == "Q":
                    s.send(('Q'.encode()))
                    loop=False

                elif preference.upper() == "1":
                    s.send(('1'.encode()))
                    loop=False

                elif preference.upper() == "2":
                    s.send(('2'.encode()))
                    loop=False

                elif preference.upper() == "3":
                    s.send(('3'.encode()))
                    loop=False

                elif preference.upper() == "4":
                    s.send(('4'.encode()))
                    loop=False

                elif preference.upper() == "5":
                    s.send(('5'.encode()))
                    loop=False

                elif preference.upper() == "6":
                    s.send(('6'.encode()))
                    loop=False

                elif preference.upper() == "7":
                    s.send(('7'.encode()))
                    loop=False

                elif preference.upper() == "8":
                    s.send(('8'.encode()))
                    loop=False
                else:
                    print('Please enter a correct input.')
                    time.sleep(1)
                    loop=False
                    os.system('cls' if os.name == 'nt' else 'clear')
                    remotecomboedits()
            os.system('cls' if os.name == 'nt' else 'clear')
            print(centered)
            print(log+'Initializing...')
            time.sleep(3)
            title='Select a combolist file'
            filetypes=['*.txt']
            default='*.txt'
            securityrun()
            windowicon = requests.get("https://medusa.tools/icons/icon.ico") # remote medusa icon files
            with open(tkicon,'wb') as output:
                    output.write(windowicon.content)
            tk.iconbitmap(tkicon)
            combofullpath = filedialog.askopenfilename(title = "Select a combolist file.",filetypes = (("Combolist File","*.txt"),("All files","*.*")))
            combobytes = open(combofullpath, "rb").read(); comboencoding = chardet.detect(combobytes).get('encoding')
            combolinesno = (sum(1 for line in open(combofullpath, encoding=comboencoding)))
            with open(combofullpath,"r") as q:
                print(log+'Reading combolist...')
                texts = q.read()
                comboline = texts.split("\n")
                combolist = []
                for i in range(combolinesno):
                    try:
                        combopair = comboline[i]
                        combolist.append(combopair)
                    except ValueError:
                        pass
                print(log+'Packaging combolist...')
                combostring = str(combolist)
                comboencoded = combostring.encode()
                print(log+'Sending combolist...')
                s.send(comboencoded)
                print(log+'Sent!')
                print(log+'Waiting for server response...')
                comboedittedencoded = s.recv(7516192768)
                print(log+'Received server response...')
                comboeditteddecoded = comboedittedencoded.decode()
                print(log+'Decoding editted combolist...')
                combostrlist = literal_eval(comboeditteddecoded)
                print(log+'Saving editted combolist...')
                orgfilename = str(HOST+'_'+datetime.today().strftime('%Y-%m-%d')+'.txt')
                with open(orgfilename, mode='wt', encoding='utf-8') as myfile:
                                myfile.write('\n'.join(combostrlist))
                                myfile.write('\n')
                print(log+'Saved list, exiting...')
                print(f"\n{bcolors.UNDERLINE}Navigation Options:{bcolors.ENDC}")
                print(f"{bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.ENDC} Back to Local Combolist Edit Options")
                print(f"{bcolors.CYAN}[{bcolors.ENDC}M{bcolors.CYAN}]{bcolors.ENDC} Back to Main Menu")
                print(f"{bcolors.OKGREEN}What would you like to do today? {bcolors.ENDC}"); emailtouserpreference = (msvcrt.getch()).decode("utf-8")

                if emailtouserpreference.upper() == "M":
                    mainui()
                else:
                    pass

                if emailtouserpreference.upper() == "B":
                    localcomboedits()
                else:
                    pass
    except ConnectionRefusedError:
        print(f'{bcolors.UNDERLINE}{bcolors.FAIL}Connection failed.{bcolors.ENDC}')
        print(f"\n{bcolors.UNDERLINE}Navigation Options:{bcolors.ENDC}")
        print(f"{bcolors.CYAN}[{bcolors.ENDC}B{bcolors.CYAN}]{bcolors.ENDC} Back to Local Combolist Edit Options")
        print(f"{bcolors.CYAN}[{bcolors.ENDC}M{bcolors.CYAN}]{bcolors.ENDC} Back to Main Menu")
        print(f"{bcolors.OKGREEN}What would you like to do today? {bcolors.ENDC}"); emailtouserpreference = (msvcrt.getch()).decode("utf-8")

        if emailtouserpreference.upper() == "M":
            mainui()
        else:
            pass

        if emailtouserpreference.upper() == "B":
            localcomboedits()
        else:
            pass


def enablemusic():
    if musicerror = True:
        print("Music Module Error!")
        time.sleep(1)
        mainui()
    else:
        mixer.unpause()
        print('Music Enabled.')
        time.sleep(1)
        mainui()

def disablemusic():
    if musicerror = True:
        print("Music Module Error!")
        time.sleep(1)
        mainui()
    else:
        mixer.pause()
        print("Music Disabled.")
        time.sleep(1)
        mainui()

def mainui():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(centered)
    welcome = (f"Welcome back!{bcolors.ENDC}")
    print(welcome)
    time.sleep(1)

    print(f"{bcolors.UNDERLINE}Combolist Tools:{bcolors.ENDC}")
    print(f"{bcolors.CYAN}[{bcolors.ENDC}1{bcolors.CYAN}]{bcolors.ENDC} Edit Combos Locally")
    print(f"{bcolors.CYAN}[{bcolors.ENDC}2{bcolors.CYAN}]{bcolors.ENDC} Edit Combos Remotely")
    print(f"{bcolors.UNDERLINE}Settings:{bcolors.ENDC}")
    print(f"{bcolors.CYAN}[{bcolors.ENDC}E{bcolors.CYAN}]{bcolors.ENDC} Enable Music")
    print(f"{bcolors.CYAN}[{bcolors.ENDC}D{bcolors.CYAN}]{bcolors.ENDC} Disable Music")

    print(f"\n{bcolors.OKGREEN}What would you like to do today? {bcolors.ENDC}"); preference = (msvcrt.getch()).decode("utf-8")

    if preference.upper() == "E":
        enablemusic()
    else:
        pass

    if preference.upper() == "D":
        disablemusic()
    else:
        pass

    if preference.upper() == "1":
        localcomboedits()
    else:
        pass

    if preference.upper() == "2":
        remotecomboedits()
    else:
        pass
    if preference.upper() == "X":
        sys.exit(0)
    else:
        print('Please enter a correct input.')
        time.sleep(1)
        mainui()

os.system('cls' if os.name == 'nt' else 'clear')

centered = (f"""{bcolors.OKBLUE}

 ███▄ ▄███▓▓█████ ▓█████▄  █    ██   ██████  ▄▄▄
▓██▒▀█▀ ██▒▓█   ▀ ▒██▀ ██▌ ██  ▓██▒▒██    ▒ ▒████▄
▓██    ▓██░▒███   ░██   █▌▓██  ▒██░░ ▓██▄   ▒██  ▀█▄
▒██    ▒██ ▒▓█  ▄ ░▓█▄   ▌▓▓█  ░██░  ▒   ██▒░██▄▄▄▄██
▒██▒   ░██▒░▒████▒░▒████▓ ▒▒█████▓ ▒██████▒▒ ▓█   ▓██▒
░ ▒░   ░  ░░░ ▒░ ░ ▒▒▓  ▒ ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░
░  ░      ░ ░ ░  ░ ░ ▒  ▒ ░░▒░ ░ ░ ░ ░▒  ░ ░  ▒   ▒▒ ░
░      ░      ░    ░ ░  ░  ░░░ ░ ░ ░  ░  ░    ░   ▒
       ░      ░  ░   ░       ░           ░        ░  ░
                   ░
           {bcolors.ENDC}""")

print(centered)
version = "1.0.0"

versionid = (((requests.get('https://medusa.tools/logins/version.txt')).content).decode('utf-8')) # remote medusa version verification
time.sleep(1)


if version == versionid:
    verified = ("Medusa is up-to-date, v"+version+"\n")
    for char in verified:
        time.sleep(0.010)
        sys.stdout.write(char)
        sys.stdout.flush()
    pass
else:
    print("\n This version of Medusa is outdated. Please update your client.")
    input("\n Press enter to close...")
    sys.exit(0)

time.sleep(1)

loop = True
while loop:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # connects to medusa authentication server
        HOST = '127.0.0.1'  # The server's hostname or IP address - currently set to medusa's listener running on localhost
        PORT = 56420        # The port used by the server - currently set to medusa's listener running on localhost
        s.connect((HOST, PORT)) # connects to medusa authentication server
        s.send((localhwid.encode())) # sends hwid to medusa authentication server
        authvalue = s.recv(128).decode() # receives authentication reponse from medusa authentication server
        if authvalue =='1': # verifies medusa authentication response as successful
            suc = (f"\n{bcolors.OKGREEN}Authentication successful...{bcolors.ENDC}")
            for char in suc:
                time.sleep(0.010)
                sys.stdout.write(char)
                sys.stdout.flush()
            load = ("\nLoading...")
            for char in load:
                time.sleep(0.010)
                sys.stdout.write(char)
                sys.stdout.flush()
            loop = False
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(centered)
            sys.stdout.write(f"\x1b]2;Medusa - Made by kyle-import | Log-in successful. \x07")
            welcome = (f"Welcome back!\n{bcolors.ENDC}")
            for char in welcome:
                time.sleep(0.010)
                sys.stdout.write(char)
                sys.stdout.flush()
            time.sleep(1)
            mainui()
        if authvalue == '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            loop = False
            print(error)
            print("\n")
            print("\n")
            print("\n")
            print("Your HWID is not authenticated or there was an error connecting to the hwid authentication server.")
            input("\nPress enter to close...")
            sys.exit(0)
