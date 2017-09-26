import os
import subprocess as sp


networkElements = {
    "Simons Router":"192.168.0.1",
    "Simons Wifi Dish":"192.168.0.2",
    "Our Wifi Dish":"192.168.0.3",
    "House Router":"10.0.0.1",
    "Intenet":"194.168.4.100",
    }

def check_ping(hostname):
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    return pingstatus

def ipcheck(pop):
    #status,result = sp.getstatusoutput("ping -c1 -w2 " + pop + "nul")
    HOST_UP = True if os.system("ping -c 1 " + pop +" >nul") is 0 else False
    if HOST_UP == True:
        pingstatus = " is UP !"
    else:
        pingstatus = " is Down !"
    return pingstatus

def check_home(hosts_to_check):
    for hostName, ipAddress in hosts_to_check.items():
        print ("Testing : ", hostName, " at Address: ",ipAddress, ipcheck(ipAddress))

check_home(networkElements)
