"""
Scrape data from YouTube
"""

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import selenium.webdriver
import time
from bs4 import BeautifulSoup
from scrapy import Selector
import pandas as pd

# # Search a term at the youtube search bar
# search_xpath = '//*[(@id = "search")]'
# search = driver.find_element_by_xpath(search_xpath)
# time.sleep(sleep)
# search.send_keys(term, Keys.RETURN)
# time.sleep(sleep)
# url = 'https://www.youtube.com/'

# Scrape a specific search url
url = 'https://www.youtube.com/results?search_query=asma+%2B+doença%2A+OR+saúde+OR+crise%2A+OR+sintoma%2A+OR+morte%2A+OR+morre%2A+OR+trata%2A+OR+ter+OR+cuida%2A+OR+adulto%2A+OR+criança%2A+OR+bronquite%2A+OR+simpatia%2A+OR+hospital+OR+diagnost%2A+OR+benz%2A&sp=CAI%253D'

# Setting chrome drive
chrome_location = '/Users/liviaclarete/coding/scrap_page/chromedriver'
driver = selenium.webdriver.Chrome(chrome_location)
driver.get(url)
time.sleep(1)

# Scrolling YouTube page
tag = 'html'
n = 0
n_iterations = 10
sleep = 4

try:
    while n < n_iterations:
        html = driver.find_element_by_tag_name(tag)
        time.sleep(sleep)
        html.send_keys(Keys.END)
        time.sleep(sleep)
        html.send_keys(Keys.HOME)
        print(f'scrolling {n}')
        n += 1
    # Saving data into a BS object
    content = driver.page_source
    file_ = open('page2.html', 'w')
    file_.write(content)
    file_.close()
    response = Selector(text=driver.page_source.encode('utf-8'))
    soup = BeautifulSoup(content, 'lxml')
    driver.close()
    # with open('soup_youtube.html', 'w') as file:
    #     file.write(str(content))        
except:
    driver.close()


def parse_xpath(xpath_expression, text=True):
    if text==True:
        xpath_expression = xpath_expression +'//text()'
    else:
        xpath_expression = xpath_expression + '/@href'
        
    data = response.xpath(xpath_expression).extract()
    data_list = []
    for i in data:
        data_list.append(i.strip())
    return(data_list)

# Extract info from html using xpath
title_xpath = '//*[(@id = "video-title")]'
title = parse_xpath(title_xpath)
link = parse_xpath(title_xpath, text=False)

link = ['https://www.youtube.com'+i for i in link]

id_video = [i.split('=')[1] for i in link]

