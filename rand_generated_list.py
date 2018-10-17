#!/usr/bin/env python3.6
import time,mwclient,csv,random
listing = []
listing2 = []
rows = []

def process():
    # listing = []
    # listing2 = []
    # rows = []
    #f = open('./output00.txt','a+')
    with open('./proposed_amendments.csv') as csvfile:
        readCSV = csv.reader(csvfile,delimiter=',')
        for row in readCSV:
            rows.append(row)
            listing.append(row[0])
            # f.write(row[0] + "\n")
            listing2.append(row[1])
                # f.close()
# f2.close()

#site = mwclient.Site(('https','en.wikipedia.org'), '/w/')

process()
f = open("list.txt","a+")
nums = []
for i in range(150):
    r=random.randint(1,len(listing))
    if r not in nums: nums.append(r)
for n in nums:
    f.write("* " + listing[n] + "  ---->  " + listing2[n] + "\n")
    #for x in range(100):
    #num = random.sample(listing,100)
#f.write("• " + listing[num] + "  ---->  " + listing2[num] + "\n")
f.close()
