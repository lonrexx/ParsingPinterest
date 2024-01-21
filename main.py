import requests
import os
from bs4 import BeautifulSoup

def find_and_download_image(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()


        soup = BeautifulSoup(response.content, 'html.parser')
        
        div_element = soup.find('div', class_='XiG zI7 iyn Hsu')

        image_url = div_element.find('img')['src']

        response_image = requests.get(image_url, stream=True)
        response_image.raise_for_status()

        with open(save_path, 'wb') as file:
            for chunk in response_image.iter_content(chunk_size=8192):
                file.write(chunk)


    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")