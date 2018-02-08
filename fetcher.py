# For Python 2.7
# Author: Park, Han Gyu
#
# NOTE: using default user for now.

import os
import argparse
import ConfigParser

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--set-ip", type=str, default=None,
                    help="XXX.XXX.XXX.XXX")

parser.add_argument("-p", "--set-port", type=str, default=None,
                    help="xxxxx")

parser.add_argument("--set-path", type=str, default=None,
                    help="/path/to/target")

parser.add_argument("--check", action="store_true",
                    help="print default fetch setting")

parser.add_argument("target", type=str,
                    help="print default fetch setting")

parser.add_argument("dest", type=str,
                    help="print default fetch setting")


def main():
    config = ConfigParser.SafeConfigParser()
    config.read('config.ini')
    args = parser.parse_args()

    # Check new configurations
    if args.set_ip:
        ip = args.set_ip
        config.set('DEFAULT', 'IP', ip)
    else:
        ip = config.get('DEFAULT', 'IP')
    if args.set_port:
        port = args.set_port
        config.set('DEFAULT', 'PORT', ip)
    else:
        port = config.get('DEFAULT', 'PORT')
    if args.set_path:
        path = args.set_path
        config.set('DEFAULT', 'path', ip)
    else:
        path = config.get('DEFAULT', 'path')

    # Update new configurations
    with open('config.ini', 'wb') as configfile:
        config.write(configfile)

    print("Target IP  : " + ip)
    print("Target Port: " + port)
    print("Target Path: " + path)

    if args.check:
        pass
    else:
        com = "scp -P " + port + " "
        com += ip + ":" + path + "/" + args.target + " "
        com += args.dest
        print("Executing:\n\t" + com)
        os.system(com)

if __name__ == "__main__":
    main()
