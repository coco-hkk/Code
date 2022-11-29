import requests
import parsel
import time

def check_ip(proxies):
    """检测代理有效性"""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

    valid_ip = []
    for ip in proxies:
        try:
            response = requests.get(url="https://www.baidu.com", headers=headers, proxies=ip, timeout=1)
            if response.status_code == 200:
                valid_ip.append(ip)
        except:
            print('当前代理：', ip, "请求超时，检测不合格")
        else:
            print("当前代理：", ip, "检测通过")
    
    return valid_ip


proxies_list = []

for page in range(1, 11):
    """
    代理格式
    {
        'http': 'http://' + ip:port,
        'https': 'https://' + ip:port,
    }
    """

    time.sleep(1)
    print(f"==============正在请求第 {page} 页=========================")
    url = f'https://www.kuaidaili.com/free/intr/{page}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

    response = requests.get(url=url, headers=headers)
    html_data = response.text

    # 将 html_data 字符串类型转换为对象
    selector = parsel.Selector(html_data)
    # 可在 chrome 使用 xpath helper 插件解析 xpath
    trs = selector.xpath('//*[@id="list"]/table/tbody/tr')

    for tr in trs:
        ip = tr.xpath('./td[1]/text()').get()
        port = tr.xpath('./td[2]/text()').get()
        ip_proxy = ip + ":" + port

        proxies_dict = {
            'http': 'http://' + ip_proxy,
            'https': 'https://' + ip_proxy,
        }

        proxies_list.append(proxies_dict)
    print(proxies_list)

print("获取代理数量：", len(proxies_list))

print("=====================正在检测ip质量===================")
valid_ip = check_ip(proxies_list)
print('质量高的代理', valid_ip)
print('高质量的代理数量', len(valid_ip))