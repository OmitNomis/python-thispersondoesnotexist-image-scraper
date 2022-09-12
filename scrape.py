import requests
import os
from datetime import datetime

folder = datetime.now().strftime('%Y%m%d%H%M%S')
iterations = int(input("\n\tHow many images do you want to scrape? "))
os.mkdir(folder)

print ("\n\tDirectory created with name {}".format(folder))
def download(fileName):
    file = open(os.path.join(folder, fileName),'wb')
    file.write(requests.get('https://thispersondoesnotexist.com/image', headers={'User-Agent': 'My User Agent 1.0'}).content)
    file.close()
    print ("\n\t{} created".format(fileName))

for i in range(iterations):
     download(str(i)+'.jpg')
