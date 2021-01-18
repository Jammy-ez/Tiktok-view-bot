from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from os import system, name
from colorama import Fore, Back, Style
def clear():
        _ = system('cls')
print(Fore.RED + '''

████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗    ██╗   ██╗██╗███████╗██╗    ██╗    ██████╗  ██████╗ ████████╗
╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝    ██║   ██║██║██╔════╝██║    ██║    ██╔══██╗██╔═══██╗╚══██╔══╝
   ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝     ██║   ██║██║█████╗  ██║ █╗ ██║    ██████╔╝██║   ██║   ██║   
   ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗     ╚██╗ ██╔╝██║██╔══╝  ██║███╗██║    ██╔══██╗██║   ██║   ██║   
   ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗     ╚████╔╝ ██║███████╗╚███╔███╔╝    ██████╔╝╚██████╔╝   ██║   
   ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝      ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝     ╚═════╝  ╚═════╝    ╚═╝   
''')
print(Fore.GREEN + '''       
   Type help for help
   [1]View bot with proxies
   [2]View bot without proxies (proxyless)
   [!]More options coming soon
''')

optionfirst = input("Eneter option: ")
if optionfirst == '1':
    URL = input("Eneter tiktok link: ")
    print("Views automatically set to infinite!")
    time.sleep(1)
    WATCHTIME = input("Enter watch time: ")
    WATCHTIME = float(WATCHTIME)
    print("Proxie should look like (11.456.448.110:8080) and should be a http/https proxie")
    proxie1 = input("Eneter proxie: ")
    time.sleep(1)
    print("Settup up varibles")
    time.sleep(1)
    print("headless mode is disabled")
    #browser 1
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % proxie1)
    chrome_options.add_argument("--mute-audio")
    browser1 = webdriver.Chrome(chrome_options=chrome_options)
    #browser 2
    browser2 = webdriver.Chrome(chrome_options=chrome_options)
    print("Drivers getting link...")
    browser1.get(URL)
    browser2.get(URL)
    time.sleep(10)
    print("Drivers successfully opened link..")
    print("Refreshing drivers...")
    browser1.refresh()
    browser2.refresh()
    time.sleep(1.5)
    print("Setting up loop...")
    time.sleep(1)
    clear()
    print(Fore.RED + '''
 Made by jam
████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗    ██╗   ██╗██╗███████╗██╗    ██╗    ██████╗  ██████╗ ████████╗
╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝    ██║   ██║██║██╔════╝██║    ██║    ██╔══██╗██╔═══██╗╚══██╔══╝
   ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝     ██║   ██║██║█████╗  ██║ █╗ ██║    ██████╔╝██║   ██║   ██║   
   ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗     ╚██╗ ██╔╝██║██╔══╝  ██║███╗██║    ██╔══██╗██║   ██║   ██║   
   ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗     ╚████╔╝ ██║███████╗╚███╔███╔╝    ██████╔╝╚██████╔╝   ██║   
   ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝      ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝     ╚═════╝  ╚═════╝    ╚═╝   
    ''')
    while True:
     time.sleep(WATCHTIME)
     browser1.refresh()
     browser2.refresh()
     print("All browsers finished")
if optionfirst == '2':
    URL = input("Eneter tiktok link: ")
    print("Views automatically set to infinite!")
    time.sleep(1)
    WATCHTIME = input("Enter watch time: ")
    WATCHTIME = float(WATCHTIME)
    print("Proxie should look like (11.456.448.110:8080) and should be a http/https proxie")
    time.sleep(1)
    print("Settup up varibles")
    time.sleep(1)
    print("headless mode is disabled")
    #browser 1
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    browser1 = webdriver.Chrome(chrome_options=chrome_options)
    browser2 = webdriver.Chrome(chrome_options=chrome_options)
    print("Drivers getting link...")
    browser1.get(URL)
    browser2.get(URL)
    time.sleep(10)
    print("Drivers successfully opened link..")
    print("Refreshing drivers...")
    browser1.refresh()
    browser2.refresh()
    time.sleep(1.5)
    print("Setting up loop...")
    time.sleep(1)
    clear()
    print(Fore.RED + '''
 Made by jam
████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗    ██╗   ██╗██╗███████╗██╗    ██╗    ██████╗  ██████╗ ████████╗
╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝    ██║   ██║██║██╔════╝██║    ██║    ██╔══██╗██╔═══██╗╚══██╔══╝
   ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝     ██║   ██║██║█████╗  ██║ █╗ ██║    ██████╔╝██║   ██║   ██║   
   ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗     ╚██╗ ██╔╝██║██╔══╝  ██║███╗██║    ██╔══██╗██║   ██║   ██║   
   ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗     ╚████╔╝ ██║███████╗╚███╔███╔╝    ██████╔╝╚██████╔╝   ██║   
   ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝      ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝     ╚═════╝  ╚═════╝    ╚═╝   
    ''')
    while True:
     time.sleep(WATCHTIME)
     browser1.refresh()
     browser2.refresh()
     print("All browsers finished")
