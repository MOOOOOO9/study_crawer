import encodings.utf_8

import requests
from bs4 import BeautifulSoup
import re
import os
from lxml import etree
import time


# 批量下载
def get_urls(url):
    page = get_url_page(url)
    print(page)
    for one in range(page + 1):
        # 除掉0和1
        if one == 0:
            urls = "https://pic.netbian.com/%s/" % opt
            html = get_xpath_html(urls)
            save_img(html, opt)
            print("第%d页保存完毕" % (one + 1))
            time.sleep(3)
        elif one == 1:
            pass
        else:
            urls = "https://pic.netbian.com/%s/index_%s.html" % (opt, one)
            html = get_xpath_html(urls)
            save_img(html, opt)
            print("第%d页保存完毕" % one)
            time.sleep(3)


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
def save_img(html, opt):
    img_src, img_name = get_html(html)
    if not os.path.isdir("D:/python/study/Crawler/美女图片/%s_img" % opt):
        os.makedirs("%s_img" % opt)
    else:
        for one in range(len(img_src)):
            # 文件名内不能含有特殊字符*
            img_names = img_name[one].replace(" ", "").replace('*',"x")
            # save_img(img_names, img_src[one])
            data = requests.get(img_src[one]).content
            with open("./%s_img/" % opt + img_names, "wb") as f:
                f.write(data)
                print("保存完毕：", img_src[one])


def main():
    print("----------------------------")
    print("----------1、4K动漫----------")
    print("----------2、4K游戏----------")
    print("----------3、4K美女----------")
    print("----------4、4K风景----------")
    print("----------5、4K影视----------")
    print("----------6、4K汽车----------")
    print("----------7、4K人物----------")
    print("----------8、4K动物----------")
    print("----------9、4K宗教----------")
    print("----------10、4K背景---------")
    print("---------11、平板壁纸---------")
    print("---------12、4K手机壁纸-------")
    print("----------------------------")


if __name__ == '__main__':
    while True:
        main()
        opts = input("请输入你需要图片分类：")
        os.system("cls")
        if opts == '1':
            opt = '4kdongman'
            url = 'https://pic.netbian.com/%s/' % opt
            get_urls(url)
        elif opts == '2':
            opt = '4kyouxi'
            url = 'https://pic.netbian.com/%s/' % opt
            get_urls(url)
        elif opts == '3':
            opt = '4kmeinv'
            url = 'https://pic.netbian.com/%s/' % opt
            get_urls(url)


