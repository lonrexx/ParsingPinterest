import aiohttp
import aiofiles
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

async def download(url, user_id):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()

                soup = BeautifulSoup(await response.text(), 'html.parser')

                div_element = soup.find('div', class_='XiG zI7 iyn Hsu')
                img_element = div_element.find('img', class_='hCL kVc L4E MIw')

                image_url = img_element['src']
                image_title = img_element['alt'] if 'alt' in img_element.attrs else 'No title'

                async with session.get(image_url) as response_image:
                    response_image.raise_for_status()

                    gif_data = BytesIO(await response_image.read())

                    async with aiofiles.open(f'images/{user_id}_{image_title}.gif', 'wb') as file:
                        await file.write(gif_data.getvalue())

                        return image_title
    except aiohttp.ClientError as e:
        print(f"Ошибка при выполнении запроса: {e}")