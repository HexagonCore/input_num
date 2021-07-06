## -------------------------------------------------- ##
##    So you are checking my code? Have a nice day!   ##
##    Check out http://is.gd/duhovavoda               ##
## -------------------------------------------------- ##
import socket
import json
import requests
import os 
import sys
import time


#!------------------------------!
#! Start                        !
#!                              !
#!------------------------------!

lvers = "0.0.1"


def checkver():
    packagenm = 'nput_num'
    responseinfl = requests.get(f'https://pypi.org/pypi/{packagenm}/json')
    latest_version = responseinfl.json()['info']['version']
    if latest_version != lvers:
        print("You are not using latest version, run 'python3 -m pip install --upgrade input_num' three times")

        
checkver()



#!------------------------------!
#!       End                    !
#!                              !
#!------------------------------!

