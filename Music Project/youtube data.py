import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL to scrape data from
urls = ['https://kworb.net/youtube/topvideos2020.html',
       'https://kworb.net/youtube/topvideos2021.html',
       'https://kworb.net/youtube/topvideos2022.html',
       'https://kworb.net/youtube/topvideos2023.html'
       ]

# Function to scrape data from URL
def scrape_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract data from the HTML content as needed
        data = []
        for table in soup.find_all('table', {'class': 'addpos sortable'}):
             # Iterate through each row in the table
            for row in table.find_all('tr'):
                # Extract data from each cell in the row
                try:
                    cell_data = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
                    # Append the row data to the list of rows
                    data.append(cell_data)
                except Exception as e:
                    print(f"Error extracting data from row: {e}")
                    continue
        return data
    else:
        print("Failed to retrieve data from the URL.")
        return None

# Function to save data into multiple CSV sheets
def save_to_csv(data, filename):
    df = pd.DataFrame(data[1:], columns = data[0] )
    df.to_csv(filename, index=False)


# Loop through each URL, scrape data, and save it to a CSV file
for index, url in enumerate(urls):
    scraped_data = scrape_data(url)
    if scraped_data:
        filename = f'youtubedata_{index}.csv'  # Generate filename dynamically
        save_to_csv(scraped_data, filename)
        print(f"Data scraped from {url} and saved to {filename}")

