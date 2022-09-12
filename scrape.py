import requests

def download(fileName):
    file = open(fileName,'wb')
    file.write(requests.get('https://thispersondoesnotexist.com/image', headers={'User-Agent': 'My User Agent 1.0'}).content)
    file.close()

for i in range(30):
    download(str(i)+'.jpg')
