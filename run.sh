#!/usr/bin/env bash
./scrape.py
./compare.py
mv current.csv last.csv
