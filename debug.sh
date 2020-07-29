#!/usr/bin/env bash
cd ~/sh-report-archive
./scrape.py
./compare.py -d
rm current.csv
