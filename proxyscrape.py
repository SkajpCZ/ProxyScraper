# Made by: Skajp   |   Discord: DeadSkajp#5906
# Github: https://github.com/SkajpCZ/ProxyScraper
# Version: 1
import os
def scrapes():
    import json, requests
    proxy_resources = [
    'https://www.proxy-list.download/api/v1/get?type=socks4',
    'https://www.proxyscan.io/download?type=socks4',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt',
    'https://api.openproxylist.xyz/socks4.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt',
    'https://www.freeproxychecker.com/result/socks4_proxies.txt',
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt',
    'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true',
    'https://www.proxy-list.download/api/v1/get?type=socks5',
    'https://www.proxyscan.io/download?type=socks5',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
    'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt',
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt',
    'https://api.openproxylist.xyz/socks5.txt',
    'https://www.freeproxychecker.com/result/socks5_proxies.txt',
    'https://api.proxyscrape.com/?request=displayproxies&proxytype=http',
    'https://www.proxy-list.download/api/v1/get?type=http',
    'https://www.proxyscan.io/download?type=http',
    'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt',
    'https://api.openproxylist.xyz/http.txt',
    'https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt',
    'http://alexa.lr2b.com/proxylist.txt',
    'http://rootjazz.com/proxies/proxies.txt',
    'https://www.freeproxychecker.com/result/http_proxies.txt',
    'http://proxysearcher.sourceforge.net/Proxy%20List.php?type=http',
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt',
    'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
    'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
    'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt',
    'https://proxy-spider.com/api/proxies.example.txt',
    'https://multiproxy.org/txt_all/proxy.txt',
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
    'https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/http.txt',
    'https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/https.txt',
    'https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all'
    ]

    def steal_proxies(site):
        try:
            data = requests.get(site)
            text_for_parse = data.text
            res = text_for_parse.split()
            with open('./proxies.txt', 'a') as proxy_file:
                proxy_file.writelines('\n'.join(res))
            return True
        except Exception as Error:
            return Error
    def count_proxies():
        try:
            proxies = sum(1 for line in open('./proxies.txt', 'r'))
            return proxies
        except Exception as Error:
            return Error
    countSC = 1
    try:
        print('\033[1;93m' + "\n Scraping Proxies" + '\033[1;90m' + " > " + '\033[1;37m' + f"{len(proxy_resources)} sites")
        for site in proxy_resources:
            if countSC == len(proxy_resources):
                print('\033[1;90m' + "\r Scraping is done             ", end="\r")
            else:
                print('\033[1;90m' + "\r Scraping >" + f" \033[1;90m{countSC} / {len(proxy_resources)}", end="\r")
            res = steal_proxies(site)
            countSC += 1
    except:
        print('\033[1;31m' + "\n ERROR")
    pr = count_proxies()
    print('\033[1;93m' + "\n\n Scraped" + '\033[1;90m' + " > " + '\033[1;37m' + f"{pr}")
    print('\033[1;93m' + " Saved in" + '\033[1;90m' + " > " + '\033[1;37m' + f"./proxies.txt")
    input('\n\033[1;37m Press \033[1;93m[ Enter ]\033[1;37m to exit')


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
clear()

print(f"""\033[1;36m
              _____                                
        ____ / ___/______________ _____  ___  _____
       / __ \\\__ \/ ___/ ___/ __ `/ __ \/ _ \/ ___/
      / /_/ /__/ / /__/ /  / /_/ / /_/ /  __/ /    
     / .___/____/\___/_/   \__,_/ .___/\___/_/     
    /_/                        /_/                  \033[1;37mby \033[1;90mSkajp
                                                    \033[1;37mVersion: \033[1;90m1
""")

scrapes()