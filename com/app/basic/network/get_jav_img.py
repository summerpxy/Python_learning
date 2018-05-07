import bs4
import requests


# 1.获取所选页面的信息
# 2.解析当前页面的信息，包括所有的大图地址和下一页的地址
# 3.下载大图的图片
# 4.访问下一页的地址

def get_page_info(url):
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        page_txt = response.text
        bs_info = bs4.BeautifulSoup(page_txt, "lxml")


if __name__ == "__main__":
    pass
