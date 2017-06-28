import urllib.request

data = {}
data['word'] = 'Jinx'

url_values = urllib.parse.urlencode(data)
url = "http://www.baidu.com/s?"
full_url = url + url_values
print(full_url)
data = urllib.request.urlopen(full_url).read()
data = data.decode('UTF-8')
print(data)