"""
find and open wifi captive portal (such as Starbucks)
written by Jess Sullivan
"""
from netifaces import gateways
from sys import argv
from time import sleep
import subprocess

help_str = str("\n " +
               'usage: \n ' +
               ' -h : print this message again \n' +
               ' -i : `pip3 install netifaces`  \n' +
               'You may specify a browser argument to complete the portal, such as \n' +
               'google-chrome')


def argtype():
    try:
        if len(argv) > 1:
            use = True
        elif len(argv) == 1:
            use = False
            print(help_str)
        else:
            print('command takes 0 or 1 args, use -h for help')
            raise SystemExit
    except:
        print('arg error... \n command takes 0 or 1 args, use -h for help')
        raise SystemExit
    return use


def main():

    all_gates = gateways()
    target = all_gates['default'][2][0]

    if argtype():

        if argv[1] == '-h':
            print(help_str)
            quit()

        if argv[1] == '-i':
            try:
                subprocess.Popen('pip3 install netifaces',
                                 shell=True,
                                 executable='/bin/bash')
                sleep(1)
                quit()
            except:
                print('err running pip3 install netifaces')
                quit()

        else:

            print(str('opening portal in ' + argv[1]))
            subprocess.Popen(str(argv[1] + ' ' + str(target)),
                             shell=True,
                             executable='/bin/bash')
            sleep(1)
            quit()

    else:

        print(str('\n please visit address ' + target +
                  ' in a browser to complete portal setup \n'))
        quit()


main()
