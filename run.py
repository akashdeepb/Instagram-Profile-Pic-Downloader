import requests
import os
import re
import sys

# Variable Initialization and Declarations
PROFILE_UNAME=""
OUTPUT=""
URL="https://www.instagram.com/"

# Check if no arguments are given 
if len(sys.argv) == 1:
    PROFILE_UNAME = input("Enter Username : ")

# Loop through all the Arguments
for i in range(len(sys.argv)):
    # Get Output name from Args
    if str(sys.argv[i]) == '-o' or str(sys.argv[i]) == '--output':
        try:
            OUTPUT = sys.argv[i+1]
        except:
            print("Invalid Output Filename")
            exit(0)
    
    # Show help Text 
    if str(sys.argv[i]) == '-h' or str(sys.argv[i]) == '--help':
        print("\n\n Instagram-Profile-Pic-Downloader\n Git Repository : https://www.github.com/akashdeepb/Instagram-Profile-Pic-Downloader\n\n -u \t Username \n -o \t Output Filename \n -h \t Well this is what happens ;)\n\n")
        exit(0) 
    # Get Username from Args
    if str(sys.argv[i]) == '-u' or str(sys.argv[i]) == '--username':
        try:
            PROFILE_UNAME = sys.argv[i+1]
        except:
            print("Invalid Username")
            exit(0)

# If Username not Given as User to input
if len(PROFILE_UNAME) == 0:
    PROFILE_UNAME = input("Enter Instagram Username : ")
if len(OUTPUT) == 0:
    OUTPUT = PROFILE_UNAME

# Start a new Session
r = requests.Session()
res = r.get(URL+PROFILE_UNAME+"/")  # Make GET request to Instagram
pic_url = ""
# Get all lines of response
for line in res.text.splitlines():
    # Search for line containing Profile Picture
    if re.search("property=\"og:image\"", line):
        pic_url = line.split()[2][9:-1] # Extract Profile Picture link
        break

# Exit if Couldn't find Image URL
if(len(pic_url) == 0):
    print("Couldn't Find Image")
    exit(0)
# Make GET request to Image URL
res = r.get(pic_url)
if res.status_code == 200:      # If link works
    with open(OUTPUT, 'wb') as f:
        for chunk in res:
                f.write(chunk)
    print("Image Downloaded. File Name : " + OUTPUT)
