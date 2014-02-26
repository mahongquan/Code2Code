import urllib
fp = urllib.urlopen("http://www.baidu.com")
mybytes = fp.read()
mystr = mybytes.decode('utf-8')
print(mystr)
fp.close()
