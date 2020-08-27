#!/usr/bin/env python3
# Read the last scrape and compare it to the current.
# All lines in last.csv, but not in current.csv are appended to archive.csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", help = "Doesn't print to archive.csv, prints to stdout instead.", action = "store_true")
args = parser.parse_args()

fcur = open("current.csv", "r")
flast = open("last.csv", "r")
farch = open("archive.csv", "a")

cur = [ll.rstrip('\n') for ll in fcur]
last = [ll.rstrip('\n') for ll in flast]

for e in last[::-1]:
    if e not in cur:
        if args.debug: print(e)
        else: farch.write(e + '\n')

fcur.close()
flast.close()
farch.close()
