# ex.1 simple web browser***********************************************************************************

 # import urllib.request, urllib.parse, urllib.error # imports urllib, 

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') # urlopen automatically opens socket and  encodes data
# for line in fhand: 
#    print(line.decode().strip()) # open url, read through and print

# ex. 2 ******************************************************************************************

# import urllib.request, urllib.parse, urllib.error # imports urllib, 

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# counts = dict()
#for line in fhand:
#    words = line.decode().split()
#    for word in words:
#        counts[word] = counts.get(word, 0) + 1
#    print(counts)

# ex. 3 Reading Web Pages

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())

# ex. 4 Parsing HTML(Web Scraping)
# When a program or script pretends to be a browser and retrieves webapes, looks at those web pages,
# extracts information, and then looks at more web pages
# Search engines scrape web pages - we call this "spidering the web" or "web crawling"
# USE software library call BEAUTIFUL SOUP ***************************
# download from http://www.py4e.com/code3/bs4.zip
# 
# below 2 lines are together

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
#
#
