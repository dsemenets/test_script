#!/usr/bin/env python3
import yaml
import os
import argparse


def main():
    ret = 0
    parser = argparse.ArgumentParser(description="fota")
    parser.add_argument('conf',
                        metavar='conf.yaml',
                        type=str,
                        help='YAML file with configuration')
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("-l", "--layers", nargs="*", help="List of enabled layers")
    parser.add_argument("-f", "--file", action="store", help="Config file with enabled layers")
    args = parser.parse_args()
    print(args)
    print(f"Using conf {args.conf}")
    return ret

if __name__ == "__main__":
    exit(main())
