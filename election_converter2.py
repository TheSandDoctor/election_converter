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
    edit_summary = """Moving page per result of [[Special:Diff/869750233|RfC on election/referendum page naming format]] using [[User:""" + config.get('enwikitsb','username') + "| " + config.get('enwikitsb','username') + """]]. Questions? See [[Special:Diff/869750233|the RfC]] or [[User talk:TheSandDoctor|msg TSD!]] (please mention that this is task #1!))"""
    if page.exists and page.redirects_to() == None:
        return page.move(new_title,reason=edit_summary,move_talk=True, no_redirect=False)
    return None


site = mwclient.Site(('https','en.wikipedia.org'), '/w/')
#login stuff
page = site.Pages['User:Number 57/Elections/Propositions']
text = page.text()
match = re.findall(r"\*\[\[(.*)\]\] to \[\[(.*)\]\]",text)
for mat in match:
    if not call_home(site):#config):
        raise ValueError("Kill switch on-wiki is false. Terminating program.")
    elif move_page(mat[0],mat[1]):
        fh.write("Converted " + mat[0] + " ----> " + mat[1] + "\n")
    else:
        fh.write("CONVERTION FAILED " + mat[0] to mat[1])
f.close()
