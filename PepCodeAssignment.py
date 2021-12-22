import requests
from bs4 import bs
url = "https://en.wikipedia.org/wiki/S"
menu=int(input("Press 1 for Name \n press 2 for History "))
lis=['Name','History']
content = requests.get(url)
soup = bs(content.text, 'html.parser')
data = soup.find_all('p')
if menu-1 ==0:
    for i in range(4,8):
        print(data[i].text.strip())
elif menu-1==1:
    for i in range(8,15):
        print(data[i].text.strip())


