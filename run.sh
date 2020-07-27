#!/usr/bin/env bash
cd ~/sh-report-archive
./scrape.py
./compare.py
mv current.csv last.csv
git add .
git commit -m "sadf"
git push

