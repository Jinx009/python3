import urllib.request

url = "http://www.800bank.com.cn"
data = urllib.request.urlopen(url).read()
data = data.decode('utf-8')
print(data)
