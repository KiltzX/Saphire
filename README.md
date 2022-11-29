## Saphire - API endpoint finder

```
  _________             .__    .__                
 /   _____/____  ______ |  |__ |__|______   ____  
  \_____  \__  \ \____ \|  |  \|  \_  __ \_/ __ \ 
  /        \/ __ \|  |_> >   Y  \  ||  | \/\  ___/ 
 /_______  (____  /   __/|___|  /__||__|    \___  >
        \/     \/|__|        \/                \/ 

        -- API - ENDPOINT FINDER --
        Version: 1.0
        Created by: @Kiltzx
    
Usage: python3 saphire.py -u <url> -w <wordlist> -s <sleep> -c <custom headers>

Example: python3 saphire.py -u https://example.com -w /home/user/wordlist.txt -s 1 -c {x-access-token:XXXXXXXXX}

-h, --help: Show this help
-u, --url: Target URL
-w, --wordlist: Wordlist full path
-s, --sleep: Sleep time between requests
-c, --custom: Use custom headers
```

Saphire is a tool that helps you find API endpoints in a website. It is a simple tool that uses a wordlist to find endpoints in a website. 
