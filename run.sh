#!/usr/bin/env bash
cat 1 > test.txt
./scrape.py
cat 2 > test.txt
./compare.py
cat 3 > test.txt
cp current.csv debug-intended-history/$(date +%Y.%m.%d-%H:%M:%S).csv
cat 4 > test.txt
mv current.csv last.csv
cat 5 > test.txt
git add .
cat 6 > test.txt
git commit -m "Automated commit by the run.sh script"
cat 7 > test.txt
git push
cat 8 > test.txt

