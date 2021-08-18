#!/usr/bin/python3
import os
import time
import sys


os.system("clear")

PKGs =["Termux Styles","Basic Tools", "Advanced Tools",]
TermuxStylesList=["Extra Keys","Set login","Text Theme"]
BasicTools=["python","python2","python-dev","python3","php","java","git","perl","bash","nano","curl","openssl","openssh","wget","clang","nmap","w3m","hydra","ruby","macchanger","host","dnsutils","coreutils","figlet and toilet"]
AdvancedTools=["Metasploit","Kali (Nethunter)","Youtube Downloader"]
print ('''\n\033[95m
+-----------------------------------------+
| This Tool Install All Packages          |
+-----------------------------------------+
| Coded By Balaji K Hacker| version : 2.0 |
+-----------------------------------------+''')

def TermuxStyles():
    j=1
    loopVal=1
    for i in TermuxStylesList:
        slowprint("[{0}] {1}".format(j,i))
        j=j+1
    print ("\n")
    while loopVal != '0' or loopVal !='00':
        ch = input("\n\033[93m Enter You Want to Install PKG  index (Exit: 'E' or Back: 'B'): ")
        loopVal=ch
        if ch=='01' or ch=='1':
            print("\033[95mYou entered index= {0}".format(ch))
            print('After modified extra keys it will be restarted.')
            os.system('''mkdir $HOME/.termux/ ;echo "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP','DEL'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN','BKSP']]" >> $HOME/.termux/termux.properties && termux-reload-settings && sleep 1 &&logout''')
            
        elif ch=='02' or ch=='2':
            print("\033[95mYou entered index= {0}".format(ch))
            os.system("git clone https://github.com/balajibe1994/Termuxlogin.git")
            os.system("cd Termuxlogin")
            os.system("chmod +x *")
            os.system("bash install.sh")
            os.system("cp log.py /data/data/com.termux/files/usr/etc/")
            chB=input("\033[95mDo you want to replace bash.basrc file? (y/n):")
            if 'y' ==chB or 'Y' ==chB:
                os.system("cp /data/data/com.termux/files/usr/etc/bash.bashrc /data/data/com.termux/files/usr/etc/bash.bashrc.save")
                os.system("cp bash.bashrc /data/data/com.termux/files/usr/etc/")
                print("\033[95mLogin Passwd: bala ")
                print("Restart the Termux app!!")            
            
        elif ch=='03' or ch=='3':
            print("\033[95mYou entered index= {0}".format(ch))
            os.system("git clone https://github.com/balajibe1994/TermuxStyle.git")
            chB=input("\033[95mDo you want to replace bash.basrc file? (y/n):")
            if 'y' ==chB or 'Y' ==chB:
                os.system("cp /data/data/com.termux/files/usr/etc/bash.bashrc /data/data/com.termux/files/usr/etc/bash.bashrc.save")
                os.system("cp TermuxStyle/bash.bashrc /data/data/com.termux/files/usr/etc/")
                print("Restart the Termux app!!")
            
        elif ch=='E' or ch=='e':
            sys.exit()
        elif ch=='B' or ch=='b':
            main()
        else:
            print ("\033[93m\n Try Again.. Thanks.")

            
