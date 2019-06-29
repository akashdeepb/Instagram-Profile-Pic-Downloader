import requests
import os
import re
import sys

PROFILE_UNAME=""
OUTPUT=""
URL="https://www.instagram.com/"
if len(sys.argv) == 1:
    PROFILE_UNAME = input("Enter Username : ")
    OUTPUT = input("Enter Output Filename : ")
for i in range(len(sys.argv)):
    if str(sys.argv[i]) == '-o' or str(sys.argv[i]) == '--output':
        try:
            OUTPUT = sys.argv[i+1]
        except:
            print("Invalid Output Filename")
            exit(0)
    if str(sys.argv[i]) == '-h' or str(sys.argv[i]) == '--help':
        print("HELP")
    if str(sys.argv[i]) == '-u' or str(sys.argv[i]) == '--username':
        try:
            PROFILE_UNAME = sys.argv[i+1]
        except:
            print("Invalid Username")
            exit(0)
if len(PROFILE_UNAME) == 0:
    PROFILE_UNAME = input("Enter Instagram Username : ")
if len(OUTPUT) == 0:
    OUTPUT = PROFILE_UNAME

r = requests.Session()
res = r.get(URL+PROFILE_UNAME+"/")
for line in res.text.splitlines():
    if re.search("property=\"og:image\"", line):
        pic_url = line.split()[2][9:-1]
        break
res = r.get(pic_url)
if res.status_code == 200:
    with open(OUTPUT, 'wb') as f:
        for chunk in res:
                f.write(chunk)
    print("Image Downloaded. File Name : " + OUTPUT)
