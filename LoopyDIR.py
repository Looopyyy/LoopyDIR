import requests
print("""
 ██▓     ▒█████   ▒█████   ██▓███ ▓██   ██▓   ▓█████▄  ██▓ ██▀███  
▓██▒    ▒██▒  ██▒▒██▒  ██▒▓██░  ██▒▒██  ██▒   ▒██▀ ██▌▓██▒▓██ ▒ ██▒
▒██░    ▒██░  ██▒▒██░  ██▒▓██░ ██▓▒ ▒██ ██░   ░██   █▌▒██▒▓██ ░▄█ ▒
▒██░    ▒██   ██░▒██   ██░▒██▄█▓▒ ▒ ░ ▐██▓░   ░▓█▄   ▌░██░▒██▀▀█▄  
░██████▒░ ████▓▒░░ ████▓▒░▒██▒ ░  ░ ░ ██▒▓░   ░▒████▓ ░██░░██▓ ▒██▒
░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒▓▒░ ░  ░  ██▒▒▒     ▒▒▓  ▒ ░▓  ░ ▒▓ ░▒▓░
░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░▒ ░     ▓██ ░▒░     ░ ▒  ▒  ▒ ░  ░▒ ░ ▒░
  ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░░       ▒ ▒ ░░      ░ ░  ░  ▒ ░  ░░   ░ 
    ░  ░    ░ ░      ░ ░           ░ ░           ░     ░     ░     
                                   ░ ░         ░                                                                                                     
""")
user_input = input("Url : ")
user_input = user_input + "/"
r = requests.get('{}'.format(user_input))
print('[{}] {} successfully witch {}{}'.format(0,user_input, r.status_code, " ✔️"))

diccionario = open('./LoopyDIR/directorysmall.txt', 'r')
diccionario_lines = diccionario.readlines()

count = 0
for direc in diccionario_lines:
        count += 1
        direc = ''.join(direc.splitlines())
        r_direct_format = user_input + direc
        s_direct_format = user_input + direc + "/"
        r = requests.get('{}'.format(r_direct_format))
        s = requests.get('{}'.format(s_direct_format))
        if r.status_code == 200:
            print('[{}] {} successfully witch {}{}'.format(count, r_direct_format, r.status_code, " ✔️"))
        if s.status_code == 200:
            print('[{}] {} successfully witch {}{}'.format(count, s_direct_format, r.status_code, " ✔️"))
   