def AdvancedToolsMethod():
    j=1
    loopVal=1
    for i in AdvancedTools:
        slowprint("[{0}] {1}".format(j,i))
        j=j+1
    print ("\n")
    while loopVal != '0' or loopVal !='00':
        ch = input("\n\033[93m Enter You Want to Install PKG  index (Exit: 'E' or Back: 'B'): ")
        loopVal=ch
        if ch=='01' or ch=='1':
            print("\033[95mYou entered index= {0}".format(ch))
            os.system ("pkg install python python2 curl wget -y")
            os.system ("pkg install perl ruby php -y")
            os.system ("pkg install unstable-repo")
            os.system ("pkg install metasploit -y")
            print('Type "msfconsole" and enjoy.!!')
            
        elif  ch=='02' or ch=='2':
            print("\033[95mYou entered index= {0}".format(ch))
            os.system ("termux-setup-storage")
            os.system ("pkg install wget -y")
            os.system ("wget -O install-nethunter-termux https://offs.ec/2MceZWr")
            os.system ("chmod +x install-nethunter-termux")
            print("It will take some time to download kali image (depends on internet speed), please wait..");
            os.system ("./install-nethunter-termux")
                    
        elif  ch=='03' or ch=='3':
            print("\033[95mYou entered index= {0}".format(ch))
            os.system ("termux-setup-storage")
            os.system ("pkg install python python2 curl wget -y")
            os.system ("pkg install perl ruby php -y")
            os.system ("wget https://pastebin.com/raw/iNa0NixT -O YoutubeDownloader.sh")
            os.system ("dos2unix YoutubeDownloader.sh")       
            os.system ("chmod u+x YoutubeDownloader.sh")
            print("It will take some time install downloader, please wait..");
            os.system ("./YoutubeDownloader.sh")
            
        elif  ch=='E' or ch=='e':
            sys.exit()
        elif  ch=='B' or ch=='b':
            main()
        else:
            print ("\033[93m\n Try Again.. Thanks.")

