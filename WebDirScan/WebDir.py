# -*- coding: utf-8 -*-
#目录枚举


import urllib2
import threading
import Queue
import urllib
import optparse
import conf as cf


flag = None
threads = 50
target_url = "http://127.0.0.1"
wordlist = "PHP.txt"
user_agent = "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; \
AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"


def read_wordlist(wordlist):
    f = open(wordlist,"rb" )
    words = f.readlines()
    f.close()
    found_flag = False
    words = Queue.Queue()
    for word in words: 
        word = word.rstip()
        if flag is not None:
            if found_flag:
                words.put(word)
            else:
                if word == flag:
                    found_flag = True
                    print 'wordlist from: %s' % word
        else:
            words.put(word)
    return words
        
def webdir(word, extensions = None):
    while not word.empty():
        temp = word.get()
        temp_list = []
        if "." not in temp:
            temp_list.append("/%s/" % temp)
        else:
            temp_list.append("/%s/" % temp)
        if extensions:
            for extension in extensions:
                temp_list.append("/%s%s" %(temp, extension))
        
        for dirs in temp_list:
            url = "%s%s" % (target_url, urllib.quote(dirs))
            
            try:
                headers = {}
                headers["User-Agent"] = user_agent
                r = urllib2.Request(url, headers = headers)
                response = urllib2.urlopen(r)
                if len(response.read()):
                    print "[%d] => %s" %(response.code, url)
            except urllib2.URLError, e:
                if hasattr(e, 'code') and e.code != 404:
                    print "!!!! %d => %s" % (e.code, url)
                pass

"""
    第一种方法
    w = []
    for word in words:
        word = word.rstrip()
        w.append(word)
    return w

def main():
   
    global flag
    global threads 
    global target_url
    global wordlist
    global user_agen
    
    #提交参数
    parser = optparse.OptionParser(usage=" WebDirScan version v1.0" )
    parser.add_option('-t', '--target_url', action="store_false", default=True,dest='target_url', help='Add target URL')
    parser.add_option('-T', '--threads'   , action="store_false", default=True,dest='threads'   , help='Add thread, you can not fill, the default is 50 threads')
    parser.add_option('-w', '--wordlist'  , action="store_false", default=True,dest='wordlist'  , help='Add your burst dictionary')
    parser.add_option('-u', '--user_agnet', action="store_false", default=True,dest='target_url', help='Add your user_agent. Only one default can add more of your configuration in the configuration file,')
    (options,args)= parser.parse_args()
  
    threads            = options.threads #可选项
    target_url         = options.target_url 
    wordlist           = options.wordlist
    options.user_agent = cf.USER_AGENT
    user_agent         = options.user_agent #可选项
    word               = read_wordlist(wordlist)
    """
word = read_wordlist(wordlist)
    #扩展名可以随意添加扩展
extensions = [ ".bak", ".html", ".inc", ".asp" , ".asa"]
    
for i in range(threads):
    t = threading.Thread(target = webdir, args = (word, extensions,))
    t.start()
        
"""
if __name__ == '__main__':
    main()

"""  
    
    
    

    
    
    
