#!/usr/bin/env python3

def main():

    ######### EXPLORE READ #########
    ## create file object in "r"(read) mode
    configfile = open("vlanconfig.cfg", "r")

    ## display file to the screen - .read()
    print(configfile.read())

    configfile.seek(0,0)

    ######## EXPLORE READLINES #########
    configlist = configfile.readlines()
    print(configlist)

    for x in configlist:
        print(x.strip())

        configfile.close()
        ### Always close your file

if __name__ == "__main__":
    main()
