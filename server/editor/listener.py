import socket
import random, os
from time import gmtime, strftime
from colorama import init
from colorama import Fore, Back, Style
from ast import literal_eval
from psutil import virtual_memory
from datetime import datetime

init()
log = (Fore.MAGENTA+'['+Style.RESET_ALL+(strftime("%Y-%m-%d %H:%M:%S", gmtime()))+Fore.MAGENTA+'] '+Style.RESET_ALL)


mem = virtual_memory()
mem.total  # total physical memory available

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 56420        # Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while(True):
        def emailpassuhq(filename):
                combolinesno = (sum(1 for line in open(filename)))
                
                with open(filename,"r") as q:
                    print(log+'Reading combolist...')
                    texts = q.read()
                    comboline = texts.split("\n")
                    print(log+'Editting combolist...')
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

                    print(log+'Cleaning combolist...')
                    cleanedcombo = list(dict.fromkeys(combo))
                    print(log+'Shuffling combolist...')
                    shuffledcombo = random.sample(cleanedcombo, len(cleanedcombo))
                    print(log+'Sending combolist back to client...')
                    edittedcombo = str(shuffledcombo).encode()
                    clientConnected.sendall(edittedcombo)
                    print(log+'Sent!')

        def emailtouser(filename):
            combolinesno = (sum(1 for line in open(filename)))
            
            with open(filename,"r") as q:
                print(log+'Reading combolist...')
                texts = q.read()
                comboline = texts.split("\n")
                print(log+'Editting combolist...')
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


                print(log+'Cleaning combolist...')
                cleanedcombo = list(dict.fromkeys(combo))
                print(log+'Shuffling combolist...')
                shuffledcombo = random.sample(cleanedcombo, len(cleanedcombo))
                print(log+'Sending combolist back to client...')
                edittedcombo = str(shuffledcombo).encode()
                clientConnected.sendall(edittedcombo)
                print(log+'Sent!')

        def addemailstoemail(filename):
            combolinesno = (sum(1 for line in open(filename)))
            
            with open(filename,"r") as f:
                print(log+'Reading combolist...')
                texts = f.read()
                comboline = texts.split("\n")
                print(log+'Editting combolist...')
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

                print(log+'Cleaning combolist...')
                cleanedcombo = list(dict.fromkeys(combo))
                print(log+'Shuffling combolist...')
                shuffledcombo = random.sample(cleanedcombo, len(cleanedcombo))
                print(log+'Sending combolist back to client...')
                edittedcombo = str(shuffledcombo).encode()
                clientConnected.sendall(edittedcombo)
                print(log+'Sent!')

        def usertoemail(filename):
            combolinesno = (sum(1 for line in open(combofullpath)))
            
            with open(combofullpath,"r") as q:
                startedit = time.time()
                print(log+'Reading combolist...')
                texts = q.read()
                comboline = texts.split("\n")
                print(log+'Editting combolist..')
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

                print(log+'Cleaning combolist...')
                cleanedcombo = list(dict.fromkeys(combo))
                print(log+'Shuffling combolist...')
                shuffledcombo = random.sample(cleanedcombo, len(cleanedcombo))
                print(log+'Sending combolist back to client...')
                edittedcombo = str(shuffledcombo).encode()
                clientConnected.sendall(edittedcombo)
                print(log+'Sent!')


        def removespecialchars(filename):           
            combolinesno = (sum(1 for line in open(filename)))
            
            with open(filename,"r") as q:
                print(log+'Reading combolist...')
                texts = q.read()
                comboline = texts.split("\n")
                print(log+'Editting combolist...')
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


                print(log+'Cleaning combolist...')
                cleanedcombo = list(dict.fromkeys(combo))
                print(log+'Shuffling combolist...')
                shuffledcombo = random.sample(cleanedcombo, len(cleanedcombo))
                print(log+'Sending combolist back to client...')
                edittedcombo = str(shuffledcombo).encode()
                clientConnected.sendall(edittedcombo)
                print(log+'Sent!')


        def nonnumericuser(filename):  
            combolinesno = (sum(1 for line in open(combofullpath)))
            
            with open(filename,"r") as q:
                print(log+'Reading combolist...')
                texts = q.read()
                comboline = texts.split("\n")
                print(log+'Editting combolist...')
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


                print(log+'Cleaning combolist...')
                cleanedcombo = list(dict.fromkeys(combo))
                print(log+'Shuffling combolist...')
                shuffledcombo = random.sample(cleanedcombo, len(cleanedcombo))
                print(log+'Sending combolist back to client...')
                edittedcombo = str(shuffledcombo).encode()
                clientConnected.sendall(edittedcombo)
                print(log+'Sent!')
                
                


        def nonnumericemail(filename):
            combolinesno = (sum(1 for line in open(filename)))
            
            with open(combofullpath,"r") as q:
                print(log+'Reading combolist...')
                texts = q.read()
                comboline = texts.split("\n")
                print(log+'Editting combolist...')
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


                print(log+'Cleaning combolist...')
                cleanedcombo = list(dict.fromkeys(combo))
                print(log+'Shuffling combolist...')
                shuffledcombo = random.sample(cleanedcombo, len(cleanedcombo))
                print(log+'Sending combolist back to client...')
                edittedcombo = str(shuffledcombo).encode()
                clientConnected.sendall(edittedcombo)
                print(log+'Sent!')



        def appendspecialpass(filename):
            combolinesno = (sum(1 for line in open(filename)))

            with open(filename,"r") as q:
                print(log+'Reading combolist...')
                texts = q.read()
                comboline = texts.split("\n")
                print(log+"Editting combolist...")
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


                print(log+'Cleaning combolist...')
                cleanedcombo = list(dict.fromkeys(combo))
                print(log+'Shuffling combolist...')
                shuffledcombo = random.sample(cleanedcombo, len(cleanedcombo))
                print(log+'Sending combolist back to client...')
                edittedcombo = str(shuffledcombo).encode()
                clientConnected.sendall(edittedcombo)
                print(log+'Sent!')

        def invertcap(filename):
            combolinesno = (sum(1 for line in open(filename)))
            
            with open(filename,"r") as q:
                print(log+'Reading combolist...')
                texts = q.read()
                comboline = texts.split("\n")
                print(log+'Editting combolist...')
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

                print(log+'Cleaning combolist...')
                cleanedcombo = list(dict.fromkeys(combo))
                print(log+'Shuffling combolist...')
                shuffledcombo = random.sample(cleanedcombo, len(cleanedcombo))
                print(log+'Sending combolist back to client...')
                edittedcombo = str(shuffledcombo).encode()
                clientConnected.sendall(edittedcombo)
                print(log+'Sent!')

                clientConnected.sendall(edittedcombo)
        (clientConnected, clientAddress) = s.accept()
        print(log+"Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]))
        print(log+'Awaiting edit mode request from client...')
        editmode = str((clientConnected.recv(20)).decode())
        print(log+'Received edit mode request from client: '+editmode)
        dataFromClient = clientConnected.recv(9060798464)
        comboliststr = (dataFromClient.decode())
        print(log+'Converting received combolist into list...')
        combostrlist = literal_eval(comboliststr)
        orgfilename = str(clientAddress[0]+'_'+datetime.today().strftime('%Y-%m-%d')+'.txt')
        with open(orgfilename, mode='wt', encoding='utf-8') as myfile:
                        myfile.write('\n'.join(combostrlist))
                        myfile.write('\n')
        if editmode == 'Q':
            emailpassuhq(orgfilename)
        else:
            pass
        if editmode == '1':
            emailtouser(orgfilename)
        else:
            pass
        if editmode == '2':
            usertoemail(orgfilename)
        else:
            pass
        if editmode == '3':
            addemailstoemail(orgfilename)
        else:
            pass
        if editmode == '4':
            removespecialchars(orgfilename)
        else:
            pass
        if editmode == '5':
            nonnumericuser(orgfilename)
        else:
            pass
        if editmode == '6':
            nonnumericemail(orgfilename)
        else:
            pass
        if editmode == '7':
            appendspecialpass(orgfilename)
        else:
            pass
        if editmode == '8':
            invertcap(orgfilename)
        else:
            pass
        os.remove(orgfilename)
        print(log+'Deleted combolist.\n')