import requests

iterations = int(input("How many images do you want to scrape? "))


def download(fileName):
    file = open(fileName,'wb')
    file.write(requests.get('https://thispersondoesnotexist.com/image', headers={'User-Agent': 'My User Agent 1.0'}).content)
    file.close()

for i in range(iterations):
    download(str(i)+'.jpg')
