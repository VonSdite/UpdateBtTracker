import requests

import os
import sys
path = os.path.split(os.path.abspath(sys.argv[0]))[0]
import logging
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler(os.path.join(path, "log.txt"))
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

confFile = '/root/.aria2/aria2.conf'

trackerUrl = 'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

def getBtTracker():
    res = requests.get(url=trackerUrl, headers=headers)
    btTrackerData = res.text.replace('\n\n', ',')
    return btTrackerData[:-1]

def updateFile(fileName, data):
    # 将文件读取到内存中
    with open(fileName, "r", encoding="utf-8") as f:
        lines = f.readlines() 

    # 写的方式打开文件
    with open(fileName, "w", encoding="utf-8") as f_w:
        for line in lines:
            if "bt-tracker" in line:
                # 替换
                line = data
            f_w.write(line)


if __name__ == '__main__':
    try:
        btTrackerData = "bt-tracker=" + getBtTracker()
        updateFile(confFile, btTrackerData)
        logger.info('更新bt-tracker成功')

    except:
        logger.error('更新bt-tracker失败')

