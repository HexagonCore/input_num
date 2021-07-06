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

class CallableModule():

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def __call__(self, *args, **kwargs):
        return self._wrapped.main(*args, **kwargs)

    def __getattr__(self, attr):
        return object.__getattribute__(self._wrapped, attr)

sys.modules[__name__] = CallableModule(sys.modules[__name__])


def checkver():
    packagenm = 'input_num'
    responseinfl = requests.get(f'https://pypi.org/pypi/{packagenm}/json')
    latest_version = responseinfl.json()['info']['version']
    if latest_version != lvers:
        print("You are not using latest version, run 'python3 -m pip install --upgrade input_num' three times")

        
checkver()


def main(val, option = "false"):
    global output
    try:
        output = input(val)
        nothing = float(int(output))
    except:
        main(val, option)
    finally:
        return output


#!------------------------------!
#!       End                    !
#!                              !
#!------------------------------!
