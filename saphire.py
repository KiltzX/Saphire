import os
import requests;
import time;
import json;


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
    """)

def main():
    banner()
    print("""

[+] Enter the URL of the target: """)
    url = input("saphire > ")
    print("""[+] Enter the wordlist full path: """)
    wordlist = input("saphire > ")
    print("""[+] Enter sleep time request(in seconds): """)
    sleep = input("saphire > ")

    print("""[+] Wanna use custom headers? (y/N) """)
    use_headers = input("saphire > ")
    headers_final = ''
    if use_headers == "y" or use_headers == "Y":
        headers_final = headers_choose()
    try:
        url = url.replace("https://", "")
        url = url.replace("http://", "")
        url = url.split("/")
        if url[(url.__len__() - 1)] != "":
            url = '/'.join(url)
            url = url + "/"
        else:
            url = '/'.join(url)
        url = "https://" + url
        isvalidFile = os.path.isfile(wordlist)
        if isvalidFile == True:
            print("[+] Wordlist found!")
            print("[+] Starting the scan...")
            with open(wordlist) as f:
                for line in f:
                    line = line.strip()
                    endpoint = url + line
                    time.sleep(int(sleep))
                    print("[+] Trying: " + endpoint)
                    r = requests.get(endpoint, headers=headers_final)
                    if r.status_code == 200:
                        print("Found: " + endpoint)
                    else:
                        pass
    except Exception as e:
        print("[-] Error: Check your wordlist path")
        print(e)
main()
