from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time, requests
import urllib
today_date = time.strftime("%d+%b+%Y")
yesterday = datetime.now() - timedelta(days=1)
yesterday_date = yesterday.strftime('%d+%b+%Y')
first_page_url = 'http://www.espncricinfo.com/ci/content/image/?datefrom='+yesterday_date+'&dateupto='+today_date+';'
print(first_page_url)
r = requests.get(first_page_url)
soup = BeautifulSoup(r.text, 'html.parser')
images = soup.find_all('div', class_='picture')
for image in images:
    url = "http://www.espncricinfo.com/" + image.find('a').get('href')
    print(url)
    r1 = requests.get(url)
    soup1 = BeautifulSoup(r1.text, 'html.parser')
    image1 = soup1.find('li', class_='box1')
    url = image1.get("data-image-id")
    open(url.split("/")[-1], 'wb').write(requests.get(url, allow_redirects=True).content)