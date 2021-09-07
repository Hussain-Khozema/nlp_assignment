import requests
from bs4 import BeautifulSoup
import os
import re
import config

def scrape_web(domain):
    urls = config.getURLsSuffix(domain)
    for url in urls:
        resp = requests.get(url)
        element_soup = BeautifulSoup(resp.text, 'html.parser')
        file_name = url.replace(config.DOMAIN_URL_PREFIXES[domain],"")
        file_url = config.FOLDERS["DOMAIN_FOLDER_NAME"] + domain + config.FOLDERS["DATA_FOLDER"] + file_name
        print("Scraping from " + url + ".........")
        with open (file_url, 'w',encoding="utf-8") as f:
            for p in element_soup.find_all('p'):
                filt_text = re.sub(r'[\[].*?[\]]', '', p.text)
                f.write(filt_text.strip() + " ")
            f.close()
            print("Content saved to " + file_url)
        print("\n")

    print("Scraping completed for " + str(len(urls)) + " websites in " + domain)
