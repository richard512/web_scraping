#Christopher Reeves Web Scraping Tutorial
#getting page source with python
#http://youtube.com/creeveshft
#http://christopherreevesofficial.com
#http://twitter.com/cjreeves2011

import urllib
import mechanize
from bs4 import BeautifulSoup
from urlparse import urlparse
import hashlib
import os
import imghdr
import shutil

filenum = 0

def searchPic(term):
    img_list = getPic(term)
    print img_list
    if len(img_list)>0:
        for img in img_list:
            savePic(img)
    print "done"

def getPic (search):
    search = search.replace(" ","%20")
    try:
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        browser.addheaders = [('User-agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; cs; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8')]

        htmltext = browser.open("https://www.google.com/search?site=imghp&tbm=isch&source=hp&biw=1414&bih=709&q="+search+"&oq="+search)
        img_urls = []
        formatted_images = []
        soup = BeautifulSoup(htmltext, "html.parser")
        results = soup.findAll("img")
        print results
        for r in results:
            try:
                if "Image result for" in r['alt']:
                    img_urls.append(r['src'])
            except:
                a=0
        for im in img_urls:
            image_f = im
            #refer_url = urlparse(str(im))
            #image_f = refer_url.query.split("&")[0].replace("imgurl=","")
            formatted_images.append(image_f)
        
        return  formatted_images

    except:
        return []

def savePic(url):
    global filenum
    filenum += 1
    directory = "results/"
    if not os.path.exists(directory):
        shutil.rmtree(directory)
    if not os.path.exists(directory):
        os.makedirs(directory)
    dest = directory + str(filenum)
    print url
    try:
        f = urllib.urlopen(url)
        with open(dest, "wb") as imgFile:
            imgFile.write(f.read())
        ext = imghdr.what(dest)
        newdest = dest + "." + ext
        os.rename(dest, newdest)
    except:
        print "save failed"

query = raw_input("Goole Image Search Query: ")
searchPic(query)
