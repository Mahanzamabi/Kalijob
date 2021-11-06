from colorama import Fore
import os
import time
def getip():
    import socket

    name = socket.gethostname()
    ip = socket.gethostbyname(name)
    print(ip)
def addfolder():
    import subprocess as ter
    foldername = input('Enter name folder:')
    ter.getoutput(f'mkdir {foldername}')
def addfile():
    name = input('Enter name file:')
    with open(name,'a') as file:
        pass
def READFILE():
    from colorama import Fore
    path = input('Enter your path file:')
    RAED = open(path)
    for i in RAED:
        print(Fore.CYAN+i)
def newpassword():
    import random
    lx = 'QWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_'
    password = ''
    for c in range(9):
        password += random.choice(lx)

    print(str(password))
def portscan():
    import socket
    import subprocess
    URL = input('Enter Url:')
    ip =  socket.gethostbyname(URL)
    res = subprocess.getoutput(f'nmap {ip}')
    print(Fore.CYAN+res)
def sqlmap():
    url =input('Enter Url:')
    os.system(f'sqlmap -u {url}')
    
def htmlauto():
    namesite = input('Enter name site:')

    with open('auto.html','a') as html:
        html.write(f'''
                <html>

                <body>
                    <h2> Welcom to {namesite} site</h2>
                    <b>code:Kali job</b>
            </body>

            </html>
        
        
        ''')
        import os
        pathfile = os.getcwd()+'/auto.html'
        print(Fore.GREEN,f'ok file in path {pathfile}')
def opensite():
    link = input('Enter Url==>')
    import subprocess as ter
    ter.getoutput(f'open {link}')
def removefileandfolder():
        import subprocess
        path = input('Enter path==>')
        subprocess.getoutput(f'rm -r {path}')

run = True

os.system('clear')
while run:
        print(Fore.BLUE+'''
        +++++++++++++++
        ====================        
         _____KALI JOB‌______
        ====================         
        +++++++++++++++
        ''')
        print(Fore.GREEN,''' ================================================ =====================
        We wrote this program to do important things in Kali Linux
    And we wrote this program in the sweet language of Python ||||||
    =================================''')
        print(Fore.RED,''' 

        OS:KALI‌ LINUX

        04:GET‌ IP‌ PUBLIC |02:port scan
        87:NEW‌ FOLDER | 41:SQLMAP OPEN
        34:NEW‌ FILE [name.*] | 76:new file html and data auto
        23:READ‌ FILE |57:open the site
        12:new PASSWORD | 19:exit
        0:clear         | 10:remove file and folder







        ''');
        command = input('-->')
        if command =='0':
                os.system(
                'clear'
                )
        elif command =='04':
                os.system('clear')
                getip()
        elif command =='87':
                os.system('clear')
                addfolder()
                print(Fore.GREEN+'OK!')
                time.sleep(2)
                os.system('clear')
        elif command =='34':
                os.system('clear')
                addfile()
                print(Fore.BLUE+'OK!')
                time.sleep(2)
                os.system('clear')
        elif command == '23':
                os.system('clear')
                READFILE()
        elif command =='12':
                os.system('clear')
                newpassword()
        elif command =='02':
                os.system('clear')
                portscan()
        elif command =='41':
                sqlmap()
        elif command =='76':
                os.system('clear')
                htmlauto()
        elif command =='57':
                os.system('clear')
                opensite()
                print(Fore.GREEN,'opened!!')
        elif command =='19':
                os.system('clear')
                exit()
        elif command=='10':
                os.system('clear')
                removefileandfolder()
        else:
            print('not find number')
            print('select :')
        
#i love you PYTHON3	
	

