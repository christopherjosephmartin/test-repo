#!/usr/bin/env python

#Use the ciscoconfparse library to find the crypto maps that are using 'pfs group2'

#Below is block of code taken from the file that we are going to be looking for

#crypto map CRYPTO 10 ipsec-isakmp
#set peer 1.1.1.1
# set transform-set AES-SHA
# set pfs group5
# match address VPN-TEST1
#crypto map CRYPTO 20 ipsec-isakmp
# set peer 2.2.2.1
# set transform-set AES-SHA
# set pfs group2
# match address VPN-TEST2
#crypto map CRYPTO 30 ipsec-isakmp
# set peer 3.3.3.1
# set transform-set AES-SHA
# set pfs group2
# match address VPN-TEST3
#crypto map CRYPTO 40 ipsec-isakmp
# set peer 4.4.4.1
# set transform-set AES-SHA
# set pfs group5
# match address VPN-TEST4
#crypto map CRYPTO 50 ipsec-isakmp
# set peer 5.5.5.1
# set transform-set 3DES-SHA
# set pfs group5
# match address VPN-TEST5

from ciscoconfparse import CiscoConfParse

def main():
    file1 = 'cisco.txt'
    cisco_file = CiscoConfParse(file1)

    crypto = cisco_file.find_objects_w_child(parentspec=r'crypto map CRYPTO', childspec=r'pfs group2')

    print '\nCrypto Maps using PFS group2:'
    for entry in crypto:
        print entry.text
    print

if __name__ == "__main__":
    main()

