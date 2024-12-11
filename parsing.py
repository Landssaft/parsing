import requests
import bs4


HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language': 'ru,en;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '_ym_d=1726313558; _ym_uid=1726313558740160997; _ga=GA1.1.1451052522.1726313557; fl=ru; hl=ru; feature_streaming_comments=true; _gid=GA1.2.1944230597.1733753777; habr_web_home=ARTICLES_LIST_ALL; _ym_isad=2; visited_articles=849788; SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1',
'Host': 'habr.com',
'sec-ch-ua': '"Chromium";v="133.0.6869.0", "Yandex";v="24.12.1.94", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests':'1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 YaBrowser/24.10.0.0 Safari/537.36'}




KEYWORDS = ['дизайн', 'фото', 'web', 'python']
response = requests.get('https://habr.com/ru/articles/', headers=HEADERS)
response.raise_for_status()
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article', class_='tm-articles-list__item')


for article in articles:
    link = 'https://habr.com/ru/articles/'
    article_response = requests.get(link)
    article_soup = bs4.BeautifulSoup(article_response.text, features='lxml')
    date = article_soup.select_one('time')
    span_title = article_soup.select_one('h1').text
    url = article_soup.select_one('a.tm-title__link')

    if KEYWORDS:
        print(f'Дата: {date} - Заголовок: {span_title} - Ссылка: {url}')

        #< a
        #href = "/ru/companies/reksoft/articles/865452/"


#<time datetime="2024-12-11T11:17:31.000Z" title="2024-12-11, 14:17">10 минут назад</time>