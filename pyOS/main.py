import os as cmd 
from funcs.login import login
logo = """
                                _____        ____   _____ 
                                |  __ \      / __ \ / ____|
                                | |__) |   _| |  | | (___  
                                |  ___/ | | | |  | |\___ \ 
                                | |   | |_| | |__| |____) |
                                |_|    \__, |\____/|_____/ 
                                        __/ |              
                                    |___/               
"""
print(logo)
login(logo)
a = input("                                 Click enter to terminate process")
cmd.system("clear")