import urllib.request, re, gzip
from bs4 import BeautifulSoup


def save_file(data, i):
    path = "data"+str(i)+".txt"
    file = open(path, 'wb+')
    page = '当前页：'+str(i+1)+'\n'
    file.write(page.encode('utf-8'))
    for d in data:
        d = str(d)+'\n'
        file.write(d.encode('utf-8'))
    file.close()


def ungzip(data):
    try:
        data = gzip.decompress(data)
    except:
        print("未经压缩，无需解压...")
    return data


class CSDNSpider:
    def __init__(self, page_idx=1, url="http://blog.csdn.net/wow4464/article/list/1"):
        self.page_idx = page_idx
        self.url = url[0:url.rfind('/') + 1] + str(page_idx)
        self.headers = {
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Host": "blog.csdn.net"
        }

    def get_pages(self):
        req = urllib.request.Request(url=self.url, headers=self.headers)
        page = urllib.request.urlopen(req)

        data = page.read()
        data = ungzip(data)
        data = data.decode('utf-8')

        soup = BeautifulSoup(data,'html5lib')
        tag = soup.find('div',"pagelist")
        pages_data = tag.span.get_text()
        pages_num = re.findall(re.compile(pattern=r'共(.*?)页'),pages_data)[0]
        return pages_num

    def set_page(self, idx):
        self.url = self.url[0:self.url.rfind('/')+1]+str(idx)

    def read_data(self):
        ret = []
        req = urllib.request.Request(url=self.url, headers=self.headers)
        res = urllib.request.urlopen(req)

        data = res.read()
        data = ungzip(data)
        data = data.decode('utf-8')

        soup=BeautifulSoup(data, "html5lib")
        #找到所有的博文代码模块
        items = soup.find_all('div', "list_item article_item")
        for item in items:
            #标题、链接、日期、阅读次数、评论个数
            title = item.find('span', "link_title").a.get_text()
            link = item.find('span', "link_title").a.get('href')
            write_time = item.find('span', "link_postdate").get_text()
            readers = re.findall(re.compile(r'\((.*?)\)'),item.find('span',"link_view").get_text())[0]
            comments = re.findall(re.compile(r'\((.*?)\)'),item.find('span',"link_comments").get_text())[0]

            ret.append('日期：'+write_time+'\n标题：'+title
                       +'\n链接：http://blog.csdn.net'+link
                       +'\n'+'阅读：'+readers+'\t评论：'+comments+'\n')
        return ret

cs = CSDNSpider()
pagesNum = int(cs.get_pages())
print("博文总页数： ", pagesNum)

for idx in range(pagesNum):
    cs.set_page(idx)
    print("当前页：", idx+1)
    papers = cs.read_data()
    save_file(papers, idx)

