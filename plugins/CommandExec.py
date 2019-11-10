#!/usr/bin/python3

print('loading Modules...')

import argparse

parser = argparse.ArgumentParser(description='This program is Examine-Program.')

# bool
parser.add_argument('-e','--error', action='store_true', default=False,
                    help='show error (default: show no error)')
# num
parser.add_argument('-d','--data', type=int, help='data number')

# string
parser.add_argument('-s','--str', type=str, help='data name')

args = parser.parse_args()

print (args)

def test():
    print('in test function.')

if __name__ == '__main__':

    print('python-izm')
    test()


# Ends here.
