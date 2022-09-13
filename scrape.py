import requests
import os
import time
from datetime import datetime

folder = datetime.now().strftime('%Y%m%d%H%M%S') #creating folder with date+time to make unique name
iterations = int(input("\nHow many images do you want to scrape? "))
os.mkdir(folder) #creating new folder everytime so that images don't get overridden

print ("\nDirectory created with name {}".format(folder)) 
def download(fileName):
    file = open(os.path.join(folder, fileName),'wb')
    file.write(requests.get('https://thispersondoesnotexist.com/image', headers={'User-Agent': 'My User Agent 1.0'}).content)
    file.close()
    print ("\n\t{} created".format(fileName))
    time.sleep(1)

for i in range(iterations):
     download(str(i+1)+'.jpg')

print ("\n{} images successfully generated!".format(iterations))
input("\nPress Enter to exit...")
