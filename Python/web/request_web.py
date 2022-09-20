"""网络请求"""
import requests


url = "https://www.baidu.com"
# 有些网站会现在，但可伪装浏览器爬取 浏览器User-Agent的详细信息(可采用下面的进行爬虫伪装)
# 浏览器头信息代理可以直接搜Http Header之User-Agent，以下是谷歌浏览器的
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0"
}
# 使用requests方法


def download_webpage(url, headers):
    """下载网页"""
    response = requests.get(url)
    response.encoding = 'utf-8'

    # 使用伪装浏览器的urllib方法
    #response = requests.get(url,headers=headers)
    data = response.text
    file_path = "test.html"

    with open(file_path, "w", encoding='utf-8') as f:
        f.write(data)


if __name__ == '__main__':
    download_webpage(url, headers)
