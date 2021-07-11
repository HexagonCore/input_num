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

lvers = "0.0.13"

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


def main(val, option = "true"):
    global output
    output = input(val)
    if " " in str(output).lower() or str(output).lower() == "" or str(output).lower() == None:
        return str("")
    else:
        try:
            nothing = float(int(output))
        except:
            return main(val, option)
        finally:
            if str(option).lower() == "true" or str(option).lower() == True:
                if output == None or output == "None":
                    return str("")
                else:
                    return int(output)
            else:
                if str(option).lower() == "false" or str(option).lower() == False:
                    if "-" in str(output):
                        return main(val, option)
                    else:
                        if output == None or output == "None":
                            return str("")
                        else:
                            return int(output)
                else:
                    if output == None or output == "None":
                        return str("")
                    else:
                        return int(output)


#!------------------------------!
#!       End                    !
#!                              !
#!------------------------------!
