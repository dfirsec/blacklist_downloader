from pprint import pprint
import os
import random
import re
import sys

import requests
import sys
from bs4 import BeautifulSoup
from requests.exceptions import (ConnectionError, HTTPError, RequestException,
                                 Timeout)


class tc:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GOOD = '\033[92m' + '\033[12m' + '\u2714' + '\033[0m'
    BAD = '\033[91m' + '\033[12m' + '\u2714' + '\033[0m'


def abuseipdb(ip):
    api_key = 'f8e473bb167d4f8d6be78441b063a3f016f4fc7fe63652d20ded9a3202c9cd356f0e7b8264e25e15'
    # api_key = ''
    if not api_key:
        sys.exit("[ERROR] API Key Missing")
    headers = {'Key': api_key, 'Accept': 'application/json'}
    params = {'ipAddress': ip}

    try:
        resp = requests.get('https://api.abuseipdb.com/api/v2/check',
                            headers=headers, params=params).json()
        ip_addr = resp['data']['ipAddress']
        score = resp['data']['abuseConfidenceScore']
        if bool(ip_addr) and score > 90:
            print(f"{tc.BAD} Blacklisted: {ip}")
        else:
            print(f"{tc.GOOD} NOT blacklisted: {ip}")
    except (ConnectionError, HTTPError, RequestException,
            Timeout) as err:
        print(err)
    except KeyError:
        print("Missing data: Double-check ip and/or api key")
    except Exception as err:
        print(err)


if len(sys.argv) < 2:
    sys.exit("usage: python abuseipdb.py <ip>")
else:
    ip = sys.argv[1]
    abuseipdb(ip)
