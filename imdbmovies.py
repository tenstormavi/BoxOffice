from bs4 import BeautifulSoup
import urllib2
import requests

url = "http://www.imdb.com/chart/?ref_=nv_ch_cht_2"
contents = urllib2.urlopen(url).read()
soup = BeautifulSoup(contents)
soup.prettify()

movies = soup.findAll('td', {'class': 'titleColumn'})
count = len(movies)
print "There are Currently %s Movies in IMDB's Boxoffice" % count

num = raw_input("How many movies you want to know about from top?: ")
for i in range(0,int(num)):
	link = movies[i].find('a').get('href')
	linkcontents = urllib2.urlopen("http://www.imdb.com/" + link).read()
	soup = BeautifulSoup(linkcontents)
	soup.prettify()
	castsection = soup.findAll('div',{'itemprop':'actors'})
	title = movies[i].find('a').text
	print "\nMovie Name: %s" % title
	print "Cast:"
	x = 0
	castname = castsection[x].findAll('a')
	for y in range(0,3):
		print castname[y].text
