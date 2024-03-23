import encodings.utf_8

import requests
from bs4 import BeautifulSoup
import re
import os
from lxml import etree
import time


# 批量url
def get_urls(page):
    # for one in range(page+1):
    #     # 除掉0和1
    #     if one == 0:
    #         urls = "https://pic.netbian.com/4kmeinv/"
    #         html = get_xpath_html(urls)
    #         print(one)
    #         # return html
    #     elif one == 1:
    #         pass
    #     else:
    #         urls = "https://pic.netbian.com/4kmeinv/index_%s.html" % one
    #         html = get_xpath_html(urls)
    #         # return 2
    #         print("as%s" % one)
    pass


# 解析
def get_xpath_html(url):
    html_text = requests.get(url).text
    # soup = BeautifulSoup(html_text, 'html.parser')
    # print(soup)
    html = etree.HTML(html_text)
    return html


# 获取图片和图片名称
def get_html(html):
    html_one = html.xpath('//ul[@class="clearfix"]/li/a')
    img_name_list = []
    img_src_list = []
    for one in html_one:
        img_src = "https://pic.netbian.com" + one.xpath('./img/@src')[0]
        img_name = one.xpath('./img/@alt')[0] + '.jpg'
        img_name = img_name.encode('ISO-8859-1').decode('gbk')
        img_name_list.append(img_name)
        img_src_list.append(img_src)
    return img_src_list,img_name_list,


# 获取最大页数
def get_url_page(url):
    html = get_xpath_html(url)
    url_list = html.xpath('//div[@class="page"]/a/text()')
    urls = []
    for one in url_list:
        # 修改编码
        two = one.encode('ISO-8859-1').decode('gbk')
        try:
            # 判断是否为数字
            if two.isdigit():
                urls.append(int(two))
        except Exception as e:
            print(e)
    return max(urls)


# 保存
def save_img(html):
    img_src, img_name = get_html(html)
    if not os.path.isdir("D:/python/study/Crawler/美女图片/4kmeinv_img"):
        os.makedirs("4kmeinv_img")
    else:
        for one in range(len(img_src)):
            # 文件名内不能含有特殊字符*
            img_names = img_name[one].replace(" ", "").replace('*',"x")
            # save_img(img_names, img_src[one])
            data = requests.get(img_src[one]).content
            with open("./4kmeinv_img/" + img_names, "wb") as f:
                f.write(data)
                print("保存完毕：",img_src[one])


if __name__ == '__main__':
    url = 'https://pic.netbian.com/4kmeinv/'
    page = get_url_page(url)
    for one in range(page+1):
        # 除掉0和1
        if one == 0:
            urls = "https://pic.netbian.com/4kmeinv/"
            html = get_xpath_html(urls)
            save_img(html)
            print("第%d页保存完毕" % (one+1))
            time.sleep(3)
        elif one == 1:
            pass
        else:
            urls = "https://pic.netbian.com/4kmeinv/index_%s.html" % one
            html = get_xpath_html(urls)
            save_img(html)
            print("第%d页保存完毕" % (one+1))
            time.sleep(3)


