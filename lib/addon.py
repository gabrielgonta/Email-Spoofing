# Some Additional Codes For Email-Spoofing Script

import os
import sys
import time
import shutil
import requests
try:
    import version
except:
    os.system("pip install tool-version-checker > /dev/null 2>&1")
    import version

columns = shutil.get_terminal_size().columns

def psb(z):
    for p in z + "\n":
        sys.stdout.write(p)
        sys.stdout.flush()
        time.sleep(0.01)

##Logo##
def logo():
    os.system("clear")
    print("\033[94m┌────────────────────────────────────────┐".center(columns+5))
    print("\033[94m│       \033[92m▛▀▘       ▗▜  ▀▛▘     ▜\033[94m          │".center(columns+15))
    print("\033[94m│       \033[92m▙▄ ▛▚▀▖▝▀▖▄▐   ▌▞▀▖▞▀▖▐ ▞▀▘ \033[94m     │".center(columns+15))
    print("\033[94m│       \033[92m▌  ▌▐ ▌▞▀▌▐▐   ▌▌ ▌▌ ▌▐ ▝▀▖\033[94m      │".center(columns+15))
    print("\033[94m│       \033[92m▀▀▘▘▝ ▘▝▀▘▀▘▘  ▘▝▀ ▝▀  ▘▀▀ \033[94m      │".center(columns+15))
    print("\033[94m│                              \033[94m          │".center(columns+9))
    print("\033[94m│ \033[95mAuthor : GabrielGonta                     \033[94m│".center(columns+15))
    print("│ \033[95mTool   : A Email Toolkit               \033[94m│".center(columns+9))
    print("│ \033[95mGitHub : https://github.com/gabrielgonta \033[94m│".center(columns+9))
    print("│ \033[95mCoder  : GabrielGonta             \033[37mV1.0  \033[94m│".center(columns+15))
    print("\033[94m└────────────────────────────────────────┘".center(columns+5))


#ContactGabrielGonta
def contact():
    logo()
    psb("\n\033[92m    [\033[37m★\033[92m] Thanks For Using Our Tool..")

#ExitTool
def logout():
    psb("\n\033[92m    [\033[37m★\033[92m] Thanks For Using Our Tool..")
    psb("\n\033[92m    [\033[37m★\033[92m] For More Tools, Visit:\n")
    print("\033[94m[\033[37m https://github.com/gabrielgonta/ \033[94m]".center(columns+13))
    sys.exit("\033[37m")

#ShortURL
def short_url(url):
    short = requests.get("https://is.gd/create.php?format=simple&url="+url).text
    if not ("//is.gd/" in short):
        short = ""
    return short

#CheckUpdate
def check_version():
    version.custom(check = "$blank$", checkSuccess = "$blank$", update = "\033[92m    [\033[37m*\033[92m] Tool Update Found...\n\033[92m    [\033[37m*\033[92m] Updating Tool...", updateSuccess = "\n\033[92m    [\033[37m*\033[92m] Tool Updated Successfully...\n\033[92m    [\033[37m*\033[92m] Starting Tool...", printType = "flush")
    version.check(verFile = "lib/.version", RepoFile = "email-spoofing.py", RepoURL = "https://github.com/gabrielgonta/Email-Spoofing")
