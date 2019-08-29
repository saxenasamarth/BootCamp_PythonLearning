from concurrent.futures import ThreadPoolExecutor
import time
from urllib.request import urlopen, Request

def download_image(url):
	with urlopen(url) as image:
		fname = url.split("/")[-1]
		f = open(fname, "wb")
		f.write(image.read())
		f.close()
		print('Downloaded ', fname)


url_list = ["https://cdn.images.express.co.uk/img/dynamic/72/590x/secondary/Roger-Federer-currently-uses-Wilson-s-RF27-racket-1972731.jpg", "https://cdn.images.express.co.uk/img/dynamic/72/590x/Roger-Federer-1155298.jpg", "https://cdn.cnn.com/cnnnext/dam/assets/190712191829-federer-fist-pump-large-169.jpg", "https://i0.wp.com/metro.co.uk/wp-content/uploads/2019/07/GettyImages-1155382712.jpg", "https://cdn.images.express.co.uk/img/dynamic/72/590x/Roger-Federer-1155713.jpg", "https://b.fssta.com/uploads/2019/07/djokovicfedererfull.jpg", "http://media.bongdapro.vn/application/admin/image/2019/07/15/roger-federer-novak-djokovic-wimbledon-1.jpg", "https://nbcolympictalk.files.wordpress.com/2019/07/federer-e1562958774822.jpg", "https://english.cdn.zeenews.com/sites/default/files/2019/02/10/760961-754070-752047-federerroger.jpg"]

start_time = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(download_image, url_list)
end_time = time.time()
print("Time taken = {}".format(end_time-start_time))


start_time=time.time()
for url in url_list:
	download_image(url)
end_time=time.time()
print("Time taken = {}".format(end_time-start_time))