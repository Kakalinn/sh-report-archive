#!/usr/bin/env bash
./scrape.py
./compare.py
cp current.csv debug-intended-history/$(date +%Y.%m.%d-%H:%M:%S).csv
mv current.csv last.csv
git add .
git commit -m "sadf"
git push

