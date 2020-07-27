#!/usr/bin/env bash
mkdir ajk
cd ~/sh-report-archive
./scrape.py
./compare.py
mv current.csv last.csv
git add .
git commit -m "sadf"
git push
mkdir bjk

