#!/usr/bin/env bash
echo 1 > test.txt
./scrape.py
echo 2 > test.txt
./compare.py
echo 3 > test.txt
cp current.csv debug-intended-history/$(date +%Y.%m.%d-%H:%M:%S).csv
echo 4 > test.txt
mv current.csv last.csv
echo 5 > test.txt
git add .
echo 6 > test.txt
git commit -m "Automated commit by the run.sh script"
echo 7 > test.txt
git push
echo 8 > test.txt

