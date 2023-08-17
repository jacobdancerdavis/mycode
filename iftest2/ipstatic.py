#!/usr/bin/env python3
"""Alta3 Research | RFeeser
    conditionals - strings test true"""

ipchk = input("Apply an IP address: ")

# a string tests as true
if ipchk == "192.168.70.1":
    print("looks like the IP address of the gateway was set: " + ipchk)
elif ipchk:
    print("looks like the IP address was set: " + ipchk)
else:
    print("You did not provide input.")

