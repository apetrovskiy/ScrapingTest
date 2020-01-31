from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
#from urllib.error import AttributeError
from bs4 import BeautifulSoup

try:
    print("============== html.parser ==============")
    html = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
    print(e)
except URLError as e:
    print(e)
else:
    #print(html.read())
    bs = BeautifulSoup(html.read(), 'html.parser')
    try:
        print(bs.html.body.h1)
    except AttributeError as e:
        print(e)
    else:
        print(bs.h1)
        print(bs.html.body.h1)
        print(bs.body.h1)
        print(bs.html.h1)

try:
    print("============== lxml ==============")
    html = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
else:
    bs2 = BeautifulSoup(html.read(), 'lxml')
    try:
        print(bs2.html.body.h1)
    except AttributeError as e:
        print(e)
    else:
        print(bs2.h1)

try:
    print("============== html5lib ==============")
    html = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
else:
    bs3 = BeautifulSoup(html.read(), 'html5lib')
    try:
        print(bs3.html.body.h1)
    except AttributeError as e:
        print(e)
    else:
        print(bs3.h1)

'''
bs.findAll('table')[4].find_all('tr')[2].find('td').find_all('div')[1].find('a')
bs2.findAll('table')[4].find_all('tr')[2].find('td').find_all('div')[1].find('a')
bs3.findAll('table')[4].find_all('tr')[2].find('td').find_all('div')[1].find('a')
'''
