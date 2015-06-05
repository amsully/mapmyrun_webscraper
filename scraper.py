from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# import requests
from bs4 import BeautifulSoup
import bs4
# import time
def hi():
	print('hi')


def scrape( link):

	scraped_data = {}

	# link begins with htt..
	if(link[0] == 'h'):

		# Now using selenium
		browser = webdriver.Firefox()
		browser.get(link)


		f = open('test.txt','w')
		soup = bs4.BeautifulSoup(browser.page_source.encode('utf-8'))

		comment = soup.select('p.comment_content')[0].getText()

		if(comment != None):
			f.write(comment)

		browser.close()
