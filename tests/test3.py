#!/usr/bin/env python3.6
import time,mwclient,csv


def process():
    listing = []
    listing2 = []
    rows = []
    f = open('./output00.txt','a+')
    f2 = open('./output01.txt','a+')
    with open('./proposed_amendments.csv') as csvfile:
        readCSV = csv.reader(csvfile,delimiter=',')
        for row in readCSV:
            rows.append(row)
            listing.append(row[0])
            f.write(row[0] + "\n")
            listing2.append(row[1])
            f2.write(row[1] + "\n")
    f.close()
    f2.close()

#site = mwclient.Site(('https','en.wikipedia.org'), '/w/')

process()
