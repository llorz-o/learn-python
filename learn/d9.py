from time import time
from threading import Thread
from pathlib import Path

import os
import requests

# 实现 Thread 类,进行多线程调用


class DownloadHandler(Thread):

    def __init__(self, urls):
        super().__init__()
        self.urls = urls

    def run(self):
        for url in self.urls:
            filename = url[url.rfind('sig') + 4:]
            resp = requests.get(url)
            with open('download_images/' + filename + '.jpg', 'wb') as f:
                f.write(resp.content)


def main():
    resp = requests.get('https://api.500px.com/v1/photos?feature=popular')
    data_model = resp.json()
    for photos in data_model['photos']:
        urls = photos['image_url']

        def download():
            for url in urls:
                filename = url[url.rfind('sig') + 4:]
                resp = requests.get(url)
                with open('./learn/download_images/' + filename + '.jpg', 'wb') as f:
                    f.write(resp.content)

        download_images_dir = Path("./learn/download_images")

        if download_images_dir.exists():
            download()
        else:
            os.system("mkdir " + "./learn/download_images")
            download()


if __name__ == '__main__':
    main()
