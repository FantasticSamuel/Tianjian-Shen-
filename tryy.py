import requests
from bs4 import BeautifulSoup

header={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76"}
for i in range(0,250,25):
    response=requests.get(f"https://movie.douban.com/top250?start={i}&filter=",headers=header)
    soup=BeautifulSoup(response.text,"html.parser")
    titles=soup.findAll("span",attrs={"class":"title"})
    for title in titles:
        str=title.string
        if "/" not in str:
            print(str)

