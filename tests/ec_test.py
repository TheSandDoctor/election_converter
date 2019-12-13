#!/usr/bin/env python3.6
import time,mwclient,csv, json, configparser
from time import sleep

def call_home(site):
    #page = site.Pages['User:' + config.get('enwiki','username') + "/status"]
    page = site.Pages['User:TheSandBot/status']
    text = page.text()
    data = json.loads(text)["run"]["election_converter"]
    if data:
        return True
    return False
def move_page(old_title,new_title):
    page = site.Pages[old_title]
    #edit_summary = """Moving page per result of [[Special:Diff/864130819|RfC on election/referendum page naming format]] using [[User:""" + config.get('enwikitsb','username') + "| " + config.get('enwikitsb','username') + """]]. Questions? See [[Special:Diff/864130819|the RfC]] or [[User talk:TheSandDoctor|msg TSD!]] (please mention that this is task #1!))"""
    edit_summary = "DEBUG: Move back; Quick userspace test, in compliance with [[WP:BOTUSERSPACE]]."
    if page.exists and page.redirects_to() == None:
        return page.move(new_title,reason=edit_summary,move_talk=True, no_redirect=True)
    return None


#rows.append(row)
#listing.append(row[0])
#f.write(row[0] + "\n")
#listing2.append(row[1])
#f2.write(row[1] + "\n")
#f.close()
#f2.close()

site = mwclient.Site(('https','en.wikipedia.org'), '/w/')
#login stuff
config = configparser.RawConfigParser()
config.read('credentials.txt')
try:
    site.login(config.get('enwiki_sandbot','username'), config.get('enwiki_sandbot', 'password'))
except errors.LoginError as e:
        #print(e[1]['reason'])
    print(e)
    raise ValueError("Login failed.")
row = ["User:TheSandBot/sandbox2","User:TheSandBot/sandbox"]
if move_page(row[0],row[1]):
    print("Converted " + row[0] + " ----> " + row[1] + "\n")
else:
    print("Something went wrong")
