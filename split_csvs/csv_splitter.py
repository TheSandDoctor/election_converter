#!/usr/bin/env python3.6
import time,mwclient,csv,re


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

#NOT election(s), year
def gen_format1():
    with open('proposed_amendments.csv', 'r') as inp, open('format1.csv', 'w') as out:
        writer = csv.writer(out)
        reader = csv.reader(inp,delimiter=',')
        for row in reader:
            reg1 = re.search(r"election(?:s)?, (\d\d\d\d)$",row[0])
            if not reg1:
                #print(row[0])
                writer.writerow(row)
        #if row[2] != " 0":
        #    writer.writerow(row)
# election(s), year
def gen_format2():
    with open('proposed_amendments.csv', 'r') as inp, open('format2.csv', 'w') as out:
        writer = csv.writer(out)
        reader = csv.reader(inp,delimiter=',')
        for row in reader:
            reg1 = re.search(r"election(?:s)?, (\d\d\d\d)$",row[0])
            if reg1:
                #print(row[0])
                writer.writerow(row)
#site = mwclient.Site(('https','en.wikipedia.org'), '/w/')


gen_format2()
