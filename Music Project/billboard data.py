import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv



def scrape_and_save(urls):
    # Make a request to the URL
    for index, url in enumerate (urls):
        response = requests.get(url)
    
    # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
        
            # Find the data you want to scrape
            data = []
            div = soup.find_all('li', class_='o-chart-results-list__item')

            for element in div:
                spans_item = element.find('span', class_='c-label')
                title_item = element.find('h3', class_='c-title')
            
                if spans_item and title_item:
                    spans = spans_item.text.strip()
                    title = title_item.text.strip()
                    data.append([spans, title])
                
            # Write the scraped data to a CSV file
            filename = f'billboards_{index}.csv'
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)      
                    
            # Write data into sheet
                for element in data:
                    writer.writerow(element)
            print(f"Scraping successful. Data from {url} saved to {filename}")
        else:
            print("Error: Unable to retrieve data from the URL")

if __name__ == "__main__":
    urls = [
        'https://www.billboard.com/charts/year-end/2020/hot-100-songs/',
        'https://www.billboard.com/charts/year-end/2021/hot-100-songs/',
        'https://www.billboard.com/charts/year-end/2022/hot-100-songs/',
        'https://www.billboard.com/charts/year-end/2023/hot-100-songs/'
    ]
    scrape_and_save(urls)

