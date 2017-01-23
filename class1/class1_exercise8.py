#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

def main():
    #Find all the crypto map entries and print out the children of each
    #Start by assigning the text file i want to open to variable called cisco_file
    #Then use the 'CiscoConfParse' function to reference the variable which opens the file

    cisco_file = 'cisco.txt'

    cisco_cfg = CiscoConfParse(cisco_file)

    #Find all objects within the text file that begin 'crypto map CRYPTO' and assign to variable 'crypto_maps'

    crypto_maps = cisco_cfg.find_objects(r"^crypto map CRYPTO")

    for i in crypto_maps:
        print
        print i.text
        for child in i.children:
            print child.text
    print

if __name__ == "__main__":
    main()

