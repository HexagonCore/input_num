import socket
import json
import requests
import os 
import sys
import time

#!------------------------------!
#! Start of getNGROK functions  !
#!   Please scroll to bottom    !
#!------------------------------!


#last line deletion
def delete_last_line():
    "Use this function to delete the last line in the STDOUT"

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')


def err_gtngr_do_not_use_for_urself():
    delete_last_line()
    print("Error: wrong tunnel name specified or no tunnel is running\n")

def gtngr_do_not_use_for_urself():
    url = "http://localhost:4040/api/tunnels/"
    
#  ---------Configurable---ˇ--------------------------------------------------------------------------------#
    tunnel_name = "command_line"
#  ---------Configurable---^--------------------------------------------------------------------------------#

    time.sleep(0.01)
    delete_last_line()
    print('Getting Ngrok stats from tunnel "{}"..'.format(par_tnl))
    try:
        res = requests.get(url)
        res_unicode = res.content.decode("utf-8")
        res_json = json.loads(res_unicode)
        for i in res_json["tunnels"]:
            if i['name'] == tunnel_name:
                delete_last_line()
                print('Getting Ngrok stats from tunnel "{}"...'.format(par_tnl))
                return i['public_url']
                break
    except:
        err = 1




def get_stats_n(tnl_nm = "command_line"):
    global ngr
    global err
    global tnl_type
    global ip
    global port
    global adress
    global par_tnl
    par_tnl = tnl_nm
    err = 0
    print('Getting Ngrok stats from tunnel "{}".'.format(par_tnl))
    ngr = gtngr_do_not_use_for_urself()
    time.sleep(0.01)
    tcp = 5
    try:
        if ngr.find("tcp://") != -1:
            tcp = 1
        else:
            tcp = 0
    except:
        err_gtngr_do_not_use_for_urself()
    
    if tcp == 1:
        try:
            ngr = ngr.replace("tcp://", "")
        except:
            err = 1
            err_gtngr_do_not_use_for_urself()
            adress = "ERR"
            ip = "ERR"
            port = "ERR"
            tnl_type = "ERR"
        if err == 0:
            ngr = ngr.split(":")
            adress = ngr[0]
            port = ngr[1]
            tnl_type = "TCP"
            try:
                ip = socket.gethostbyname(adress)
            except:
                ip = "ERR NO CONNECTION"
                tnl_type = "TCP (no connection)"
            delete_last_line()
            print("NAME:  ", par_tnl)
            print("TYPE:  ", tnl_type)
            print("ADRESS:", adress)
            print("IP:    ", ip)
            print("PORT:  ", port)
            print("")
            
    if tcp == 0:
        try:
            ngr = ngr.replace("https://", "")
        except:
            err = 1
            err_gtngr_do_not_use_for_urself()
            adress = "ERR"
            ip = "ERR"
            port = "ERR"
            tnl_type = "ERR"
        if err == 0:
            adress = ngr
            tnl_type = "HTTPS"
            try:
                ip = socket.gethostbyname(adress)
            except:
                ip = "ERR NO CONNECTION"
                tnl_type = "HTTPS (no connection)"
            delete_last_line()
            print("NAME:  ", par_tnl)
            print("TYPE:  ", tnl_type)
            print("ADRESS:", adress)
            print("IP:    ", ip, "\n")
    

    
#!------------------------------!
#!       End of getNGROK        !
#! Ur code goes below (optional)!
#!------------------------------!


# ˇThis function actually gets the stats, you can use it anywhereˇ
#-----------------------------------------------------------------#
get_stats_n("command_line")
#-----------------------------------------------------------------#
# ^This function actually gets the stats, you can use it anywhere^ 

#     WHAT IS THE "command_line" PARAMETER? Check this out https://ngrok.com/docs#tunnel-definitions
#     IF YOU DO NOT USE IT, LEAVE IT BLANK: get_stats_n()

print("Hello world!")