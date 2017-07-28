# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 14:10:04 2017

@author: abhishek
"""

import urllib2
import BeautifulSoup
import sys

def login(user,pwd):
 loginReq=urllib2.Request("https://www.facebook.com/login.php?m=m&amp;refsrc=http%3A%2F%2Fm.facebook.com%2Findex.php&amp;refid=8","email=%s&pass=%s&login=Login"%(user,pwd))
 logconn=urllib2.urlopen(loginReq)
 data=BeautifulSoup.BeautifulSoup(logconn)
# print data
 if "Log In" in data.head.title.string:
  return False
 else :
  return data


def main(arg):
    if arg<3:
        sys.exit("Please specify username and password");
    
    user = arg[1]
    pwd = arg[2]
    data = login(user, pwd)
    
    if not data==False:
        pokes = urllib2.urlopen("http://m.facebook.com/pokes")
        pokeData = BeautifulSoup.BeautifulSoup(pokes)
        
        for a in pokeLink:
            url=a["href"];
            print url;
#        links = data.findAll('a');
#        for a in links:
#            url=a['href']
#            if "/a/notifications.php?poke" in url:
#                print "Found Poke : " + url + "\n";
#            else:
#                print "Poke Not Found " + url + "\n"


if __name__ == "__main__":
    main(sys.argv)