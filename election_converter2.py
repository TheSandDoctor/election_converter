#!/usr/bin/env python3.6
import configparser
import json
import mwclient
import re
import sys
from mwclient import errors


def call_home(site_obj):
    """
    Check if still allowed to edit ("election_converter") not set to "false" in https://enwp.org/User:TheSandBot/status
    :param site_obj: mwclient site object
    :return: Whether or not can edit
    """
    h_page = site_obj.Pages['User:TheSandBot/status']
    page_text = h_page.text()
    return bool(json.loads(page_text)['run']['election_converter'])


def move_page(old_title: str, new_title: str) -> bool:
    """
    Move a page from old_title to new_title
    :param old_title: Old title to move page from
    :param new_title: New title to move page to
    :return: Whether move was successful
    """
    page = site.Pages[old_title]
    edit_summary = """Moving page per result of [[Special:Diff/869750233|RfC on election/referendum page naming 
    format]] using [[User:""" + config.get(
        'enwiki_sandbot', 'username') + "| " + config.get('enwiki_sandbot',
                                                          'username') + """]]. Questions? See [[
                                                          Special:Diff/869750233|the RfC]] or [[User 
                                                          talk:TheSandDoctor|msg TSD!]] ([[Wikipedia:Bots/Requests 
                                                          for approval/TheSandBot|BRFA]]; please mention that this is 
                                                          task #1!)) """

    if page.exists and not site.Pages[new_title].exists and page.redirects_to() is None:
        return page.move(new_title, reason=edit_summary, move_talk=True, no_redirect=False)
    return False


if __name__ == "__main__":
    try:
        site = mwclient.Site(('https', 'en.wikipedia.org'), '/w/')
        # Login stuff
        config = configparser.RawConfigParser()
        config.read('credentials.txt')
        try:
            site.login(config.get('enwiki_sandbot', 'username'), config.get('enwiki_sandbot', 'password'))
        except errors.LoginError as e:
            print(e)
            raise ValueError('Login failed.')
        # End login stuff
        source_page = site.Pages['User:Number 57/Elections/By-elections']
        text = source_page.text()
        match = re.findall(r"\*\[\[(.*)\]\] to \[\[(.*)\]\]", text)
        counter = 0
        fh = open('election_converter_results_by-elections.txt', "w")
        for mat in match:
            if counter < 113:
                counter += 113
                continue
            if not call_home(site):  # config):
                raise ValueError('Kill switch on-wiki is false. Terminating program.')
            elif move_page(mat[0], mat[1]):
                fh.write('Converted ' + mat[0] + ' ----> ' + mat[1] + "\n")
                print('Converted ' + mat[0] + ' ----> ' + mat[1] + "\n")
                counter += 1
            else:
                fh.write('CONVERSION FAILED ' + mat[0] + ' to ' + mat[1])
                print('CONVERSION FAILED ' + mat[0] + ' to ' + mat[1])
        print('DONE')
        fh.close()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
