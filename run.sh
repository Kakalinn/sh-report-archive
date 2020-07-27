#!/usr/bin/env bash
./scrape.py
./compare.py
mv current.csv last.csv
git add .
git commit -m "sadf"
git push

