# mapmyrun_webscraper
NOTE: This webscraper only adds functionality to the premium membership. It in no way extracts data in order to avoid having to pay. Could be a feature though!

## Install
	- Clone Repo
	- Make sure you have python installed (My machine is Ubuntu 14.04 with Default python2.7)
	- Install requests plugin (link-needed) and Beautiful Soup 4 (link-needed)
	- Export your .csv file from mapmyrun and move it into the mapmyrun_webscraper folder
	- Run main.py

The output will be result in a formatted text file as shown below:

''
	May 28, 2015 | 6.8mi | 08:10 | 55:36
	1st run back
	testing web scraper
	double test
''

## Features Coming
	As I continue my running I plan on adding the following features

	- No need for .csv urls, only account log-in and access to 'my workouts' page
	- Option to set up automatic syncing with crontab 
	- Option to save in the original.csv file in a new column
	- ... syncing all data?

This project is licensed under the terms of the MIT license