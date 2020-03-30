import urllib.request

try:
    url=urllib.request.urlopen("https://www.python.org/")
    content=url.read()
except urllib.error.HTTPError:
    print("url not found!")
    exit("1")

f=open("python.html", "ab")
f.write(content)
f.close()

a="https://www.python.org/static/img/python-logo@2x.png"
img=urllib.request.urlretrieve(a,"python.png") #can out url instead of a