#!/usr/bin/env bash
cd /home/kakali/programming/sh-report-archive
./scrape.py
./compare.py
cp current.csv debug-intended-history/$(date +%Y.%m.%d-%H:%M:%S).csv
mv current.csv last.csv
git add .
git commit -m "Automated commit by the run.sh script at $(date +%Y.%m.%d-%H:%M:%S)"
git push

