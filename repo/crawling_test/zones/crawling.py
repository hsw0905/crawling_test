import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from .models import CarZone


class Crawling:
    driver = webdriver.Chrome('/Users/seonwoong-hwang/Downloads/chromedriver')
    driver.implicitly_wait(5)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/83.0.4103.106 Safari/537.36 '
    }

    # 쏘카존 안내 - 현재 서울지역 총 페이지 수
    total_page = 245
    for page_index in range(total_page):

        # 쏘카존 안내 - 예) 서울 탭 1페이지
        driver.get(f'https://blog.socar.kr/category/쏘카존 안내/서울?page={page_index + 1}')

        # 페이지 당 쏘카존 상세 페이지 URL 추출
        html_depth_1 = requests.get(f'https://blog.socar.kr/category/쏘카존 안내/서울?page={page_index + 1}',
                                    headers=headers).text
        soup_depth_1 = BeautifulSoup(html_depth_1, 'html.parser')
        detail_pages = soup_depth_1.find_all('a', {'class': 'ellipsis'})

        # 상세 페이지 접근하여 DB 저장
        for i in detail_pages:
            target_base_url = 'https://blog.socar.kr'
            detail_page_url = target_base_url + i['href']

            html_depth_2 = requests.get(detail_page_url, headers=headers).text
            soup_depth_2 = BeautifulSoup(html_depth_2, 'html.parser')

            zone_informations = soup_depth_2.find_all('span', {'style': 'font-size: 16px; letter-spacing: -0.5px;'})

            # 예외 사항
            if not zone_informations:
                zone_informations = soup_depth_2.find_all('span', {'style': 'font-size: 11pt; letter-spacing: -0.5px;'})
                break

            zone_address = zone_informations[0].text
            zone_detail = zone_informations[1].text


            CarZone.objects.get_or_create(address=zone_address, detail=zone_detail)

    driver.close()

start_crawling = Crawling()
start_crawling
