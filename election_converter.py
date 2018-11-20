#!/usr/bin/env python3.6
import time,mwclient,csv, json, configparser
from time import sleep

def call_home(site):
    #page = site.Pages['User:' + config.get('enwiki','username') + "/status"]
    page = site.Pages['User:TheSandBot/status']
    text = page.text()
    return bool(json.loads(text)["run"]["election_converter"])
def move_page(old_title,new_title):
    page = site.Pages[old_title]
    edit_summary = """Moving page per result of [[Special:Diff/864130819|RfC on election/referendum page naming format]] using [[User:""" + config.get('enwikitsb','username') + "| " + config.get('enwikitsb','username') + """]]. Questions? See [[Special:Diff/864130819|the RfC]] or [[User talk:TheSandDoctor|msg TSD!]] (please mention that this is task #1!))"""
    return page.move(new_title,reason=edit_summary,move_talk=True, no_redirect=False) if page.exists and page.redirects_to() == None else None

listing = []
listing2 = []
rows = []
f = open('./completing.txt','a+')

#f2 = open('./output01.txt','a+')
with open('./proposed_amendments.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    for row in readCSV:
        if not call_home(site):#config):
            raise ValueError("Kill switch on-wiki is false. Terminating program.")
        if move_page(row[0],row[1]):
            f.write("Converted " + row[0] + " ----> " + row[1] + "\n")
                sleep(4)   # 4 second sleep between moves, can be adjusted as needed
        else:
            f.write("Attempted conversion from " + row[0] + " ----> " + row[1] + " -----, but something went wrong.\n")
            print("Something went wrong")

        #rows.append(row)
        #listing.append(row[0])
        #f.write(row[0] + "\n")
        #listing2.append(row[1])
#f2.write(row[1] + "\n")
f.close()
f2.close()

site = mwclient.Site(('https','en.wikipedia.org'), '/w/')
#login stuff
