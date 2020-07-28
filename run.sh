#!/usr/bin/env bash
cd ~/sh-report-archive
./scrape.py
./compare.py
cp current.csv debug-intended-history/$(date +%Y.%m.%d-%H:%M:%S).csv
mv current.csv last.csv
git add .
git commit -m "sadf"
git push

