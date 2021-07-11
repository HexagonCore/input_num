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

# !------------------------------!
# ! Start                        !
# !                              !
# !------------------------------!

lvers = "0.1.0"


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


def output_num(val):
    global opt2l
    if val == None or val == "None":
        if str(opt2l).lower() == "false" or str(opt2l).lower() == False:
            return main(val, option, option2)
        else:
            return str("")
    else:
        return int(val)


def main(val, option="true", option2="true"):
    global opt2l
    opt2l = option2
    global output
    output = input(val)
    # Did user just pressed enter?
    if " " in str(output).lower() or str(output).lower() == "" or str(output).lower() == None:
        if str(opt2l).lower() == "false" or str(opt2l).lower() == False:
            return main(val, option, option2)
        else:
            return str("")
    else:
        # He did not just press enter
        try:
            nothing = float(int(output))
        except:
            # it is not number
            return main(val, option, option2)
        finally:
            # it is number
            if str(option).lower() == "true" or str(option).lower() == True:
                return output_num(output)
            else:
                if str(option).lower() == "false" or str(option).lower() == False:
                    if "-" in str(output):
                        return main(val, option, option2)
                    else:
                        return output_num(output)
                else:
                    return output_num(output)

# !------------------------------!
# !       End                    !
# !                              !
# !------------------------------!
