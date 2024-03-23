import requests
import re
from bs4 import BeautifulSoup


# 章节目录和URL
def chapters(soup):
    chapters_list = []
    chapters_url_list = []
    chapters_html = soup.find("div", class_="listmain")
    chapters_url_list_html = chapters_html.find_all('a')
    for one in chapters_url_list_html:
        chapters_list.append(one.get_text())
        chapters_url_list.append(one.get('href'))
    # 判断是否是html
    for one in chapters_url_list:
        if one.endswith('html'):
            pass
        else:
            chapters_url_list.remove(one)

    return chapters_list, chapters_url_list


# 内容
def chapters_count(chapters_url):
    chapters_url = "https://www.biqg.cc" + chapters_url
    data_count = requests.get(chapters_url).text
    chapters_count_html = BeautifulSoup(data_count, 'html.parser')
    soup_count = chapters_count_html.find('div', id='chaptercontent').get_text().strip()
    chapters_content = (re.sub(r'\s+','\n', soup_count).replace('请收藏本站：https://www.biqg.cc。笔趣阁手机版：https://m.biqg.cc','')
                        .replace('『点此报错』『加入书签』',''))
    return chapters_content


# 持久化保存
def stories_preservation(novel_name, chapter,chapters_content):
    # 判断文件是否存在
    with open(novel_name + '.txt', 'a+', encoding='utf-8') as f:
        f.write(chapter + '\n' + chapters_content)


if __name__ == '__main__':
    url = 'https://www.biqg.cc/book/28686/'
    data = requests.get(url).text
    # 解析html
    soup = BeautifulSoup(data, 'html.parser')

    # 小说名字
    novel_name = soup.find('span', class_='title').get_text()

    chapter_list,chapters_url_list = chapters(soup)
    for one in range(len(chapters_url_list)):
        chapters_content = chapters_count(chapters_url_list[one])
        stories_preservation(novel_name, chapter_list[one], chapters_content)

