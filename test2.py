#!/usr/bin/env python3.6
import time,mwclient,re
def getTransclusions(site,page,sleep_duration = None,extra=""):
    cont = None;
    pages = []
    i = 1
    while(1):
        result = site.api('query',list='embeddedin',eititle=str(page),eicontinue=cont,eilimit=500,format='json')
        #print("got here")
        if sleep_duration is (not None):
            time.sleep(sleep_duration)
        #res2 = result['query']['embeddedin']
        for res in result['query']['embeddedin']:
            #print('append')
            pages.append(res['title'])
            i +=1
        try:
            cont = result['continue']['eicontinue']
        #print("cont")
        except NameError:
            print("Namerror")
            return [pages,i]
        except Exception as e:
            print("Other exception" + str(e))
            #    print(pages)
            return [pages,i]
site = mwclient.Site(('https','en.wikipedia.org'), '/w/')
f = open('./before.txt','a+')
result = getTransclusions(site,"Template:Infobox election")
print(result[0])
for n in result[0]:
    #print(n + "\n")
    f.write(n + "\n")
f.close()
def process(page):
    # The "easy" case
    reg1 = re.search(r"[election]+, (\d\d\d\d)$",page.page_title)
    if reg1:
        old_title = str(page.page_title)[:]
        new_title = reg1.group(1) + " " + old_title[:-6]
        print(new_title)
        f.write(new_title + "\n")
        #page.move("new_title", move_talk=True, no_redirect=False)
        return
    # Messier, but appears to do an adequate job
    reg2 = re.search(r"[election]+, (.*)",page.page_title)
    if reg2:
        old_title = str(page.page_title)[:]
        pos = old_title.index("election,") + 10
        new_title = old_title[pos:] + " " + old_title[:pos-2]
        print(new_title)
        f.write(new_title + "\n")
        return

#getTransclusions(site,"Template:GA Nominee") + "\n"
f = open('./after.txt','a+')
for page in result[0]:
    process(site.Pages[page])
f.close()
