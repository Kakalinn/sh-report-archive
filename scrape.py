#!/usr/bin/env python3
import requests, bs4

url = 'http://www.surfheaven.eu/reports/'
headers = {"User-Agent":"Mozilla/5.0"}
response = requests.get(url, headers=headers)
html = bs4.BeautifulSoup(response.text, 'html5lib')

s = str(html)

for i in range(len(s) - 10):
    if s[i] == 'a' and s[i + 1] == 'a' and s[i + 2] == 'D' and s[i + 3] == 'a' and s[i + 4] == 't' and s[i + 5] == 'a': break
a = []
while True:
    l = []
    ll = []
    while s[i] != '{': i += 1
    i += 1
    while s[i] != '}':
        if s[i] == '<' and s[i - 4] != 'r':
            while s[i] != '>': i += 1
            i += 1
        if s[i] == '<' and s[i - 4] == 'r':
            ll.append(',')
            ll.append('"')
            ll.append('I')
            ll.append('D')
            ll.append('"')
            ll.append(':')
            ll.append('"')
            while s[i] != '>':
                if s[i] >= '0' and s[i] <= '9': ll.append(s[i])
                i += 1
            ll.append('"')
            i += 1

        l.append(s[i])
        i += 1
    for e in ll: l.append(e)
    a.append(''.join(l).join(ll))
        
    if s[i + 1] == ']': break
l = []
for i in range(len(a)):
    j = 0
    l.append([])
    for t in range(8):
        k = []
        while a[i][j] != '"': j += 1
        j += 1
        while a[i][j] != '"': j += 1
        j += 1
        while a[i][j] != '"': j += 1
        j += 1
        while a[i][j] != '"':
            k.append(a[i][j])
            j += 1
        j += 1
        l[-1].append(''.join(k))
# each element of l looks like [status, date, map, report, author, comment, authorID]

f = open("/home/pi/programming/sh-report-archive/current.csv", "w")
for e in l: f.write('"%s","%s","%s","%s","%s","%s",%s\n' % (e[1], e[2], e[3], e[4], e[5], e[6], e[7]))
f.close()

