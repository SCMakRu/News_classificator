import os, sys
import webbrowser
import httplib
import httplib2
from urlparse import urlparse
import requests
import unirest
import re
import MySQLdb
import urllib2
import BeautifulSoup
sys.path.append("/home/slobodanka/Desktop/master/big_data/")
from News_Classificator import DBConfig_NewsClassif
db_config = DBConfig_NewsClassif.DBConfig()

#sql="DELETE FROM articles.urls LIMIT 82"
#db_config.commit(query=sql)

#lst_words = ['firefox', 'tablet-computer', 'smartphones', 'laptops','android', 'gadgets', 'television', 'internet', 'google', 'web-browsers','data-computer-security']
#for i in lst_words:
word = "sports"
request = urllib2.Request("https://www.theguardian.com/technology/"+str(word))

response = urllib2.urlopen(request)
soup = BeautifulSoup.BeautifulSoup(response)
id_n =3
url_lst = []

for a in soup.findAll('a'):    
    try:
        if a['href']:            
            if 'http://www' in a['href'] and  'page' not in a['href']:# and '2016' in a['href']:# and 'all' not in a['href'] and 'video' not in a['href']:
                if str(word) in a['href']:  
                    
                    if a['href'] not in url_lst:
                        url_lst.append(a['href'])
                        desc = str(str(a['href']).split("/")[-1]).split(".")[0]
                        
                        sql="INSERT INTO articles.urls VALUES ('%s', '%s', '%s', '%s')" % ('', a['href'], desc, "sports")
                        #db_config.commit(query=sql)                
                        print a['href'], desc
    except:
        print "Exception"

#month = 11
#day = 14
#regex_title = re.compile(r'.*')
#print type(regex_title)

#link_sport = "http://edition.cnn.com/2016/"+str(month)+"/"+str(day)+"/sport/"+regex_title
#print 'link_sport', link_sport
#print 'regex_title', regex_title
##/2016/11/11/sport/nina-carberry-pregnant-ends-season-jump-jockey-horse-racing/index.html"
#request = requests.get(link_sport)

#if request.status_code == 200:
    #print('Web site exists')
#else:
    #print('Web site does not exist') 

#for i in range(1,12):
    #for j in range(1,30):
        #month = i
        #day = j
        ##link_sport = "http://edition.cnn.com/2016/"+str(month)+"/"+str(day)+"/sport/"+(r'.*')
        ##http://www.fontanka.ru/2016/11/13/001/
        #for k in range(0,100):
            #link_sport = "http://www.fontanka.ru/2016/"+"{0:002d}".format(int(month))+"/"+"{0:002d}".format(int(day))+"/"+ "{0:003d}".format(int(k))
            #print 'link_sport', link_sport
            ##/2016/11/11/sport/nina-carberry-pregnant-ends-season-jump-jockey-horse-racing/index.html"
            #request = requests.get(link_sport)
            #print 'request.status_code',request.status_code
            #if request.status_code == 200:
                #print('Web site exists')
            #else:
                #print('Web site does not exist') 
            

def checkURL(url):
    p = urlparse(url)
    conn = httplib.HTTPConnection(p.netloc)
    conn.request('HEAD', p.path)
    resp = conn.getresponse()
    return resp.status < 400

if __name__ == '__main__':
    
    print checkURL('http://www.dailymail.co.uk/news/article-3947730/Adorable-moment-wild-polar-bear-pets-sled-dog-Manitoba-Canada.html')

#from alchemy
#
#import webhose
#webhose.config(token='539d3a58-1f32-4625-abb9-526a60d0e6cf')
#for post in webhose.search("github"):
    #print post.title
response = unirest.get("https://webhose.io/search?token=539d3a58-1f32-4625-abb9-526a60d0e6cf&format=json&q=tramp%20putin%20obama%20language%3A(english)",
    headers={
    "Accept": "text/plain"
    }
)
#print response.body
#webbrowser.open('http://inventwithpython.com/')



