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

global silent
silent = False

# !------------------------------!
# ! Start                        !
# !                              !
# !------------------------------!

__version__ = "develop"


class CallableModule():

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def __call__(self, *args, **kwargs):
        return self._wrapped.main(*args, **kwargs)

    def __getattr__(self, attr):
        return object.__getattribute__(self._wrapped, attr)


sys.modules[__name__] = CallableModule(sys.modules[__name__])

def no_update():
    silent = True

def silent():
    no_update()

def online():
    try:
        sock = socket.create_connection(("www.google.com", 80))
        if sock is not None:
            sock.close
        return True
    except OSError:
        pass
    return False

def checkver():
    if online() == True:
        packagenm = 'input_num'
        latest_version = "ERR"
        responseinfl = requests.get(f'https://pypi.org/pypi/{packagenm}/json')
        latest_version = responseinfl.json()['info']['version']
        if latest_version != __version__:
            if silent == False:
                print("[{}] New update is here, run 'python3 -m pip install --upgrade input_num' THREE TIMES in normal terminal".format(packagenm))

checkver()


def output_num(val):
    global opt2l
    if val == None or val == "None":
        if str(opt2l).lower() == "false" or str(opt2l).lower() == False:
            return main(val, option, option2)
        else:
            return str("")
    else:
        try:
            return int(val)
        except:
            return str("")
        finally:
            pass


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
