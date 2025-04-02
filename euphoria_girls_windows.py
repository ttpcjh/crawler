import winsound

import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime

'''
crawler script for euphoriagirls by ttpcjh.
'''

def crawl():
    today = datetime.today()
    today_formatted_date = today.strftime("%A, %B %d.")
    while True:
        url = "https://www.euphoriagirls.com/"

        # Send a GET request to the webpage
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the page content with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the span tag with specific class and style
            span_tag = soup.find('span', class_='wixui-rich-text__text', style='font-family:snellroundhandw01-scrip,cursive; font-size:83px; letter-spacing:0em;')

            if span_tag:
                print(datetime.now())
                print("Text in span tag:", span_tag.text)
                if span_tag.text != today_formatted_date:
                    winsound.Beep(500,100)
            else:
                print("No matching span tag found")
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        time.sleep(5)


if __name__ == '__main__':
    crawl()