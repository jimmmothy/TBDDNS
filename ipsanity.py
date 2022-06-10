'''
#!/usr/bin/python3

Sanity check for input ipv4 addresses
Very basic, doesn't consider subnets, ipv6, or RFC1918 addresses
(simply because it isn't needed)
'''

import re
#import sys

class ipsanity:
    def __init__(self, input):

        self.input = input
        self.valid = self.sanityCheck()
    
    def sanityCheck(self) -> bool:

        regex = "^(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})$"
        reg = re.findall(regex, self.input)

        if len(reg) == 0:
            return False

        for x in reg[0]:
            if int(x) <= 0 or int(x) >= 256:
                return False
        
        return True

'''
def main():
    if len(sys.argv) != 2:
        print("??? does not compute ???")
    
    sanitycheck = ipv4sanity(sys.argv[1])
    print(f"{sys.argv[1]} valid:{sanitycheck.valid}")

if __name__ == "__main__":
    main()
'''