#!/usr/bin/env python3


import crayons

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys():
        print(f'{crayons.red("Handshaking")}. .. ... connecting with {ip}')
        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}')
    return None

# start our main script
def main():
    """called at runtime"""

    devicemd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth/5", "noshutdown"]}
    print("Welcome to the {crayons.blue ('network')} device command pusher")
    print("\nData set found\n")
    commandpush(devicemd)

main()
