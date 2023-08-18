#!/usr/bin/env python3

for bottles in range(99,0,-1):
    if bottles > 1:
        print(f"{bottles} of beer on the wall, {bottles} of beer.")
        print(f"Take on down, passit around. {bottles -1} of beer on the wall")
    else:
        print("1 bottle of beer on the wall. 1 bottle of beer")
        print("Take one down. Pass it around. No more bottles of beer on the wall")

print("No more bottle of beer on the wall. No more bottles of beer.")
print("Go to the store and buy some more. 99 bottles of beer on the wall.")
