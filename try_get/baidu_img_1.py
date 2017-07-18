import requests
import os
import time


def get_many_pages(keyword, pages):
    params = []
    for i in range(30, 30*pages+30, 30):
        params.append({
                      'tn': 'resultjson_com',
                      'ipn': 'rj',
                      'ct': 201326592,
                      'is': '',
                      'fp': 'result',
                      'queryWord': keyword,
                      'cl': 2,
                      'lm': -1,
                      'ie': 'utf-8',
                      'oe': 'utf-8',
                      'adpicid': '',
                      'st': -1,
                      'z': '',
                      'ic': 0,
                      'word': keyword,
                      's': '',
                      'se': '',
                      'tab': '',
                      'width': '',
                      'height': '',
                      'face': 0,
                      'istype': 2,
                      'qc': '',
                      'nc': 1,
                      'fr': '',
                      'pn': i,
                      'rn': 30,
                      'gsm': '1e',
                      '1488942260214': ''
                  })
    url = 'https://image.baidu.com/search/acjson'
    urls = []
    for i in params:
        urls.append(requests.get(url, params=i).json().get('data'))

    return urls


def get_img(data_list, local_path):

    if not os.path.exists(local_path):  # 新建文件夹
        os.mkdir(data_list)

    _time = time.time()
    x = 0
    for _list in dataList:
        for i in _list:
            if i.get('thumbURL') is not None:
                _time = _time + x
                print('正在下载：%s' % i.get('thumbURL'))
                ir = requests.get(i.get('thumbURL'))
                open(local_path + '%d.jpg' % _time, 'wb').write(ir.content)
                x += 1
            else:
                print('图片链接不存在')

if __name__ == '__main__':
    dataList = get_many_pages('丝袜', 10)
    get_img(dataList, '/Users/jinx/Downloads/img/sw/')

