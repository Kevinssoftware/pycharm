import fileinput
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup


def downonepage(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44"
    }
    resp = requests.get(url, headers=headers)
    resp.encoding = "utf-8"
    '''2.数据获取
        数据初始化
        图片url获取'''

    main_page = BeautifulSoup(resp.text, "html.parser")
    alist = main_page.find_all("div", class_="img_single")
    for a in alist:
        p = a.find("img")
        src = p.get("src")
        img_resp = requests.get(src)
        img_name = src.split("/")[-1]
        with open(img_name, mode="wb") as f:
            f.write(img_resp.content)
            print("successful")





if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        for i in range(1,200):
            t.submit(downonepage,f"https://www.buxiuse.com/?cid=7&page={i}")
f.close()
print("over")

"""多线程爬小姐姐丝袜图片，速度极快"""