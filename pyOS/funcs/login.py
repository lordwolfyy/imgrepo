
import os
import subprocess
import time
import re

def getpass(username):
    try:
        with open(f"/workspaces/imgrepo/pyOS/passwds/.pass4{username}", "r") as passwd:
            paswd = passwd.read()
            return paswd
    except FileNotFoundError:
        paswd = ""
        return paswd

def log(log, username, output=""):
    with open("/workspaces/imgrepo/pyOS/log.log", "a") as logfile:
        logfile.write(f"\ncommand: {log}\nuser: {username}")
        if output:
            logfile.write(f"\noutput: {output}")

def login(icon):
    admins = ["lol","lordwolfy"]
    username = input("                                  Enter your username:")
    password = input("                                  Enter your password:")
    os.system("clear")
    stored_password = getpass(username)
    if username == "":
        username = "guest"
    if stored_password is not None and password == stored_password:
        loggedin = True
    else:
        loggedin = False
        print("Login failed. Please check your username and password.")
        time.sleep(3)
        os.system("clear")
        login()
    print(icon)
    while loggedin:
        shouldexecute = True
        
        a = input(f"                                         {username}@PyOS: ")
        x = a
        r = x
        if r == "exit":
            loggedin = False
        if x == "whoami":
            print(f"                                           {username}\n\n\n")
            shouldexecute = False
        if username not in admins and re.match("sudo", r):
            print("                             User is not in the sudoers file. This will be logged.\n\n")
            log(r, username)
            shouldexecute = False
        if re.search("^cd ", r):
            m = r.replace("cd ", "")
            try:
                os.chdir(m)
                log(r, username)
                print(f"Changed directory to {os.getcwd()}")
                shouldexecute = False
            except FileNotFoundError:
                print(f"Directory '{m}' not found.")
        if re.match("^install* ", x):
            r = x.replace("install ", "sudo apt install ")
        r = x
        if x != "logout":
            x = shouldexecute
            if x == True:
                try:
                    output = subprocess.check_output(r, shell=True, stderr=subprocess.STDOUT, text=True)
                    for l in output.splitlines():
                        print(f"                {l}")
                    print("\n\n\n")
                    log(r, username, output)
                except subprocess.CalledProcessError as e:
                    print(f"                        Error {e}")
        if x == "logout":
            log(r, username)
            loggedin = False
            os.system("clear")
            login()