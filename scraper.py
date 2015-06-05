from selenium import webdriver
from bs4 import BeautifulSoup
import bs4



def scrape( link ):

	scraped_data = {}

	# link begins with htt..
	if(link[0] == 'h'):

		# GET HTML
		# Now using selenium
		browser = webdriver.Firefox()
		browser.get(link)

		# HTML PROCESSOR
		f = open('test.txt','w')
		soup = bs4.BeautifulSoup(browser.page_source.encode('utf-8'))

		browser.close()

		with open("comment_log.txt", "a") as comment_log:

			header = getHeader(soup)
			comments = getComments(soup)
			if( comments != ""):
				comment_log.write("\n\n" +header +comments)




def getHeader(soup):
	return "TEST"

def getComments(soup):
	comments = soup.select('p.comment_content')
	comment_string =""

	if( comments != []):
		for comment in comments:
			comment_string = comment_string + "\n" + comment.getText()

	return comment_string

