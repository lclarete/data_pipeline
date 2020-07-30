from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import selenium.webdriver
import time
from bs4 import BeautifulSoup


# GLOBAL VARIABLES DRIVER
chrome_location = '/Users/liviaclarete/coding/scrap_page/chromedriver'

# GLOBAL VARIABLES YOUTUBE SEARCH
search_xpath = '//*[(@id = "search")]'
term = 'asma'
url = 'https://www.youtube.com/'
# only videos with asma
url = 'https://www.youtube.com/results?search_query=asma+%2B+doença%2A+OR+saúde+OR+crise%2A+OR+sintoma%2A+OR+morte%2A+OR+morre%2A+OR+trata%2A+OR+ter+OR+cuida%2A+OR+adulto%2A+OR+criança%2A+OR+bronquite%2A+OR+simpatia%2A+OR+hospital+OR+diagnost%2A+OR+benz%2A&sp=CAI%253D'

# # GLOBAL VARIABLE FACEBOOK LOGIN
# # username = 'livia.clarete@gmail.com'
# # password = 'liviapistico20!!!'
# # url = "https://mbasic.facebook.com"
# # url = 'https://www.facebook.com/'

# Setting chrome drive
driver = selenium.webdriver.Chrome(chrome_location)
driver.get(url)
time.sleep(1)


# search a term within the youtube search bar
sleep = 3
search = driver.find_element_by_xpath(search_xpath)
time.sleep(sleep)
search.send_keys(term, Keys.RETURN)
time.sleep(sleep)


# Scrolling YouTube page
tag = 'html'
n = 0
n_iterations = 5
sleep = 4

try:
    while n < n_iterations:
        html = driver.find_element_by_tag_name(tag)
        html.send_keys(Keys.END)
        time.sleep(sleep)
        print(n)
        n += 1
    # Saving data into a BS object
    content = driver.page_source
    file_ = open('page2.html', 'w')
    file_.write(content)
    file_.close()

    soup = BeautifulSoup(content, 'lxml')
    driver.close()
    # with open('soup_youtube.html', 'w') as file:
    #     file.write(str(content))        
except:
    driver.close()


# user_data = driver.find_element_by_xpath('//*[@id="video-title"]').text
# title = driver.find_element_by_id('video-title').text
# print(title)

# import re
# dynamic_info = soup.find_all('div',id = re.compile('items'))
# rows = dynamic_info[1].find_all('ytd-compact-video-renderer')

# TITLES = []
# CHANNELS = []
# DURATIONS = []
# VIEWS = []

# count = 0

# for row in rows:
#     count += 1
#     title_column = row.find('span',{'id':'video-title'})
#     title_column = title_column.text
#     channels_column = row.find('yt-formatted-string',{'id':'byline'})
#     channel_name = channels_column.text
#     duration_column = row.find('div',{'class':'ytd-thumbnail'})
#     duration_value = duration_column.text
#     views_column = row.find('span',{'class':'ytd-video-meta-block'})
#     views_number = views_column.text
#     duration = duration_value.split('\n')[1].split('\n')[-1].strip()
#     title = title_column.split('\n')[1].split('\n')[-1].strip()
#     TITLES.append(title)
#     CHANNELS.append(channel_name)
#     DURATIONS.append(duration)
#     VIEWS.append(views_number)
# print(count)

id_of_video = 'CUNq2_VjRn4'
your_api_key = 'AIzaSyBKhbu3j5izgiPqBALUedXHtSqeGrPXM9o'
 
url = f'https://www.googleapis.com/youtube/v3/videos?id={id_of_video}&key={your_api_key}&part=status'
print(url)


# driver.close()


# # Extract info from html
# from scrapy import Selector

# sel = Selector(text=content, type='lxml')
# desc = sel.css('.description-text').extract()

# print(desc)

# def extract_text(list_xpath, page=soup):
#     sel = Selector(text=page, type='lxml')
#     xpath_values = [sel.xpath(val).extract() for val in list_xpath]
#     xpath_values_flat = [x for k in xpath_values for x in k]
#     return(xpath_values_flat)

# # Setting xpath to build a dataframe
# xpath_title = '//*[(@id = "video-title")]'
# xpath_viz = xpath_title#[]
# xpath_likes = xpath_title#[]
# xpath_link = xpath_title#[]
# xpath_desc = xpath_title#[]

# xpath_values = [xpath_title, xpath_viz, xpath_likes, xpath_link, xpath_desc]

# # Extract data
# youtube_data = extract_text(xpath_values)

# columns = ['title', 'n_viz', 'n_likes', 'link', 'desc']
# import pandas as pd
# df_youtube = pd.DataFrame(youtube_data, columns=columns)
# df_youtube.to_csv('youtube_posts.csv')


# # FACEBOOK LOGIN
# driver.find_element_by_name('email').send_keys(username)
# driver.find_element_by_name('pass').send_keys(password)
# time.sleep(2)
# driver.find_element_by_name('login').click()

# # Login in one tap -- Still passing facebook security
# time.sleep(2)
# driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "bl", " " ))]').click()

# time.sleep(2)
# driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "bj", " " ))]').click()


