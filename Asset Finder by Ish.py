import requests
import os
import threading
from colorama import Fore, Back, Style

threadsnum = input("Enter threads amount: ")
print("1 - search for single asset")
print("2 - search for multiple assets (from assets.txt)")
userid = 1
infloop = True
optionreq = input()

def assetfinderone(ishisthebest):
    global assetid
    global userid
    while infloop == True:
        r = requests.get(f"https://api.roblox.com/users/{userid}")
        if "Username" in r.json():
            currusername = r.json()["Username"]
            checking = requests.get(f"http://api.roblox.com/Ownership/HasAsset?userId={userid}&assetId={assetid}")
            if checking.json() == False:
                print(Fore.RED + f"User does not own the asset | Username: {currusername} - User ID: {userid}")
                Style.RESET_ALL
            else:
                print(Fore.GREEN + f"User owns the asset | Username: {currusername} - User ID: {userid} | Saved in owners.txt")
                Style.RESET_ALL
                open("owners.txt", "a+").write(f"Username: {currusername} | User ID: {userid} | Profile: https://www.roblox.com/users/{userid}/profile | Owns asset ID: {assetid}\n")
            userid = str(int(userid) + 1)
        else:
            print(Fore.RED + "User is banned, skipping")
            Style.RESET_ALL
            userid = str(int(userid) + 1)

def assetfindertwo(ishisthebest):
    global assets
    global checkusers
    global userid
    for line in assets:
        assetid = line.split()
        if userid == checkusers:
            print(f"Finished checking for {assetid}")
            continue
        else:
            for x in range(int(checkusers)):
                r = requests.get(f"https://api.roblox.com/users/{userid}")
                if "Username" in r.json():
                    currusername = r.json()["Username"]
                    checking = requests.get(f"http://api.roblox.com/Ownership/HasAsset?userId={userid}&assetId={assetid}")
                    if checking.json() == False:
                        print(Fore.RED + f"User does not own the asset ({assetid}) | Username: {currusername} - User ID: {userid}")
                        Style.RESET_ALL
                    else:
                        print(Fore.GREEN + f"User owns the asset ({assetid}) | Username: {currusername} - User ID: {userid} | Saved in owners.txt")
                        Style.RESET_ALL
                        open("owners.txt", "a+").write(f"Username: {currusername} | User ID: {userid} | Profile: https://www.roblox.com/users/{userid}/profile | Owns asset ID: {assetid}\n")
                    userid = str(int(userid) + 1)
                else:
                    print(Fore.RED + "User is banned, skipping")
                    Style.RESET_ALL
                    userid = str(int(userid) + 1)

if optionreq == "1":
    os.system("cls")
    assetid = input("Enter asset id: ")
    threads = list()
    for index in range(int(threadsnum)):
        x = threading.Thread(target=assetfinderone, args=(index,))
        threads.append(x)
        x.start()

elif optionreq == "2":
    os.system("cls")
    checkusers = input("Enter how many users you want to check for asset (for each asset): ")   
    assets = open("assets.txt", "r+")
    threads = list()
    for index in range(int(threadsnum)):
        x = threading.Thread(target=assetfindertwo, args=(index,))
        threads.append(x)
        x.start()
    