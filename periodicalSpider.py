# coding: utf-8
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import re
import random
import tqdm
# 将中文转换为url编码形式
from urllib.parse import quote
import utils
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


def get_page_number(response):
    """
    :param response: 网页源代码
    :return: 返回该期刊一共搜索到多少页论文 总页数
    """
    soup = BeautifulSoup(response, 'html.parser')
    try:
        # .classname查找css类，#id查找id
        page_number_str = soup.find(class_='page-number').string
        pattern = re.compile('[0-9]+')
        numList = pattern.findall(page_number_str)  # 存储两个字符串数字，代表当前页和总页数
        # current_page = int(numList[0])
        total_page = int(numList[1])
        # page_list = [current_page, total_page]
        return total_page
    except:
        print('cannot find page number')


def getAuthorListAndPubilictime(paper_url):
    """
    :param paper_url: 论文详情页url
    :return: 返回作者列表，以及期刊时间
    """
    authorList = []
    response = get_page(paper_url)
    # time.sleep(1)
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


def get_content(response):
    """
    :param response: 网页源代码
    :return: 返回当前页论文列表
    """
    soup = BeautifulSoup(response, 'html.parser')
    list_tag = soup.find_all('div', class_='normal-list')
    # 不一定有 abstract 对应的div 要记得处理
    # 如果是空值，直接用判断输出空值
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
            detailed.append(str(authorList))
        else:
            detailed.append(','.join(authorList))
        detailed.append(publicTime)
        detailed.append(abstract_detail)
        if len(keywords) == 1:
            detailed.append(str(keywords))
        else:
            detailed.append(','.join(keywords))
        result.append(detailed)


    return result


if __name__ == '__main__':

    periodicalFields = ['gyjs', 'jckx', 'jjcz', 'jkwy', 'nyws', 'shkx', 'yyws', 'zxzf']
    for field in periodicalFields:
        print('current field:', field)
        periodical_list = utils.getPeriodicalFromCSV(field)
        for periodicalName in periodical_list:
            for year in range(1998, 2020):
                url = 'http://s.wanfangdata.com.cn/periodical?q=%28%28{}%29%20%29%20Date%3A{}-{}&s=50'.format(quote('刊名:{}'.format(periodicalName)), year, year)
                response = get_page(url)
                total_number = get_page_number(response)
                print(periodicalName, '共有', total_number, '页')

                for page in range(1, total_number + 1):
                    print("当前爬取《" + periodicalName +"》第" + str(year) + "年" + "第" + str(page) + "页")
                    url = 'http://s.wanfangdata.com.cn/periodical?q=%28%28{}%29%20%29%20Date%3A{}-{}&p={}&s=50'.format(quote('刊名:{}'.format(periodicalName)), year, year, str(page))
                    attempts = 0
                    success = False
                    while attempts < 10 and not success:
                        try:
                            response = get_page(url)
                            utils.save_as_csv(get_content(response))
                            time.sleep(2 + random.randint(0, 9) * 0.1)
                            success = True
                        except:
                            print("----------爬取错误，当前爬取至" + periodicalName + "第" + str(page) + "页,正在重试:" + str(attempts) +"---------")
                            attempts += 1
                    if attempts == 10:
                        txtfile = open('./log.txt', 'a', encoding='utf-8')
                        txtfile.write(periodicalName + '第' + str(page) + '页读取错误 \n')
                        txtfile.close()




