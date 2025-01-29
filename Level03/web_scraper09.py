#!/usr/bin/python3
"""
    A Script that Scrapes A Website
"""

from prettytable import PrettyTable
import requests
from bs4 import BeautifulSoup

def scrape(url):
    """ 
        Web Sraper
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTP errors if any
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data safely
        title = soup.select_one('h1')
        text = soup.select_one('p')
        link = soup.select_one('a')

        
        table = PrettyTable(["Field", "Value"])
        table.align["Field"] = "l"
        table.align["Value"] = "l"
        table.add_row(["Title", title.text if title else "No title found"])
        table.add_row(["Text", text.text if text else "No paragraph found"])
        table.add_row(["First Link", link.get('href') if link else "No link found"])

        print(table)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == '__main__':
    url = input("Enter a website URL: ").strip()
    scrape(url)
