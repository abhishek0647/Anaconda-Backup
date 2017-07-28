# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 19:28:22 2017

@author: abhishek
"""

#!usr/bin/env/ python
# Python Script to automatically Poke people on facebook
# By Sebin Thomas
# USE AT YOUR OWN RISK
# It was written in a Hurry so no error handling whatsoever and there may be a zillion Bugs
# And it's not Safe 
# THOSE WHO USE THIS CODE ARE DOING SO IN THEIR OWN RISK AND THE AUTHOR 
# IS NOT ACCOUNTABLE FOR ANY DAMAGE WHATSOEVER
# Usage : poke.py Username password
import urllib2
from BeautifulSoup import BeautifulSoup
import sys
import requests
import time
import logging

try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
#http_client.HTTPConnection.debuglevel = 1


logging.basicConfig() 
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

Session = requests.Session()

def handle_login_response(r):
    print "Handle Response"
    print r.text
    if "Remember Browser" in r.text:
        remember_browser(r)
        return
    
    if "New! Log In Faster" in r.text:
        login_faster(r)
        return
    
    if "Review Recent Login" in r.text:
        review_login(r)
        return
    
    if "Enter Security Code to Continue" in r.text:
        two_step(r)
        return

def two_step(r):
    print "2 step Verify"
    sec_code = raw_input("Enter Security Code: ")
    soup = BeautifulSoup(r.text)
    url = "https://m.facebook.com" + soup.find('form').get('action')
    data = {
        'lsd': soup.find('input', {'name': 'lsd'}).get('value'),
        'charset_test': soup.find('input', {'name': 'charset_test'}).get('value'), 
        'codes_submitted': soup.find('input', {'name': 'codes_submitted'}).get('value'), 
        'nh': soup.find('input', {'name': 'nh'}).get('value'), 
        'submit[Submit Code]': 'Submit Code'
        
    }
    
    data["approvals_code"] = sec_code

    r = Session.post(url, data=data)
    r.raise_for_status()
    
    handle_login_response(r)

def login_faster(r):
    print "Login Faster"
    soup = BeautifulSoup(r.text)
    URL = "https://m.facebook.com/login/device-based/update-nonce/"
    
    data = {
        'fb_dtsg': soup.find('input', {'name': 'fb_dtsg'}).get('value'),
        'charset_test': soup.find('input', {'name': 'charset_test'}).get('value'), 
        'flow': soup.find('input', {'name': 'flow'}).get('value'), 
        'next': ''
        
    }
    
    r = Session.post(url, data=data)
    r.raise_for_status()
    
    handle_login_response(r)
    
def review_login(r):
    print "Review Login"
    soup = BeautifulSoup(r.text)
    URL = "https://www.facebook.com/checkpoint/"
    
    data = {
        'lsd': soup.find('input', {'name': 'lsd'}).get('value'),
        'charset_test': soup.find('input', {'name': 'charset_test'}).get('value'), 
        'nh': soup.find('input', {'name': 'nh'}).get('value'), 
        'submit[Continue]': 'Continue'
        
    }
    
    r = Session.post(url, data=data)
    r.raise_for_status()
    
    data = {
        'lsd': soup.find('input', {'name': 'lsd'}).get('value'),
        'charset_test': soup.find('input', {'name': 'charset_test'}).get('value'), 
        'nh': soup.find('input', {'name': 'nh'}).get('value'), 
        'submit[This is Okay]': 'This is Okay'
        
    }
    
    r = Session.post(url, data=data)
    r.raise_for_status()
    
    handle_login_response(r)
    
def remember_browser(r):
    print "Remember Browser"
    soup = BeautifulSoup(r.text)
    url = "https://m.facebook.com/login/checkpoint/"
    data = {
        'lsd': soup.find('input', {'name': 'lsd'}).get('value'),
        'charset_test': soup.find('input', {'name': 'charset_test'}).get('value'), 
        'name_action_selected': "save_device",
        'nh': soup.find('input', {'name': 'nh'}).get('value'), 
        'submit[Continue]': 'Continue'
        
    }
    
    r = Session.post(url, data=data)
    r.raise_for_status()
    
    handle_login_response(r) 

def login(user,pwd):
    print "Login"
    r = requests.get('https://m.facebook.com/')
    soup = BeautifulSoup(r.text)
    data = {
        'lsd': soup.find('input', {'name': 'lsd'}).get('value'),
#        'charset_test': soup.find('input', {'name': 'charset_test'}).get('value'), 
        'version': soup.find('input', {'name': 'version'}).get('value'),
        'ajax': soup.find('input', {'id': 'ajax'}).get('value'),
        'width': soup.find('input', {'id': 'width'}).get('value'),
        'pxr': soup.find('input', {'id': 'pxr'}).get('value'),
        'gps': soup.find('input', {'id': 'gps'}).get('value'),
        'dimensions': soup.find('input', {'id': 'dimensions'}).get('value'),
        'li': soup.find('input', {'name': 'li'}).get('value'),
        'm_ts': soup.find('input', {'name': 'm_ts'}).get('value'),
    }
    data["email"] = user
    data["pass"] = pwd
    
    url = soup.find('form').get('action')    
    r = Session.post(url, data=data)
    
    r.raise_for_status()
    
    handle_login_response(r)

def has_kait_poked_me():
    print "Has Shama Poked me?"
    search = "Shama Singh"
    URL = "https://m.facebook.com/pokes/"
    r = Session.get(URL)
    r.raise_for_status()
    
    print r.text
    
    if search in r.text:
        return True

def poke_back():
    print "Poke People Back"
    
    URL = "https://m.facebook.com/pokes/"
    r = Session.get(URL)
    r.raise_for_status()
    
    soup = BeautifulSoup(r.text)
#    print soup
    poke_area = soup.find("div", {"id":"poke_area"})

    for el in poke_area:
        if "poked you" in el.text and "Shama Singh" in el.text:
            poke_url = el.find("a", {"class":"bz y z bb"}).get("href")
            print "poke"
            print poke_url
            URL = "https://m.facebook.com" + poke_url
            r = Session.get(URL)
            r.raise_for_status()

def main(arg):
 user="Nice"
 pwd="Try"
 login(user,pwd)
 while 1:
     poke_back()
     time.sleep(5)

 

if __name__=="__main__":
 main(sys.argv)