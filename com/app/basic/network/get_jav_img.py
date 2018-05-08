import bs4
import requests
import os
import re
import shutil


# 1.获取所选页面的信息
# 2.解析当前页面的信息，包括所有的大图地址和下一页的地址
# 3.下载大图的图片
# 4.访问下一页的地址

def get_page_info(url):
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        page_txt = response.text
        bs_info = bs4.BeautifulSoup(page_txt, "lxml")
        # 解析大图的地址
        pic_infos = bs_info.select(".video > a")
        url_regx = re.compile("(?<=./).*")
        for pic in pic_infos:
            big_pic_url = "http://www.ja16b.com/cn/" + url_regx.search((pic["href"])).group()
            title = pic["title"]
            parse_big_url(big_pic_url, title + ".jpg")
        # 解析下一页地址
        next_info = bs_info.select("a.page.next")
        if len(next_info) == 0:
            return
        else:
            next_url = "http://www.ja16b.com" + next_info[0]["href"]
            get_page_info(next_url)


def parse_big_url(url, name):
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        page_txt = response.text
        bs_info = bs4.BeautifulSoup(page_txt, "lxml")
        pic_info = bs_info.select("div #video_jacket > img")
        big_pic_url = "http:" + pic_info[0]["src"]
        save_pic(big_pic_url, name)


def save_pic(url, name):
    dest_path = os.path.join("f:", os.sep, "abp")
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    response = requests.get(url, stream=True)
    if response.status_code == requests.codes.ok:
        with open(os.path.join(dest_path, name), "wb") as fd:
            for chunk in response.iter_content(1024):
                fd.write(chunk)
        fd.close()


def _save_page(url):
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        path_save = os.path.join("f:", os.sep, "save.html")
        with open(path_save, "wb") as fd:
            for chunk in response.iter_content(1024):
                fd.write(chunk)
        fd.close()


if __name__ == "__main__":
    get_page_info("http://www.ja16b.com/cn/vl_searchbyid.php?keyword=abp")
    # _save_page("http://www.ja16b.com/cn/vl_searchbyid.php?keyword=abp")
