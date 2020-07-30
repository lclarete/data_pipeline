import requests
from bs4 import BeautifulSoup
import pandas as pd

USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


def fetch_results(search_term, number_results, language_code):
    assert isinstance(search_term, str), 'camara vereadores'
    assert isinstance(number_results, int), '100'
    escaped_search_term = search_term.replace(' ', '+')

    google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results, language_code)
    response = requests.get(google_url, headers=USER_AGENT)
    response.raise_for_status()

    return search_term, response.text


def parse_results(html):
    soup = BeautifulSoup(html, 'html.parser')
 
    found_results = []
    rank = 1
    result_block = soup.find_all('div', attrs={'class': 'g'})

#    import pdb; pdb.set_trace()
    for result in result_block:
 
        link = result.find('a', href=True)
        title = result.find('h3')
        if link and title:
            link = link['href']
            title = title.get_text()
            if link != '#':
                found_results.append({ 'title': title, 'link': link })
    return found_results



if __name__ == '__main__':
    keyword, html = fetch_results('camara municipal', 500, 'pt')
    # print(html)

    data = parse_results(html)
    data = pd.DataFrame(data)
    print(data)