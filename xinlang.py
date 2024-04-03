import requests
import json

# 由于批量获取URL，所以page那我用{}
url = ('https://feed.sina.com.cn/api/roll/get?pageid=121&lid=1356&num=20&'
       'versionNumber=1.2.4&page={}&encode=utf-8&callback=feedCardJsonpCallback&_=1712079687912')

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
}


def get_title():
    data = requests.get(urls, headers=header, timeout=20).text
    rel = data.split("try{feedCardJsonpCallback(")[1].split(');}catch(e){};')[0]
    rel_js = json.loads(rel)
    data_get = rel_js["result"]['data']
    title = []
    for i in range(len(data_get)):
        # print(data_get[one]['wapurl'])
        titles = data_get[i]['title'] + " " + data_get[i]['wapurl']
        title.append(titles)
    return title


def save_file(data):
    with open('news.txt','a+',encoding='utf-8') as f:
        f.write(data)
        f.write('\n')


if __name__ == '__main__':
    # 获取新浪新闻里面国内新闻标题和URL
    for one in range(1, 10):
        urls = url.format(one)
        print("写入第%s页" %one)
        title = get_title()
        for i in range(len(title)):
            save_file(title[i])
        print("第%s页保存完毕" %one)

