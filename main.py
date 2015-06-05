import csv,scraper
with open('Alexs_workout_history.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		scraper.scrape(row[14])
		