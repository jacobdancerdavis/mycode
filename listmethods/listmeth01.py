#!/usr/bin/env python3

proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
print(proto[1])
proto.append("dns")
protoa.append("dns") # this line will add d, n, and s
print(proto)
proto2 = [ 22, 80, 443, 53 ]
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)
