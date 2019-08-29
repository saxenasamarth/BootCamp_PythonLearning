import asyncio
import time
import aiohttp

async def download_image(session, url):
	async with session.get(url) as response:
		if response.status == 200:
			fname = url.split("/")[-1]
			f = await aiofiles.open(fname, mode='wb')
			await f.write(await response.read())
			await f.close()


async def download_all_images(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(download_image(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
	url_list = ["https://cdn.images.express.co.uk/img/dynamic/72/590x/secondary/Roger-Federer-currently-uses-Wilson-s-RF27-racket-1972731.jpg", "https://cdn.images.express.co.uk/img/dynamic/72/590x/Roger-Federer-1155298.jpg", "https://cdn.cnn.com/cnnnext/dam/assets/190712191829-federer-fist-pump-large-169.jpg", "https://i0.wp.com/metro.co.uk/wp-content/uploads/2019/07/GettyImages-1155382712.jpg", "https://cdn.images.express.co.uk/img/dynamic/72/590x/Roger-Federer-1155713.jpg", "https://b.fssta.com/uploads/2019/07/djokovicfedererfull.jpg", "http://media.bongdapro.vn/application/admin/image/2019/07/15/roger-federer-novak-djokovic-wimbledon-1.jpg", "https://nbcolympictalk.files.wordpress.com/2019/07/federer-e1562958774822.jpg", "https://english.cdn.zeenews.com/sites/default/files/2019/02/10/760961-754070-752047-federerroger.jpg"]
	start_time = time.time()
	asyncio.get_event_loop().run_until_complete(download_all_images(url_list))
	end_time = time.time()
	print("Time taken = {}".format(end_time-start_time))