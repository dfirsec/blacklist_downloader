# IP Blacklist Check

![Generic badge](https://img.shields.io/badge/python-3.7-blue.svg) [![Twitter](https://img.shields.io/badge/Twitter-@pulsecode-blue.svg)](https://twitter.com/pulsecode)

Python script to download blacklists from various sources and check IP addresses against those blacklists.  Utilizes the FreeGeopIP Live service for IP geolocation. (ref: <https://freegeoip.live/)>

## Installation

```text
git clone https://github.com/dfirsec/blacklist_check.git
cd blacklist_check
pip install -r requirements.txt
```

## Usage

```console
        ____  __           __   ___      __     ________              __
       / __ )/ /___ ______/ /__/ (_)____/ /_   / ____/ /_  ___  _____/ /__
      / __  / / __ `/ ___/ //_/ / / ___/ __/  / /   / __ \/ _ \/ ___/ //_/
     / /_/ / / /_/ / /__/ ,< / / (__  ) /_   / /___/ / / /  __/ /__/ ,<
    /_____/_/\__,_/\___/_/|_/_/_/____/\__/   \____/_/ /_/\___/\___/_/|_|
     v2.0

usage: blacklist_check.py [-h] [-u] [-s] [-q query [query ...]] [-w] [-f file] [-i insert insert] [-r remove]

IP Blacklist Check

optional arguments:
  -h, --help            show this help message and exit
  -t [threads]          threads for rbl check (default 25, max 50)
  -w                    perform ip whois lookup
  -u                    update blacklist feeds
  -fu                   force update of all feeds
  -s                    show blacklist feeds
  -vt                   check virustotal for ip info
  -q query [query ...]  query a single or multiple ip addrs
  -f file               query a list of ip addresses from file
  -i                    insert a new blacklist feed
  -r                    remove an existing blacklist feed
  ```

#### Example Run
  ![alt text](images/blacklist_check.gif)

### Update Blacklisted IPs from feeds

  ```text
  python blacklist_check.py -u

 [ Updating ]
  ➜  Alien Vault Reputation
  ➜  Bambenek Consulting
  ➜  Bitcoin Nodes
  ➜  Blocklist DE
  ➜  Bot Scout IPs
  ➜  Brute Force Blocker
  ➜  CI Army Badguys
  ➜  Coin Blacklist Hosts
  ➜  CyberCrime
  ➜  Danger Rulez
  ➜  Darklist DE
  ➜  ET Compromised
  ➜  ET Tor Rules
  ➜  IP Spamlist
  ➜  MalC0de Blacklist
  ➜  Malware Army
  ➜  Malware Domains
  ➜  Mirai Security
  ➜  MyIP Blacklist
  ➜  SSL Abuse IP List
  ➜  SpamHaus Drop
  ➜  Stop Forum Spam
  ➜  Talos Intel
  ➜  Threat Crowd
  ➜  Threatweb Botnet IPs
  ➜  Threatweb Watchlist
  ➜  URL Haus
  ➜  WindowsSpyBlocker
```

### Show count of Blacklisted IPs

```text
python blacklist_check.py -s

LIST                      COUNT
-----------------------------------
Alien Vault Reputation   : 36112
Bambenek Consulting      : 564
Bitcoin Nodes            : 7762
Blocklist DE             : 25879
Bot Scout IPs            : 56
Brute Force Blocker      : 625
CI Army Badguys          : 14987
Coin Blacklist Hosts     : 7358
CyberCrime               : 2334
Danger Rulez             : 627
Darklist DE              : 7746
ET Compromised           : 622
ET Tor Rules             : 7114
IP Spamlist              : 50
MalC0de Blacklist        : 21
Malware Army             : 4383
Malware Domains          : 996
Mirai Security           : 999
MyIP Blacklist           : 1145
SSL Abuse IP List        : 86
SpamHaus Drop            : 48
Stop Forum Spam          : 178470
Talos Intel              : 1320
Threat Crowd             : 976
Threatweb Botnet IPs     : 313
Threatweb Watchlist      : 745
URL Haus                 : 96865
Windows SpyBlocker       : 358

➜  Last Modified: 2020-01-30 07:22:35
```

### Insert new Blacklist feed
```text
python blacklist_check.py" -i 
        ____  __           __   ___      __     ________              __
       / __ )/ /___ ______/ /__/ (_)____/ /_   / ____/ /_  ___  _____/ /__
      / __  / / __ `/ ___/ //_/ / / ___/ __/  / /   / __ \/ _ \/ ___/ //_/
     / /_/ / / /_/ / /__/ ,< / / (__  ) /_   / /___/ / / /  __/ /__/ ,<
    /_____/_/\__,_/\___/_/|_/_/_/____/\__/   \____/_/ /_/\___/\___/_/|_|
     v2.0
     
Feed name: Windows SpyBlocker
Feed url: https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/firewall/extra.txt

[ Checking URL ]
✔  URL is good
✔  Added feed: "Windows SpyBlocker": "https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/firewall/extra.txt"

[ Updating new feed ]
✔  371 IPs added to 'Windows SpyBlocker'
```

### Remove Blacklist feed
Removes entry from both the feeds and blacklist
```
python blacklist_check.py" -r
 1) Alien Vault Reputation   http://reputation.alienvault.com/reputation.data
 2) Bambenek Consulting      https://osint.bambenekconsulting.com/feeds/c2-masterlist.txt
 3) Bitcoin Nodes            https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bitcoin_nodes.ipset
 4) Blocklist DE             http://www.blocklist.de/lists/all.txt
 5) Bot Scout IPs            https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/botscout.ipset
 6) Brute Force Blocker      https://panwdbl.appspot.com/lists/bruteforceblocker.txt
 7) CI Army Badguys          http://www.ciarmy.com/list/ci-badguys.txt
 8) Coin Blacklist Hosts     https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/coinbl_hosts.ipset
 9) CyberCrime               https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cybercrime.ipset
10) Danger Rulez             http://danger.rulez.sk/projects/bruteforceblocker/blist.php
11) Darklist DE              https://www.darklist.de/raw.php
12) ET Compromised           https://rules.emergingthreats.net/blockrules/compromised-ips.txt
13) ET Tor Rules             https://rules.emergingthreats.net/blockrules/emerging-tor.rules
14) GreenSnow                https://blocklist.greensnow.co/greensnow.txt
15) IP Spamlist              http://www.ipspamlist.com/public_feeds.csv
16) MalC0de Blacklist        http://malc0de.com/bl/IP_Blacklist.txt
17) Malware Army             https://malware.army/api/honey_iplist
18) Malware Domains          http://www.malwaredomainlist.com/hostslist/ip.txt
19) Mirai Security           https://mirai.security.gives/data/ip_list.txt
20) MyIP Blacklist           https://www.myip.ms/files/blacklist/csf/latest_blacklist.txt
21) OpenPhish                https://openphish.com/feed.txt
22) PhishTank                http://data.phishtank.com/data/online-valid.csv
23) SSL Abuse IP List        https://panwdbl.appspot.com/lists/sslabuseiplist.txt
24) SpamHaus Drop            https://panwdbl.appspot.com/lists/shdrop.txt
25) Stop Forum Spam          https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/stopforumspam.ipset
26) Talos Intel              https://talosintelligence.com/documents/ip-blacklist
27) Threat Crowd             https://www.threatcrowd.org/feeds/ips.txt
28) Threatweb Botnet IPs     https://www.threatweb.com/access/Botnet-IPs-High_Confidence_BL.txt
29) Threatweb Watchlist      https://www.threatweb.com/access/SIEM/OPTIV_HIGH_CONFIDENCE_SIEM_IP_WATCHLIST.txt
30) URL Haus                 https://urlhaus.abuse.ch/downloads/csv_recent/
31) Windows SpyBlocker       https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/firewall/extra.txt

Please select your choice by number: 31
✔ Successfully removed feed: "Windows SpyBlocker"
```

### Check if IP is blacklisted

#### Single

```text
python blacklist_check.py" -q 104.152.52.31
  
✖  Blacklisted [104.152.52.31] > Alien Vault Reputation
   Location: United States (US)

✖  Blacklisted [104.152.52.31] > CI Army Badguys
   Location: United States (US)

................................
[ Reputation Block List Check ]
✖  Blacklisted > abuse-contacts.abusix.org
✖  Blacklisted > abuse.spfbl.net
✖  Blacklisted > all.s5h.net
✖  Blacklisted > black.dnsbl.brukalai.lt
✖  Blacklisted > contacts.abuse.net
✖  Blacklisted > dnsbl.justspam.org
✖  Blacklisted > dnsbl.rymsho.ru
✖  Blacklisted > dnsbl.spfbl.net
✖  Blacklisted > dnsbl-2.uceprotect.net
✖  Blacklisted > free.v4bl.org
✖  Blacklisted > light.dnsbl.brukalai.lt
✖  Blacklisted > origin.asn.spameatingmonkey.net
✖  Blacklisted > origin.asn.cymru.com
✖  Blacklisted > peer.asn.cymru.com
✖  Blacklisted > rbl.rbldns.ru

[*] 104.152.52.31 is listed in 15 block lists

................................
[ IP-46 IP Intel Check ]
294 attacks reported for 104.152.52.31 (mainly by Port Scan). 104.152.52.31 is an Open Proxy used by Hackers

................................
[ URLhaus Check ]
✔  NOT LISTED 
```

#### Multiple inline

```text
python blacklist_check.py -q 5.255.250.96, 78.46.85.236, 46.229.168.146
  
✔  NOT LISTED  [5.255.250.96]
   Location: Moscow, Russia (RU)

✔  NOT LISTED  [78.46.85.236]
   Location: Germany (DE)

✔  NOT LISTED  [46.229.168.146]
   Location: Ashburn, Virginia (US)
```

#### Multiple from file

```text
python blacklist_check.py -f ip_list.txt
```

#### IP Whois Lookup

```text
python blacklist_check.py -q 75.62.69.12, 12.16.5.23, 87.56.25.4, 18.23.36.2 -w

..............................
[ Performing IP whois lookup ]


✔  NOT LISTED  [75.62.69.12]
   Location: Allen, Texas (US)
   Whois:  AT&T Corp.


✔  NOT LISTED  [12.16.5.23]
   Location: United States (US)
   Whois:  AT&T Services, Inc.


✔  NOT LISTED  [87.56.25.4]
   Location: Denmark (DK)
   Whois:  TDC BB-ADSL users


✔  NOT LISTED  [18.23.36.2]
   Location: United States (US)
   Whois:  Massachusetts Institute of Technology
```

#### VirusTotal Check (requires api key)

```text
python blacklist_check.py -q 3.135.65.187 -vt
................................
[ VirusTotal Check ]
Please add VT API key to the 'settings.yml' file, or enter it below
Enter key: <API KEY>
= URLs =
> http://3.135.65.187/
  Positives: 2
  Scan Date: 2020-12-03 03:29:33

> http://3.135.65.187/iejbl7.rar/
  Positives: 6
  Scan Date: 2020-12-03 03:16:08

> http://3.135.65.187/iejbl7.rar
  Positives: 7
  Scan Date: 2020-12-03 01:33:59

> https://3.135.65.187/
  Positives: 2
  Scan Date: 2020-12-03 01:10:16

> http://3.135.65.187/ek2atk2q.zip
  Positives: 8
  Scan Date: 2020-11-19 14:07:04

> http://3.135.65.187/goal.php
  Positives: 2
  Scan Date: 2020-11-17 19:04:07

> http://3.135.65.187/wp-content/uploads/2020/10/zinold.php
  Positives: 1
  Scan Date: 2020-11-05 06:41:45

= Hashes =
> 2aa35dc4f75e7a7a3e26561c5f051a50c4c13f90a3e2ac2c663139868f35f09f
  Positives: 19
  Date: 2020-12-02 20:07:21

> f2e354c9a4a21528e843122e38ed656d665a5e32141e26a1d60602a382d44912
  Positives: 20
  Date: 2020-11-19 12:02:02

> 83c390d82e19beec14d007b7350f4296c23ce9b3d131a3670ebb7424ad917410
  Positives: 12
  Date: 2020-11-18 22:42:02

> d49f5b9b3da2c5ae18f28c40d008544337ba6e5febd76a8c88619079d0c262ca
  Positives: 19
  Date: 2020-11-18 11:43:21
```
