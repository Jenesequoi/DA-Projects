#Import the libraries necessary for scrapper

from bs4 import BeautifulSoup
import requests
import csv

#Create url variable to scrape
url= 'https://en.wikipedia.org/wiki/List_of_African_countries_by_area'
page= requests.get(url).text

#Save result in a variable (soup)
soup= BeautifulSoup(page, 'html5lib')

print(soup.prettify())  #arrange it in indented format

csv_file= open('scrapy.csv', 'w', newline='', encoding='utf8') #save the file scrapped in csv format

#Write csv file and label columns
csv_writer= csv.writer(csv_file)
csv_writer.writerow(['name', 'total_%', 'area in km'])

#Find the data you want to scrape
country_table= soup.find('table', {'class': 'wikitable'})
rows= country_table.find_all('tr')[1:]

#Iterate to populate csv file
for row in rows:
    columns= row.find_all(['th', 'td'])
    # index= columns[0].text.strip()
    name= columns[1].text.strip()
    total_area_percentage= columns[2].text.strip()
    area_km= columns[3].text.strip()
    
    csv_writer.writerow([name, total_area_percentage, area_km])
#Close csv
csv_file.close()