def BasicToolsMethod():
    j=1
    loopVal=1
    for i in BasicTools:
        slowprint("[{0}] {1}".format(j,i))
        j=j+1

    print ("\n")
    choice = input("\n\033[93mDo You Want to Install All PKGs (Y/N): ")
    if choice == 'n' or choice == 'N' :        
        while loopVal != '0' or loopVal !='00' or loopVal !='b0':        
            ch = input("\n\033[93m Enter You Want to Install PKG index (Exit: 'E' and Back : 'B'): ")
            loopVal=ch
            if ch=='01' or ch=='1':
                print("\033[95mYou entered index= {0}".format(ch))
                os.system ("apt install python -y")
                
            elif  ch=='02' or ch=='2':
                print("You entered index= {0}".format(ch))
                os.system ("apt install python2 -y")
                
            elif  ch=='03' or ch=='3':                
                print("You entered index= {0}".format(ch))
                os.system ("apt install python-dev -y")
                
            elif  ch=='04' or ch=='4':
                print("\033[95mYou entered index= {0}".format(ch))
                os.system ("apt install python3 -y")
                
            elif  ch=='05' or ch=='5':
                print("\033[95mYou entered index= {0}".format(ch))
                os.system ("apt install php -y")
                
            elif  ch=='06' or ch=='6':
                print("\033[95mYou entered index= {0}".format(ch))
                os.system ("apt install java -y")
                
            elif  ch=='07' or ch=='7':
                print("\033[95mYou entered index= {0}".format(ch))
                os.system ("apt install git -y")
                
            elif  ch=='08' or ch=='8':
                print("You entered index= {0}".format(ch))
                os.system ("apt install perl -y")
                
            elif  ch=='09' or ch=='9':
                print("You entered index= {0}".format(ch))
                os.system ("apt install bash")
                
            elif  ch=='10' or ch=='10':
                print("You entered index= {0}".format(ch))
                os.system ("apt install nano -y")
                
            elif  ch=='11' or ch=='11':                
                print("You entered index= {0}".format(ch))
                os.system ("apt install curl -y")
                
            elif  ch=='12' or ch=='12':
                print("\033[95mYou entered index= {0}".format(ch))
                os.system ("apt install openssl -y")
            elif  ch=='13' or ch=='13':
                print("\033[95mYou entered index= {0}".format(ch))
                os.system ("apt install openssh -y")
                
            elif  ch=='14' or ch=='14':
                print("\033[95mYou entered index= {0}".format(ch))
                os.system ("apt install wget -y")
                
            elif  ch=='15' or ch=='15':
                print("\033[95mYou entered index= {0}".format(ch))
                os.system ("apt install clang -y")
                
            elif  ch=='16' or ch=='16':
                print("You entered index= {0}".format(ch))
                os.system ("apt install nmap -y")
                
            elif  ch=='17' or ch=='17':
                print("You entered index= {0}".format(ch))
                os.system ("apt install w3m -y")
                
            elif  ch=='18' or ch=='18':
                print("\033[95mYou entered index= {0}".format(ch))
                os.system ("apt install hydra -y")
                
            elif  ch=='19' or ch=='19':
                print("\033[95mYou entered index= {0}".format(ch))
                os.system ("apt install ruby -y")
                
            elif  ch=='20' or ch=='20':
                print("\033[95mYou entered index= {0}".format(ch))
                os.system ("apt install macchanger -y")
                
            elif ch=='21' or ch=='21':
                print("\033[95mYou entered index= {0}".format(ch))
                os.system ("apt install host -y")
                
            elif  ch=='22' or ch=='22':
                print("\033[95mYou entered index= {0}".format(ch))
                os.system ("apt install dnsutils -y")
                
            elif  ch=='23' or ch=='23':
                print("\033[95mYou entered index= {0}".format(ch))
                os.system ("apt install coreutils -y")
            elif  ch=='24' or ch=='24':
                print("\033[95mYou entered index= {0}".format(ch))
                os.system ("apt install figlet toilet -y")
            #elif  ch=='25' or ch=='25':
               # print("You entered index= {0}".format(ch))
            #elif  ch=='26' or ch=='26':
            #elif  ch=='27' or ch=='27':
            #elif  ch=='28' or ch=='28':
            #elif  ch=='29' or ch=='29':
            #elif  ch=='30' or ch=='30':
            #elif  ch=='31' or ch=='31':
            #elif  ch=='32' or ch=='32':
            #elif  ch=='33' or ch=='33':
            #elif  ch=='34' or ch=='34':
            elif  ch=='E' or ch=='e':
                sys.exit()
            elif  ch=='B' or ch=='b':
                main()
            else:
                print ("\n Try Again.. Thanks.")
                
        print ("Allow the Button For Access the Storage in Termux")
        os.system ("termux-setup-storage")
    
    if choice == 'y' or choice == 'Y':
        os.system ("apt update")
        os.system ("atp upgrade -y")
        os.system ("apt install python -y")
        os.system ("apt install python2 -y")
        os.system ("apt install php -y")
        os.system ("apt install python-dev -y")
        os.system ("apt install python3 -y")
        os.system ("apt install java -y")
        os.system ("apt install git -y")
        os.system ("apt install perl -y")
        os.system ("apt install bash")
        os.system ("apt install nano -y")
        os.system ("apt install curl -y")
        os.system ("apt install openssl -y")
        os.system ("apt install openssh -y")
        os.system ("apt install wget -y")
        os.system ("apt install clang -y")
        os.system ("apt install nmap -y")
        os.system ("apt install w3m -y")
        os.system ("apt install hydra -y")
        os.system ("apt install ruby -y")
        os.system ("apt install macchanger -y")
        os.system ("apt install host -y")
        os.system ("apt install dnsutils -y")
        os.system ("apt install coreutils -y")
        print ("Allow the Button For Access the Storage in Termux")
        os.system ("termux-setup-storage")

    cho1=input("Type Exit(00) and Back(b0) :")
    if ch01 =="00":
        sys.exit()
    if ch01=="b0":
        main()
       
    
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)


def main():
    j=1
    loopVal=1
    for i in PKGs:
        print("[{0}] {1}".format(j,i))
        j=j+1
      
    cho=input("\n\033[93m Enter You Want to Install PKG  index (Exit: 'E'): ")
    if cho =='1':
        TermuxStyles()
        
    elif cho=='2':
        BasicToolsMethod()
        
    elif cho=='3':
        AdvancedToolsMethod()
        
    elif cho =='E' or cho =='e':
        sys.exit()
    else:
        print ("\n Try Again.. Thanks.")


if __name__ == "__main__":
    main()

print("\033[95m+-------------------------------------------------+")
slowprint('''\033[95m
|             Welcome To Hacker                   |
| Watch Ours Tutorials For Learn Ethical Hacking  |''')
print("\033[95m+-------------------------------------------------+")

input("\n\nPress the enter key to exit : ")
