import requests

url = "https://www.ymori.com/books/python2nen/test1.html"
response = requests.get(url)

# 文字コードをUTF-8に設定
response.encoding = "UTF-8"

filename = "download.txt"
with open(filename, mode="w", encoding="UTF-8") as f:
    f.write(response.text)

