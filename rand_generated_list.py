#!/usr/bin/env python3.6
import time, mwclient, csv, random

listing = []
listing2 = []
rows = []


def process():
    # listing = []
    # listing2 = []
    # rows = []
    # f = open('./output00.txt','a+')
    with open('./proposed_amendments.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            rows.append(row)
            listing.append(row[0])
            listing2.append(row[1])


process()
f = open('list.txt', 'a+')
nums = []
for i in range(150):
    r = random.randint(1, len(listing))
    if r not in nums: nums.append(r)
for n in nums:
    f.write('* ' + listing[n] + '  ---->  ' + listing2[n] + "\n")
f.close()
