import os
import requests;
import time;
import json;
import sys;

def headers_choose(old_headers={'origin_request': 'Saphire 1.0'}):
    print("""[+] Enter the header name: """)
    header_name = input("saphire > ")
    print("""[+] Enter the header value: """)
    header_value = input("saphire > ")
    dictA = json.dumps(old_headers)
    dictB = json.dumps({header_name: header_value})
    dictA = json.loads(dictA)
    dictB = json.loads(dictB)
    dictA.update(dictB)
    headers = dictA
    print("""[+] Wanna add more headers ? (y/N): """)
    add_more = input("saphire > ")
    if add_more == "y" or add_more == "Y":
        headers_choose(headers)
    return headers


def banner():
    os.system('clear')
    print(""" 
  _________             .__    .__                
 /   _____/____  ______ |  |__ |__|______   ____  
  \_____  \\__  \ \____ \|  |  \|  \_  __ \_/ __ \ 
  /        \/ __ \|  |_> >   Y  \  ||  | \/\  ___/ 
 /_______  (____  /   __/|___|  /__||__|    \___  >
        \/     \/|__|        \/                \/ 

        -- API - ENDPOINT FINDER --
        Version: 1.0
        Created by: @Kiltzx
        Contribuitor: @jeanrafaellourenco
    """)

def main(url='', wordlist='',method='' , sleep='', custom_headers='', show_banner=True):
    print(""" 
    """)
    if show_banner:
        banner()
    if url == '':
        print("""[+] Enter the target URL: """)
        url = input("saphire > ")
    if wordlist == '':
        print("""[+] Enter the wordlist full path: """)
        wordlist = input("saphire > ")
    if method == '':
        print("""[+] Enter the HTTP method(GET,POST): """)
        method = input("saphire > ")
    if sleep == '':
        print("""[+] Enter the sleep time between requests: """)
        sleep = input("saphire > ")
    if custom_headers == '':
        print("""[+] Use custom headers ? (y/N): """)
        headers_choose = input("saphire > ")
        if headers_choose == "y" or headers_choose == "Y":
            custom_headers = headers_choose()

    try:
        url = url.replace("https://", "")
        url = url.replace("http://", "")
        url = url.split("/")
        print("""[+] Use SSL ? (S/n): """)
        ssl = input("saphire > ")
        if url[(url.__len__() - 1)] != "":
            url = '/'.join(url)
            url = url + "/"
        else:
            url = '/'.join(url)
        if(ssl == "S" or ssl == "s"):
            url = "https://" + url
        else:
            url = "http://" + url
        isvalidFile = os.path.isfile(wordlist)
        if isvalidFile == True:
            print("[+] Wordlist found!")
            print("[+] URL: " + url)
            print("[+] Method: " + method)
            print("[+] Wordlist: " + wordlist)
            print("[+] Sleep time: " + sleep)
            print("[+] Custom headers: " + str(custom_headers))
            print("[+] Starting the scan...")
            with open(wordlist) as f:
                for line in f:
                    line = line.strip()
                    endpoint = url + line
                    time.sleep(int(sleep))
                    print("[+] Trying: " + endpoint)
                    if method == "GET":

                        r = requests.get(endpoint, headers=custom_headers)
                        if r.status_code == 200:
                            print("Found: " + endpoint)
                        else:
                            pass
                    elif method == "POST":
                        r = requests.post(endpoint,{} , headers=custom_headers)
                        if r.status_code == 200:
                            print("Found: " + endpoint)
                        else:
                            pass
    except Exception as e:
        print("[-] Error: Check your wordlist path")
        print(e)

def checkParams():
    url= ''
    method= ''
    wordlist = ''
    sleep = ''
    custom_headers = ''
    if len(sys.argv) <= 1:
        main()
        return
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "-h" or sys.argv[i] == "--help":
            banner()
            print("""Usage: python3 saphire.py -u <url> -w <wordlist> -s <sleep> -c <custom headers>""")
            print("""""")
            print("""Example: python3 saphire.py -u https://example.com -m GET -w /home/user/wordlist.txt -s 1 -c {x-access-token:XXXXXXXXX}""")
            print("""""")
            print("""-h, --help: Show this help""")
            print("""-u, --url: Target URL""")
            print("""-m, --method: HTTP method""")
            print("""-w, --wordlist: Wordlist full path""")
            print("""-s, --sleep: Sleep time between requests""")
            print("""-c, --custom: Use custom headers""")
            sys.exit()
        else:
            if sys.argv[i] == "-u" or sys.argv[i] == "--url":
                url = sys.argv[i+1]
            if sys.argv[i] == "-m" or sys.argv[i] == "--method":
                method = sys.argv[i+1]
            if sys.argv[i] == "-w" or sys.argv[i] == "--wordlist":
                wordlist = sys.argv[i+1]
            if sys.argv[i] == "-s" or sys.argv[i] == "--sleep":
                sleep = sys.argv[i+1]
            if sys.argv[i] == "-c" or sys.argv[i] == "--custom":
                custom_headers = sys.argv[i+1]
    main(url, wordlist,method, sleep, custom_headers, True)


checkParams()
