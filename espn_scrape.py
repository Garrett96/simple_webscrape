import csv
import requests
from bs4 import BeautifulSoup

url = 'https://www.espn.com/nfl/schedule'

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for any HTTP errors
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.select('.Table__TBODY tr')

    with open('nfl_schedule.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in rows:
            content = row.get_text(strip=True)
            writer.writerow([content])

    print("CSV file created successfully.")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
