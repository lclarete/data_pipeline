import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup as bs

# download data from the website
def download_page(url, method_bs=True):
    res = requests.get(url)
#     if method_bs == True:
#         return bs(res.text, 'html.parser')
    return res.content

def download_pages(list_url, method_bs=True):
    data = []
    for link in links:
        data.append(download_page(link, method_bs=True))
    return data