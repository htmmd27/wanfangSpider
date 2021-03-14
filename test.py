# coding: utf-8
import random
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import re
from urllib.parse import quote
# 配置浏览器设置
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=chrome_options)

def get_page(url):
    """
    :param url: 网页url
    :return: 返回网页选然后的html代码
    """
    driver.get(url)
    response = driver.page_source
    return response


def getAuthorListAndPubilictime(paper_url):
    """
    :param paper_url: 论文详情页url
    :return: 返回作者列表，以及期刊时间
    """
    authorList = []
    response = get_page(paper_url)
    time.sleep(1 + random.randint(0, 9) * 0.1)
    soup = BeautifulSoup(response, 'html.parser')
    author_area = soup.find('div', class_='author list')
    if author_area is not None:
        author_list = author_area.find_all('a')  # 作者列表
        for tag in author_list:
            authorList.append(tag.text.strip())
    elif author_area is None:
        authorList.append('No Author')
    pubicTime_area = soup.find('div', class_='getYear list')
    publicTime = pubicTime_area.text  # 期刊发表时间

    return authorList, publicTime
'''
将中文转换为url编码形式
'''
periodical = '刊名:计算机学报'
url = 'http://s.wanfangdata.com.cn/periodical?q=%28%28{}%29%20%29%20Date%3A{}-{}&p={}&s=50'.format(
    quote('刊名:{}'.format('石油勘探与开发')), 2020, 2020, str(2))

driver.get(url)
response = driver.page_source
soup = BeautifulSoup(response, 'html.parser')
page_number_str = soup.find(class_='page-number').string
pattern = re.compile('[0-9]+')
numList = pattern.findall(page_number_str)  # 存储两个字符串数字，代表当前页和总页数
# current_page = int(numList[0])
total_page = int(numList[1])
print(total_page)
soup = BeautifulSoup(response, 'html.parser')
list_tag = soup.find_all('div', class_='normal-list')
print(len(list_tag))
result = []
for tag in list_tag:
    detailed = []
    title_area = tag.find('div', class_='title-area')
    author_area = tag.find('div', class_='author-area')
    abstract_area = tag.find('div', class_='abstract-area')
    keywords_area = tag.find('div', class_='keywords-area')
    periodical_title_area = author_area.find('span', class_='periodical-title')
    # 存储论文url以及名称
    paper_url = title_area.a['href']  # 存储论文url
    paper_name = title_area.a.string  # 存储论文名称

    # 存储期刊名称
    periodical_title = periodical_title_area.string.strip('《》')

    # 存储论文作者，以及发刊时间
    # 搜索页面作者信息显示不全，需要进入论文界面将作者名称进行提取
    authorList, publicTime = getAuthorListAndPubilictime(paper_url)

    # 存储论文摘要
    abstract_detail = ''
    if abstract_area is not None:
        abstract_detail = abstract_area.span.next_sibling.string
    elif abstract_area is None:
        abstract_detail = 'No Abstract'  # 如果摘要为空，存储空值

    # 存储论文关键词,是一个列表
    keywords = []
    keywords_tag = keywords_area.find_all('span', class_='keywords-list')
    if keywords_tag is not None:
        for keyword in keywords_tag:
            keywords.append(keyword.string)
    elif keywords_tag is None:
        keywords.append('No Keyword')
    detailed.append(periodical_title)
    detailed.append(paper_name)
    detailed.append(paper_url)
    if len(authorList) == 1:
        detailed.append(authorList)
    else:
        detailed.append(','.join(authorList))
    detailed.append(publicTime)
    detailed.append(abstract_detail)
    if len(keywords) == 1:
        detailed.append(keywords)
    else:
        detailed.append(','.join(keywords))
    result.append(detailed)
    for i in result:
        print(i)

# url = 'http://d.wanfangdata.com.cn/periodical/ChlQZXJpb2RpY2FsQ0hJTmV3UzIwMjEwMzAyEg14emp5MjAyMTAxMDA3GghxZnU4ejZiZg%3D%3D'
# driver.get(url)
# response = driver.page_source
# soup = BeautifulSoup(response, 'html.parser')
# author_area = soup.find('div', class_='author list')
# author_list = author_area.find_all('a')
# for tag in author_list:
#     print(tag.text.strip())
# pubicTime_area = soup.find('div', class_='getYear list')
# publicTime = pubicTime_area.a.text
# print(publicTime)
# print('《史丹阳》'.strip('《》'))