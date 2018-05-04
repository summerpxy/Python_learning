import os
import requests


def save_picture(url, name):
    response = requests.get(url, stream=True)
    if response.status_code == requests.codes.ok:
        dir_path = os.path.join("f:", os.sep, "gank")
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        os.chdir(dir_path)
        with open(name, "wb") as fd:
            for chunk in response.iter_content(1024):
                fd.write(chunk)
        fd.close()


def get_json_object(url):
    response = requests.get(url)
    item = 1
    if response.status_code == requests.codes.ok:
        res_josn = response.json()
        res_list = list(res_josn["results"])
        for items in res_list:
            pic_url = items["url"]
            print(pic_url)
            save_picture(pic_url, "pic" + str(item) + ".jpg")
            item += 1


if __name__ == "__main__":
    get_json_object("http://gank.io/api/data/福利/20/1")
