#!/usr/bin/env python3


counter= 0
with open("dracula.txt","r") as foo:
    with open("vampytime.txt", "w") as fang:
        for line in foo:
            if "vampire" in line.lower():
                counter += 1
                fang.write(line)


print(counter)
